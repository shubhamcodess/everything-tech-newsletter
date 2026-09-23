"""TLDR.tech daily digests (tech/ai/dev/... editions). No official API, but
each day's issue is server-rendered static HTML at a predictable dated URL,
so this scrapes it directly. TLDR is itself a curated digest -- a good
complementary source since its editors already did a first pass of triage."""
import re
from datetime import date, timedelta

from common import normalize

import requests

ARTICLE_RE = re.compile(
    r'<article[^>]*><a class="font-bold" href="([^"]+)"[^>]*><h3>(.*?)</h3></a>'
    r'<div class="newsletter-html">(.*?)</div></article>',
    re.S,
)
TAG_RE = re.compile(r"<[^>]+>")


def _clean(text: str) -> str:
    text = TAG_RE.sub(" ", text)
    text = text.replace("&amp;", "&").replace("&#39;", "'")
    return re.sub(r"\s+", " ", text).strip()


def _strip_tracking(url: str) -> str:
    return re.split(r"[?&]utm_source=", url)[0]


def fetch(source: dict, max_items: int) -> list[dict]:
    edition = source.get("edition", "tech")
    headers = {"User-Agent": "tech-newsletter-bot/1.0"}

    # An unpublished day's URL (e.g. today, before the issue goes out, or a
    # weekend with no issue) 307-redirects to an unrelated feed page that
    # still contains <article> tags in a different shape, so acceptance has
    # to be "the real story pattern matched", not just "got a 200".
    matches = []
    issue_day = None
    for days_back in range(4):
        issue_day = date.today() - timedelta(days=days_back)
        url = f"https://tldr.tech/{edition}/{issue_day.isoformat()}"
        resp = requests.get(url, headers=headers, timeout=15)
        matches = ARTICLE_RE.findall(resp.text)
        if matches:
            break
    if not matches:
        raise RuntimeError(f"no issue found for edition '{edition}' in the last 4 days")

    articles = []
    for link, title_html, summary_html in matches:
        title = _clean(title_html)
        if "(Sponsor)" in title:
            continue
        title = re.sub(r"\s*\([^()]*read\)\s*$", "", title, flags=re.I)
        articles.append(normalize(
            title=title,
            url=_strip_tracking(link),
            source=source["name"],
            source_id=source["id"],
            summary=_clean(summary_html),
            published_at=issue_day.isoformat(),
        ))
        if len(articles) >= max_items:
            break
    return articles
