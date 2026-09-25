"""Publishes today's edition from the routine's draft.

Usage:  python scripts/publish_edition.py            # validate data/draft.md, publish, build the site
        python scripts/publish_edition.py --check    # validate only, change nothing

The draft carries only what needs judgment -- which candidates, rank,
headline, dek, body, takeaways, topic, signal, and the brief. This script
fills in everything mechanical (source links, authors, images, read times,
discussion links, edition number) and writes the day's durable record:

    editions/<date>/edition.md     the edition, self-contained
    editions/<date>/sources.md     full text + metadata of the articles used
    editions/<date>/candidates.md  everything that was considered that day

then updates data/seen.json and runs build_site.py. Exits non-zero with a
list of fixable problems if the draft is invalid.
"""
import json
import math
import os
import shutil
import sys
from datetime import datetime, timedelta, timezone
from urllib.parse import urlsplit, urlunsplit
from zoneinfo import ZoneInfo

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_site  # noqa: E402
import edition_md  # noqa: E402
from edition_schema import validate_draft  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AGGREGATORS = ("hn", "reddit", "lobsters", "tldr", "github_trending")


def load(path, default=None):
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        if default is None:
            sys.exit(f"missing {os.path.relpath(path, ROOT)} -- see CLAUDE.md for which step produces it")
        return default


def domain(url):
    return urlsplit(url).netloc.lower().removeprefix("www.")


def clean_url(url):
    parts = urlsplit(url)
    query = "&".join(q for q in parts.query.split("&") if q and not q.lower().startswith(("utm_", "ref=")))
    return urlunsplit((parts.scheme, parts.netloc, parts.path, query, ""))


def source_entry(cand):
    is_aggregator = str(cand.get("source_id", "")).startswith(AGGREGATORS)
    entry = {"name": domain(cand["url"]) if is_aggregator else cand["source"], "url": clean_url(cand["url"])}
    if is_aggregator and "news.ycombinator.com" not in cand["url"]:
        entry["via"] = cand["source"]
    return entry


def resolve_story(draft_story, candidates, articles):
    ids = draft_story["ids"]
    primary = candidates[str(ids[0])]
    members = [candidates[str(i)] for i in ids]
    members += [candidates[str(i)] for i in primary["cluster"] if i not in ids]

    sources, names = [], set()
    for cand in members:
        entry = source_entry(cand)
        if entry["name"] not in names:
            names.add(entry["name"])
            sources.append(entry)

    art = articles.get(str(ids[0]), {})
    discuss = next((c for c in members if c.get("discuss_url")), None)
    image = art.get("image") or next((c.get("image") for c in members if c.get("image")), None)
    author = art.get("author") or (None if str(primary.get("source_id", "")).startswith(AGGREGATORS)
                                   else primary.get("author"))
    story = {
        **{k: draft_story[k] for k in ("headline", "dek", "body", "takeaways", "topic", "signal")},
        "ids": ids,
        "url": clean_url(primary["url"]),
        "source_title": primary["title"],
        "sources": sources,
        "full_text": bool(art.get("ok")),
    }
    if author:
        names = [a.strip() for a in author.replace(" and ", ";").replace(",", ";").split(";") if a.strip()]
        story["author"] = names[0] if len(names) == 1 else f"{names[0]} and {names[1]}" if len(names) == 2 \
            else f"{names[0]} et al."
    if image and str(image).startswith("https://"):
        story["image"] = image
    if art.get("words"):
        story["read_minutes"] = max(1, math.ceil(art["words"] / 230))
    if discuss:
        story.update(discuss_url=discuss["discuss_url"], discuss_via=discuss["source"])
        if discuss.get("points"):
            story["points"] = discuss["points"]
        if discuss.get("comments"):
            story["comments"] = discuss["comments"]
    return story, [c["url"] for c in members]


def main():
    check_only = "--check" in sys.argv
    settings = load(os.path.join(ROOT, "config", "settings.json"))
    topics = [t["label"] for t in load(os.path.join(ROOT, "config", "interests.json"))["topics"]]
    cand_file = load(os.path.join(ROOT, "data", "candidates.json"))
    candidates = cand_file["candidates"]
    articles = load(os.path.join(ROOT, "data", "articles.json"), {})

    draft_path = os.path.join(ROOT, "data", "draft.md")
    if not os.path.exists(draft_path):
        sys.exit("missing data/draft.md -- write the edition there first (see CLAUDE.md)")
    try:
        draft = edition_md.parse(open(draft_path).read())
    except edition_md.ParseError as exc:
        sys.exit(f"data/draft.md doesn't follow the edition format: {exc}")

    source_texts = {}
    articles_md = os.path.join(ROOT, "data", "articles.md")
    if os.path.exists(articles_md):
        for chunk in open(articles_md).read().split("\n## [")[1:]:
            cid, _, rest = chunk.partition("]")
            source_texts[cid] = rest
    errors = validate_draft(draft, candidates, topics, settings, source_texts)
    if errors:
        print(f"data/draft.md has {len(errors)} problem(s) -- fix them and re-run:")
        print("\n".join(f"  - {e}" for e in errors))
        sys.exit(1)
    if check_only:
        print(f"draft OK: {len(draft['stories'])} stories")
        return

    tz = ZoneInfo(settings.get("timezone", "UTC"))
    now = datetime.now(timezone.utc)
    date = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--date=")),
                now.astimezone(tz).date().isoformat())
    manifest = build_site.read_manifest()
    existing = next((e for e in manifest["editions"] if e["date"] == date), None)
    number = existing["edition"] if existing else manifest["count"] + 1

    stories, featured = [], []
    for draft_story in draft["stories"]:
        story, urls = resolve_story(draft_story, candidates, articles)
        stories.append(story)
        featured.append((story, urls))

    edition = {
        "date": date,
        "edition": number,
        "generated_at": now.isoformat(timespec="seconds"),
        "stats": {
            "sources_ok": cand_file["ok_sources"],
            "sources_total": cand_file["total_sources"],
            "fetched": cand_file["fetched"],
            "candidates": len(candidates),
            "full_text": sum(1 for s in stories if s["full_text"]),
        },
        "brief": draft["brief"],
        "stories": stories,
    }
    day_dir = os.path.join(ROOT, "editions", date)
    os.makedirs(day_dir, exist_ok=True)
    with open(os.path.join(day_dir, "edition.md"), "w") as f:
        f.write(edition_md.write(edition))
    for name in ("articles.md", "candidates.md"):
        src = os.path.join(ROOT, "data", name)
        if os.path.exists(src):
            shutil.copy(src, os.path.join(day_dir, "sources.md" if name == "articles.md" else name))

    seen_path = os.path.join(ROOT, "data", "seen.json")
    seen = load(seen_path, {"featured": []})
    cutoff = (datetime.fromisoformat(date) - timedelta(days=settings.get("dedup_lookback_days", 7))).date().isoformat()
    kept = [s for s in seen["featured"] if cutoff <= s.get("date", "") != date]
    for story, urls in featured:
        kept += [{"title": story["headline"], "url": u, "source": story["sources"][0]["name"], "date": date} for u in urls]
    with open(seen_path, "w") as f:
        json.dump({"featured": kept}, f, ensure_ascii=False)
        f.write("\n")

    print(f"wrote editions/{date}/ (edition No. {number}, {len(stories)} stories, "
          f"{edition['stats']['full_text']} from full article text)")
    build_site.main()


if __name__ == "__main__":
    main()
