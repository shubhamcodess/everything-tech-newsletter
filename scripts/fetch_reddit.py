"""Reddit via public .json listing endpoints. No auth needed, but Reddit requires
a descriptive User-Agent or it will 429 the request."""
from common import normalize

import requests

HEADERS = {"User-Agent": "tech-newsletter-bot/1.0 (personal daily digest)"}


def fetch(source: dict, max_items: int) -> list[dict]:
    subreddit = source["subreddit"]
    listing = source.get("listing", "top")
    timeframe = source.get("timeframe", "day")
    url = f"https://www.reddit.com/r/{subreddit}/{listing}.json"
    resp = requests.get(
        url, headers=HEADERS, params={"limit": max_items, "t": timeframe}, timeout=15
    )
    resp.raise_for_status()
    children = resp.json().get("data", {}).get("children", [])

    articles = []
    for child in children:
        d = child.get("data", {})
        if d.get("stickied"):
            continue
        link = d.get("url_overridden_by_dest") or f"https://reddit.com{d.get('permalink', '')}"
        articles.append(normalize(
            title=d.get("title", ""),
            url=link,
            source=source["name"],
            source_id=source["id"],
            author=d.get("author"),
            published_at=d.get("created_utc"),
            summary=d.get("selftext", ""),
            points=d.get("score"),
            comments=d.get("num_comments"),
            discuss_url=f"https://reddit.com{d.get('permalink', '')}",
        ))
    return articles
