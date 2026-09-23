"""Shared helpers for source fetchers."""
import hashlib
from datetime import datetime, timezone


def make_id(url: str) -> str:
    return hashlib.sha256(url.strip().lower().encode()).hexdigest()[:16]


def normalize(*, title, url, source, source_id, author=None, published_at=None,
              summary=None, tags=None, points=None, comments=None):
    return {
        "id": make_id(url),
        "title": (title or "").strip(),
        "url": url,
        "source": source,
        "source_id": source_id,
        "author": author,
        "published_at": published_at,
        "summary": (summary or "").strip()[:600],
        "tags": tags or [],
        "engagement": {"points": points, "comments": comments},
        "fetched_at": datetime.now(timezone.utc).isoformat(),
    }
