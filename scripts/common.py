"""Shared helpers for source fetchers."""
import hashlib


def make_id(url: str) -> str:
    return hashlib.sha256(url.strip().lower().encode()).hexdigest()[:16]


def normalize(*, title, url, source, source_id, author=None, published_at=None,
              summary=None, tags=None, points=None, comments=None,
              discuss_url=None, image=None):
    # data/raw_latest.json is never read by the model directly any more --
    # scripts/build_candidates.py compacts it into a token-budgeted list --
    # so the snippet here can be long enough to be useful.
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
        "points": points,
        "comments": comments,
        "discuss_url": discuss_url,
        "image": image,
    }
