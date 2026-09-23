"""Generic RSS/Atom fetcher, used for every source of type "rss" in sources.json."""
from common import normalize

import feedparser


def fetch(source: dict, max_items: int) -> list[dict]:
    feed_url = source["feed_url"]
    parsed = feedparser.parse(feed_url, agent="tech-newsletter-bot/1.0")
    if parsed.bozo and not parsed.entries:
        raise RuntimeError(f"could not parse feed: {parsed.bozo_exception}")

    articles = []
    for entry in parsed.entries[:max_items]:
        published = entry.get("published") or entry.get("updated")
        tags = [t.get("term") for t in entry.get("tags", [])] if entry.get("tags") else []
        articles.append(normalize(
            title=entry.get("title", ""),
            url=entry.get("link", ""),
            source=source["name"],
            source_id=source["id"],
            author=entry.get("author"),
            published_at=published,
            summary=entry.get("summary", ""),
            tags=tags,
        ))
    return articles
