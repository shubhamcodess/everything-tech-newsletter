"""Orchestrates every source in config/sources.json, normalizes results, and writes
data/raw_latest.json. Resilient to individual source failures: logs and continues
so one broken feed never takes down the whole run."""
import json
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import fetch_arxiv
import fetch_devto
import fetch_github_trending
import fetch_hn
import fetch_reddit
import fetch_rss
import fetch_tldr

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FETCHERS = {
    "rss": fetch_rss.fetch,
    "hn": fetch_hn.fetch,
    "reddit": fetch_reddit.fetch,
    "arxiv": fetch_arxiv.fetch,
    "devto": fetch_devto.fetch,
    "github_trending": fetch_github_trending.fetch,
    "tldr": fetch_tldr.fetch,
}


def load(path):
    with open(path) as f:
        return json.load(f)


def main():
    sources = load(os.path.join(ROOT, "config", "sources.json"))["sources"]
    settings = load(os.path.join(ROOT, "config", "settings.json"))
    default_max = settings.get("max_items_per_source", 15)

    all_articles = []
    errors = []

    for source in sources:
        if not source.get("enabled", True):
            continue
        fetcher = FETCHERS.get(source["type"])
        if fetcher is None:
            errors.append({"source": source["id"], "error": f"unknown type {source['type']}"})
            continue
        try:
            items = fetcher(source, source.get("max_items", default_max))
            all_articles.extend(items)
            print(f"[ok]   {source['id']:<22} {len(items):>3} items")
        except Exception as exc:  # noqa: BLE001 -- one bad source must not kill the run
            errors.append({"source": source["id"], "error": str(exc)})
            print(f"[fail] {source['id']:<22} {exc}")

    seen_ids = set()
    deduped = []
    for article in all_articles:
        if article["id"] in seen_ids:
            continue
        seen_ids.add(article["id"])
        # id/source_id/fetched_at are only needed for the dedup pass above
        # and to route the fetch to the right adapter -- the digest-writing
        # step downstream never uses them, and dropping them here is one of
        # a few changes that keep this file small enough to fit in a single
        # Read call once article counts get large. See CLAUDE.md step 3.
        article.pop("id", None)
        article.pop("source_id", None)
        article.pop("fetched_at", None)
        if not article.get("tags"):
            article.pop("tags", None)
        if not article.get("author"):
            article.pop("author", None)
        engagement = article.get("engagement") or {}
        if engagement.get("points") is None and engagement.get("comments") is None:
            article.pop("engagement", None)
        deduped.append(article)

    out = {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "total_sources": len(sources),
        "ok_sources": len(sources) - len(errors),
        "errors": errors,
        "articles": deduped,
    }

    out_path = os.path.join(ROOT, "data", "raw_latest.json")
    with open(out_path, "w") as f:
        # Compact, not pretty-printed: this file is for the routine to
        # read, not for humans to browse -- indent=2 alone can roughly
        # double the size of a file this repetitive. Pretty-print locally
        # with `python -m json.tool` if you need to eyeball it.
        json.dump(out, f, separators=(",", ":"))

    print(f"\n{len(deduped)} unique articles from {len(sources) - len(errors)}/{len(sources)} sources")
    if errors:
        print(f"{len(errors)} source(s) failed -- see 'errors' in {out_path}")


if __name__ == "__main__":
    main()
