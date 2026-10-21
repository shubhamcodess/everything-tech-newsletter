"""Replays past editions through scripts/dedupe.py to measure repeat detection.

    python scripts/eval_dedupe.py

For each day it rebuilds what build_candidates.py would have seen (that day's
editions/<date>/candidates.md), takes the stories featured in the previous
dedup_lookback_days as the "already ran" list, and checks which candidate
clusters would have been tagged POSSIBLE REPEAT.

KNOWN_REPEATS are same-event pairs found by reading the archive by hand
(date, story rank) -- the same event published again under a different URL.
Recall is how many of them would have been tagged against the right earlier
story. The per-day tag count is the cost: each tag is one more thing the editor
has to read. Editions before the 'event' field have no keywords, so this only
exercises the title matching; events add to it on top.
"""
import glob
import os
import re
import sys
from datetime import date as Date, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dedupe  # noqa: E402
import edition_md  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (earlier date, rank, later date, rank): same event, different URLs.
KNOWN_REPEATS = [
    ("2026-09-25", 3, "2026-09-26", 10), ("2026-10-14", 23, "2026-10-20", 8),
    ("2026-10-10", 2, "2026-10-11", 3), ("2026-10-10", 2, "2026-10-13", 2), ("2026-10-11", 3, "2026-10-13", 2),
    ("2026-10-01", 4, "2026-10-02", 2), ("2026-10-08", 19, "2026-10-09", 25),
    ("2026-10-11", 12, "2026-10-12", 7), ("2026-10-07", 3, "2026-10-12", 7), ("2026-10-07", 3, "2026-10-11", 12),
    ("2026-10-16", 4, "2026-10-17", 6), ("2026-10-04", 17, "2026-10-09", 13),
    ("2026-10-10", 1, "2026-10-11", 1), ("2026-10-10", 1, "2026-10-13", 7),
    ("2026-10-04", 1, "2026-10-06", 15), ("2026-10-14", 4, "2026-10-15", 4),
    ("2026-10-10", 19, "2026-10-11", 27), ("2026-10-10", 19, "2026-10-13", 15),
    ("2026-10-06", 23, "2026-10-07", 5), ("2026-10-07", 1, "2026-10-08", 9),
    ("2026-10-17", 3, "2026-10-18", 7), ("2026-10-18", 7, "2026-10-21", 10),
]


def read_clusters(date):
    """editions/<date>/candidates.md -> [{'ids': [...], 'titles': [...]}, ...]"""
    path = os.path.join(ROOT, "editions", date, "candidates.md")
    if not os.path.exists(path):
        return []
    clusters = []
    for line in open(path).read().splitlines():
        lead = re.match(r"\[(\d+)\] .*?\((?:high|medium|low)[^)]*\) (.*?)(?: -- .*)?$", line)
        more = re.match(r"\s+\+ \[(\d+)\] [^:]*: (.*)$", line)
        if lead:
            clusters.append({"ids": [int(lead.group(1))], "titles": [lead.group(2)]})
        elif more and clusters:
            clusters[-1]["ids"].append(int(more.group(1)))
            clusters[-1]["titles"].append(more.group(2))
    return clusters


def chain(date, rank, editions):
    """(date, headline) of every story linked to this one through KNOWN_REPEATS."""
    links = {}
    for a_date, a_rank, b_date, b_rank in KNOWN_REPEATS:
        links.setdefault((a_date, a_rank), set()).add((b_date, b_rank))
        links.setdefault((b_date, b_rank), set()).add((a_date, a_rank))
    seen, todo = set(), [(date, rank)]
    while todo:
        node = todo.pop()
        if node not in seen:
            seen.add(node)
            todo += links.get(node, ())
    return {(d, editions[d]["stories"][r - 1]["headline"]) for d, r in seen}


def main():
    editions = {}
    for path in sorted(glob.glob(os.path.join(ROOT, "editions", "20*", "edition.md"))):
        date = os.path.basename(os.path.dirname(path))
        edition = edition_md.parse(open(path).read())
        clusters = read_clusters(date)
        by_id = {i: c for c in clusters for i in c["ids"]}
        stories = []
        for s in edition["stories"]:
            cluster = by_id.get((s.get("ids") or [None])[0])
            stories.append({"date": date, "headline": s["headline"], "event": s.get("event", ""),
                            "titles": cluster["titles"] if cluster else []})
        editions[date] = {"clusters": clusters, "stories": stories, "by_id": by_id, "raw": edition}

    found = missed = tags = days = picked_tags = 0
    known = {}
    for a_date, a_rank, b_date, b_rank in KNOWN_REPEATS:
        known.setdefault((b_date, b_rank), []).append((a_date, a_rank))
    misses = []
    for date, ed in sorted(editions.items()):
        if not ed["clusters"]:
            continue
        today = Date.fromisoformat(date)
        prior = [s for d, e in editions.items() if today - timedelta(days=7) <= Date.fromisoformat(d) < today
                 for s in e["stories"]]
        hits = dedupe.find_covered([c["titles"] for c in ed["clusters"]], prior)
        days += 1
        tags += sum(1 for h in hits if h)
        tagged = {id(c): h for c, h in zip(ed["clusters"], hits)}
        for rank, story in enumerate(ed["raw"]["stories"], start=1):
            cluster = ed["by_id"].get((story.get("ids") or [None])[0])
            hit = tagged.get(id(cluster)) if cluster else None
            picked_tags += bool(hit)
            for a_date, a_rank in known.get((date, rank), []):
                # tagged against any earlier story of the same chain counts: a story covered
                # three days running is rightly tagged against the most recent one
                ok = bool(hit) and (hit[0]["date"], hit[0]["headline"]) in chain(a_date, a_rank, editions)
                found += ok
                missed += not ok
                if not ok:
                    misses.append((a_date, a_rank, date, rank, hit[0]["headline"] if hit else None))
    total = found + missed
    print(f"known repeats tagged against the right earlier story: {found}/{total} ({100 * found // max(total, 1)}%)")
    print(f"tags per day: {tags / max(days, 1):.1f} on average over {days} days "
          f"(of which on stories that were featured: {picked_tags})")
    for m in misses:
        print(f"  missed: {m[0]} #{m[1]} -> {m[2]} #{m[3]}" + (f" (tagged against {m[4]!r} instead)" if m[4] else ""))


if __name__ == "__main__":
    main()
