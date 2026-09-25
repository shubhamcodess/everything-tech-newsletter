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
    default_max = settings.get("max_items_per_source", 10)

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
        article.pop("id", None)
        for key in [k for k, v in article.items() if v in (None, "", [])]:
            article.pop(key)
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
        json.dump(out, f, separators=(",", ":"))

    print(f"\n{len(deduped)} unique articles from {len(sources) - len(errors)}/{len(sources)} sources")
    if errors:
        print(f"{len(errors)} source(s) failed -- see 'errors' in {out_path}")


if __name__ == "__main__":
    main()
