"""Dev.to via its public API. No auth needed for reads."""
from common import normalize

import requests

API = "https://dev.to/api/articles"


def fetch(source: dict, max_items: int) -> list[dict]:
    params = {"per_page": max_items, "top": source.get("top_days", 1)}
    if source.get("tag"):
        params["tag"] = source["tag"]
    resp = requests.get(API, params=params, timeout=15)
    resp.raise_for_status()

    articles = []
    for item in resp.json():
        articles.append(normalize(
            title=item.get("title", ""),
            url=item.get("url", ""),
            source=source["name"],
            source_id=source["id"],
            author=(item.get("user") or {}).get("name"),
            published_at=item.get("published_at"),
            summary=item.get("description", ""),
            tags=item.get("tag_list", []),
            points=item.get("positive_reactions_count"),
            comments=item.get("comments_count"),
        ))
    return articles
