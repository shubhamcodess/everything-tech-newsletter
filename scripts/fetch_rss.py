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
            image=_image(entry),
        ))
    return articles


def _image(entry) -> str | None:
    for key in ("media_content", "media_thumbnail"):
        for media in entry.get(key) or []:
            if media.get("url") and "image" in (media.get("type") or "image"):
                return media["url"]
    for link in entry.get("links") or []:
        if link.get("rel") == "enclosure" and (link.get("type") or "").startswith("image"):
            return link.get("href")
    return None
