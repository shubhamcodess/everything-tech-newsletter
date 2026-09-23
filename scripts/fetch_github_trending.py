"""GitHub Trending has no official API, so this parses the public HTML page.
GitHub occasionally changes this page's markup -- if this starts returning 0
items, that's the first place to look (see CLAUDE.md's Maintenance section)."""
import re

from common import normalize

import requests

BASE = "https://github.com/trending"


def fetch(source: dict, max_items: int) -> list[dict]:
    language = source.get("language", "")
    since = source.get("since", "daily")
    url = f"{BASE}/{language}".rstrip("/")
    resp = requests.get(
        url,
        params={"since": since},
        timeout=15,
        headers={"User-Agent": "tech-newsletter-bot/1.0"},
    )
    resp.raise_for_status()
    html = resp.text

    repo_paths = re.findall(r'href="/([\w.-]+/[\w.-]+)"\s+data-view-component="true"\s+class="Link"', html)
    ordered_unique = []
    for path in repo_paths:
        if path not in ordered_unique:
            ordered_unique.append(path)
        if len(ordered_unique) >= max_items:
            break

    articles = []
    for path in ordered_unique:
        articles.append(normalize(
            title=path,
            url=f"https://github.com/{path}",
            source=source["name"],
            source_id=source["id"],
            summary=f"Trending on GitHub ({since})",
            tags=[language] if language else [],
        ))
    return articles
