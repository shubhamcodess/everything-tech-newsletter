"""Compacts data/raw_latest.json into a numbered, pre-clustered candidate list
the routine can read in a single pass.

Writes:
  data/candidates.md   -- what the model reads: one line per story cluster
  data/candidates.json -- the same candidates with full metadata, keyed by id,
                          used by fetch_articles.py and publish_edition.py

Everything here is mechanical (dates, dedup against seen.json, obvious junk,
title-similarity clustering, token budgeting). Deciding what's actually worth
running is left to the model.
"""
import html
import json
import math
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from zoneinfo import ZoneInfo
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRUST = {"high": 3, "medium": 2, "low": 1}

JUNK = re.compile(
    r"promo code|coupon|discount code|hints and answers|\bwordle\b|quordle|"
    r"connections hints|strands hints|\(sponsor\)|\(\$\d+k|\bbest .* deals?\b|"
    r"\bsave \$\d+|\$?\d+%? off\b|deal of the day|prime day|\bon sale\b|very good deal|best early .* sales",
    re.I,
)
STOP = set(
    "a an and are as at be by for from has have how in into is it its of on or "
    "that the their this to was what when why will with you your new now after "
    "about over says just more than can could may via using use".split()
)


def load(path, default=None):
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        return default


def canon_url(url: str) -> str:
    parts = urlsplit(url.strip())
    query = urlencode([(k, v) for k, v in parse_qsl(parts.query) if not k.lower().startswith(("utm_", "ref"))])
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower().removeprefix("www."),
                       parts.path.rstrip("/"), query, ""))


def parse_date(value):
    if value in (None, ""):
        return None
    if isinstance(value, (int, float)):
        return datetime.fromtimestamp(value, timezone.utc)
    text = str(value).strip()
    try:
        dt = datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        try:
            dt = parsedate_to_datetime(text)
        except (TypeError, ValueError):
            return None
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


def title_tokens(title: str) -> set:
    words = re.findall(r"[a-z0-9][a-z0-9.+#-]*", title.lower())
    return {w for w in words if len(w) > 2 and w not in STOP}


def clean_snippet(text: str) -> str:
    text = html.unescape(re.sub(r"<[^>]+>", " ", text or ""))
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"The post .{0,200}? appeared first on .*$", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return "" if text.lower() in ("comments", "read more", "continue reading") else text


