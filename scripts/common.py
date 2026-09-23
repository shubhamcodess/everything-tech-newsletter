"""Shared helpers for source fetchers."""
import hashlib
from datetime import datetime, timezone


def make_id(url: str) -> str:
    return hashlib.sha256(url.strip().lower().encode()).hexdigest()[:16]


def normalize(*, title, url, source, source_id, author=None, published_at=None,
              summary=None, tags=None, points=None, comments=None):
    # summary is capped at 280 chars (not 600) on purpose: the LLM step
    # downstream has a single-Read token budget across ~500 articles, and
    # this field is by far the largest contributor per article. 280 chars
    # is still enough to ground a paraphrase without inviting a copy-paste
    # summary (see CLAUDE.md's "Writing digest summaries").
    return {
        "id": make_id(url),
        "title": (title or "").strip(),
        "url": url,
        "source": source,
        "source_id": source_id,
        "author": author,
        "published_at": published_at,
        "summary": (summary or "").strip()[:200],
        "tags": tags or [],
        "engagement": {"points": points, "comments": comments},
        "fetched_at": datetime.now(timezone.utc).isoformat(),
    }
