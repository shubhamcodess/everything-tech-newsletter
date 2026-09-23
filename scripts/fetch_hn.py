"""Hacker News via the Algolia public API. No auth needed."""
from common import normalize

import requests

API = "https://hn.algolia.com/api/v1/search"


def fetch(source: dict, max_items: int) -> list[dict]:
    params = {
        "tags": source.get("tags", "front_page"),
        "hitsPerPage": max_items,
    }
    resp = requests.get(API, params=params, timeout=15)
    resp.raise_for_status()
    hits = resp.json().get("hits", [])

    articles = []
    for hit in hits:
        url = hit.get("url") or f"https://news.ycombinator.com/item?id={hit['objectID']}"
        articles.append(normalize(
            title=hit.get("title") or hit.get("story_title") or "",
            url=url,
            source=source["name"],
            source_id=source["id"],
            author=hit.get("author"),
            published_at=hit.get("created_at"),
            points=hit.get("points"),
            comments=hit.get("num_comments"),
        ))
    return articles
