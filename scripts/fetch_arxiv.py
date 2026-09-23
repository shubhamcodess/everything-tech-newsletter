"""arXiv via its public Atom API. No auth needed."""
from common import normalize

import feedparser

API = "http://export.arxiv.org/api/query"


def fetch(source: dict, max_items: int) -> list[dict]:
    category = source["category"]
    query_url = (
        f"{API}?search_query=cat:{category}"
        f"&sortBy=submittedDate&sortOrder=descending&max_results={max_items}"
    )
    parsed = feedparser.parse(query_url)

    articles = []
    for entry in parsed.entries:
        authors = ", ".join(a.get("name", "") for a in entry.get("authors", [])) or None
        articles.append(normalize(
            title=entry.get("title", "").replace("\n", " ").strip(),
            url=entry.get("link", ""),
            source=source["name"],
            source_id=source["id"],
            author=authors,
            published_at=entry.get("published"),
            summary=entry.get("summary", ""),
            tags=[category],
        ))
    return articles
