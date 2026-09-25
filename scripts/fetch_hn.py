"""Hacker News via the Algolia public API. No auth needed."""
import re

from common import normalize

import requests

API = "https://hn.algolia.com/api/v1/search"
TAG_RE = re.compile(r"<[^>]+>")


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
        # Ask HN / Show HN posts often carry their own text body -- the API
        # already returns it, we just weren't capturing it. Link posts to
        # an external URL have no story_text; nothing to do about those
        # here, the title has to carry the specifics.
        story_text = TAG_RE.sub(" ", hit.get("story_text") or "").strip()
        articles.append(normalize(
            title=hit.get("title") or hit.get("story_title") or "",
            url=url,
            source=source["name"],
            source_id=source["id"],
            author=hit.get("author"),
            published_at=hit.get("created_at"),
            summary=story_text,
            points=hit.get("points"),
            comments=hit.get("num_comments"),
            discuss_url=f"https://news.ycombinator.com/item?id={hit['objectID']}",
        ))
    return articles