def main():
    raw = load(os.path.join(ROOT, "data", "raw_latest.json"))
    if raw is None:
        sys.exit("data/raw_latest.json missing -- run scripts/fetch_all.py first")
    sources = {s["id"]: s for s in load(os.path.join(ROOT, "config", "sources.json"))["sources"]}
    settings = load(os.path.join(ROOT, "config", "settings.json"), {})
    seen = load(os.path.join(ROOT, "data", "seen.json"), {"featured": []})
    budget = settings.get("candidate_token_budget", 18000)
    now = datetime.now(timezone.utc)
    today = now.astimezone(ZoneInfo(settings.get("timezone", "UTC"))).date()
    cutoff = now - timedelta(hours=settings.get("fetch_lookback_hours", 48))
    seen_urls = {canon_url(item["url"]) for item in seen.get("featured", []) if item.get("url")}

    dropped = {"old": 0, "seen": 0, "junk": 0, "dupe": 0}
    items, by_url = [], {}
    for article in raw["articles"]:
        url = article.get("url") or ""
        if not url or not article.get("title"):
            continue
        key = canon_url(url)
        published = parse_date(article.get("published_at"))
        if published and published < cutoff:
            dropped["old"] += 1
            continue
        if key in seen_urls:
            dropped["seen"] += 1
            continue
        if JUNK.search(article["title"]):
            dropped["junk"] += 1
            continue
        if key in by_url:
            dropped["dupe"] += 1
            continue
        source = sources.get(article.get("source_id"), {})
        article["title"] = html.unescape(article["title"]).strip()
        item = {
            **article,
            "trust": source.get("trust", "medium"),
            "age_h": round((now - published).total_seconds() / 3600) if published else None,
            "tokens": title_tokens(article["title"]),
        }
        by_url[key] = item
        items.append(item)

    # Title-similarity clustering: same story from different outlets.
    clusters = []
    for item in items:
        for cluster in clusters:
            lead = cluster[0]
            shared = len(item["tokens"] & lead["tokens"])
            union = len(item["tokens"] | lead["tokens"])
            if union and ((shared >= 3 and shared / union >= 0.25) or (shared >= 2 and shared / union >= 0.4)):
                cluster.append(item)
                break
        else:
            clusters.append([item])

    def priority(cluster):
        best_trust = max(TRUST.get(i["trust"], 2) for i in cluster)
        points = max((i.get("points") or 0) for i in cluster)
        age = min((i["age_h"] for i in cluster if i["age_h"] is not None), default=24)
        return best_trust * 10 + min(math.log2(points + 1), 10) + 3 * (len(cluster) - 1) - age / 12

    for cluster in clusters:
        cluster.sort(key=lambda i: (-TRUST.get(i["trust"], 2), -(i.get("points") or 0)))
    clusters.sort(key=priority, reverse=True)

    candidates, next_id = {}, 1
    for cluster in clusters:
        ids = list(range(next_id, next_id + len(cluster)))
        for cid, item in zip(ids, cluster):
            item.pop("tokens", None)
            item["id"], item["cluster"] = cid, ids
            candidates[cid] = item
        next_id += len(cluster)

    def render(snippet_len, keep):
        lines = [
            f"# Candidates -- {today} -- {len(raw['articles'])} fetched from "
            f"{raw['ok_sources']}/{raw['total_sources']} sources -> {len(candidates)} candidates "
            f"in {len(clusters)} clusters (dropped: {dropped['old']} old, {dropped['seen']} already "
            f"featured, {dropped['junk']} junk, {dropped['dupe']} duplicate URLs)",
            "# [id] Source (trust, points/comments, age) Title -- snippet",
            "# Indented '+ [id]' lines are other outlets covering the same story (same cluster).",
            "",
        ]
        for cluster in clusters[:keep]:
            for n, item in enumerate(cluster):
                meta = [item["trust"]]
                if item.get("points"):
                    meta.append(f"{item['points']}pts/{item.get('comments') or 0}c")
                if item["age_h"] is not None:
                    meta.append(f"{item['age_h']}h")
                if n == 0:
                    snippet = clean_snippet(item.get("summary"))[:snippet_len]
                    tail = f" -- {snippet}" if snippet else ""
                    lines.append(f"[{item['id']}] {item['source']} ({', '.join(meta)}) {item['title']}{tail}")
                else:
                    lines.append(f"    + [{item['id']}] {item['source']}: {item['title']}")
        return "\n".join(lines) + "\n"

    keep = len(clusters)
    for snippet_len in (180, 120, 70, 0):
        text = render(snippet_len, keep)
        if len(text) / 3.6 <= budget:
            break
    while len(text) / 3.6 > budget and keep > 20:
        keep -= 10
        text = render(0, keep)

    with open(os.path.join(ROOT, "data", "candidates.md"), "w") as f:
        f.write(text)
    with open(os.path.join(ROOT, "data", "candidates.json"), "w") as f:
        json.dump({"generated_at": now.isoformat(), "fetched": len(raw["articles"]),
                   "ok_sources": raw["ok_sources"], "total_sources": raw["total_sources"],
                   "candidates": candidates}, f, ensure_ascii=False)

    shown = sum(len(c) for c in clusters[:keep])
    print(f"{len(candidates)} candidates in {len(clusters)} clusters; "
          f"data/candidates.md lists {shown} (~{int(len(text) / 3.6)} tokens, budget {budget})")
    print(f"dropped: {dropped}")


if __name__ == "__main__":
    main()
