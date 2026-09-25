"""Validation for the routine's draft (data/draft.md) and for published
editions (editions/<date>/edition.md). Shared by publish_edition.py and
validate_editions.py (CI).

Every check here corresponds to a failure a real run has produced: template
placeholders shipped to production, raw abstracts pasted in and cut off
mid-word, escaped HTML dumped into a summary, a bare URL standing in for a
summary, and generic filler closing lines.
"""
import re

SIGNALS = ("must-read", "recommended", "notable")
PLACEHOLDERS = re.compile(r"ARTICLE_URL|ARTICLE_TITLE|SOURCE_NAME|OTHER_SOURCES|lorem ipsum|\bTODO\b|<headline>|<paragraph>", re.I)
MARKUP = re.compile(r"<\s*/?\s*[a-z][a-z0-9]*[^>]*>|&(lt|gt|amp|quot|#\d+|#x[0-9a-f]+);", re.I)
RAW_URL = re.compile(r"https?://|www\.[a-z0-9-]+\.[a-z]", re.I)
FILLER = re.compile(
    r"important update|significant development|in the tech industry|in the world of tech|"
    r"continues to evolve|growing trend|only time will tell|game[- ]changer|stay tuned",
    re.I,
)
ENDS_CLEANLY = re.compile(r"[.!?…)\]\"'”’:]\s*$")


def _words(text):
    return re.findall(r"[a-z0-9']+", text.lower())


def _ngrams(words, n=12):
    return {" ".join(words[i:i + n]) for i in range(len(words) - n + 1)}


def check_prose(where, text, errors, min_len=1, source_ngrams=None):
    if not isinstance(text, str) or len(text.strip()) < min_len:
        errors.append(f"{where}: must be a string of at least {min_len} characters")
        return
    if PLACEHOLDERS.search(text):
        errors.append(f"{where}: contains template placeholder text -- write real content")
    if MARKUP.search(text):
        errors.append(f"{where}: contains HTML tags or entities -- write plain text")
    if RAW_URL.search(text):
        errors.append(f"{where}: contains a raw URL -- describe it in words, links come from sources")
    if FILLER.search(text):
        errors.append(f"{where}: generic filler phrase {FILLER.search(text).group(0)!r} -- say something specific")
    if source_ngrams and _ngrams(_words(text)) & source_ngrams:
        errors.append(f"{where}: copies 12+ words verbatim from the source article -- paraphrase in your own words")


def validate_draft(draft, candidates, topic_labels, settings, source_texts=None):
    """Returns a list of human-readable errors; empty means valid."""
    errors = []
    source_texts = source_texts or {}
    if not isinstance(draft, dict):
        return ["draft must be a JSON object with 'brief' and 'stories'"]

    brief = draft.get("brief")
    if not isinstance(brief, list) or not 3 <= len(brief) <= 6:
        errors.append("brief: must be a list of 3-6 short strings")
    else:
        for i, line in enumerate(brief):
            check_prose(f"brief[{i}]", line, errors, min_len=20)

    stories = draft.get("stories")
    limit = settings.get("stories_per_edition", 30)
    if not isinstance(stories, list) or not stories:
        return errors + ["stories: must be a non-empty list"]
    if len(stories) > limit + 5:
        errors.append(f"stories: {len(stories)} stories, more than stories_per_edition ({limit}) allows")

    used = {}
    must_reads = 0
    for n, story in enumerate(stories):
        where = f"stories[{n}]"
        if not isinstance(story, dict):
            errors.append(f"{where}: must be an object")
            continue
        ids = story.get("ids")
        if not isinstance(ids, list) or not ids or not all(isinstance(i, int) for i in ids):
            errors.append(f"{where}.ids: must be a non-empty list of candidate ids (integers)")
            ids = []
        for cid in ids:
            if str(cid) not in candidates:
                errors.append(f"{where}.ids: {cid} is not a candidate id in data/candidates.md")
            elif cid in used:
                errors.append(f"{where}.ids: {cid} already used by stories[{used[cid]}] -- one story per cluster")
            else:
                used[cid] = n

        source_ngrams = set()
        for cid in ids:
            for text in (source_texts.get(str(cid)), (candidates.get(str(cid)) or {}).get("summary")):
                if text:
                    source_ngrams |= _ngrams(_words(text))

        headline = story.get("headline")
        check_prose(f"{where}.headline", headline, errors, min_len=15)
        if isinstance(headline, str) and len(headline) > 130:
            errors.append(f"{where}.headline: {len(headline)} chars -- keep it under 130")
        check_prose(f"{where}.dek", story.get("dek"), errors, min_len=40, source_ngrams=source_ngrams)

        body = story.get("body")
        if not isinstance(body, list) or not 1 <= len(body) <= 6:
            errors.append(f"{where}.body: must be a list of 1-6 paragraphs")
        else:
            for p, para in enumerate(body):
                check_prose(f"{where}.body[{p}]", para, errors, min_len=80, source_ngrams=source_ngrams)
                if isinstance(para, str) and not ENDS_CLEANLY.search(para):
                    errors.append(f"{where}.body[{p}]: doesn't end with punctuation -- looks cut off mid-sentence")
            if isinstance(headline, str) and body and isinstance(body[0], str) \
                    and body[0].lower().startswith(headline.lower()[:40]):
                errors.append(f"{where}.body[0]: opens by restating the headline")

        takeaways = story.get("takeaways", [])
        if not isinstance(takeaways, list) or len(takeaways) > 5:
            errors.append(f"{where}.takeaways: must be a list of 0-5 strings")
        else:
            for t, item in enumerate(takeaways):
                check_prose(f"{where}.takeaways[{t}]", item, errors, min_len=15, source_ngrams=source_ngrams)

        if story.get("topic") not in topic_labels:
            errors.append(f"{where}.topic: {story.get('topic')!r} -- must be one of {topic_labels}")
        signal = story.get("signal")
        if signal not in SIGNALS:
            errors.append(f"{where}.signal: {signal!r} -- must be one of {list(SIGNALS)}")
        must_reads += signal == "must-read"

    if stories and isinstance(stories[0], dict) and stories[0].get("signal") != "must-read":
        errors.append("stories[0]: the lead story must be signal 'must-read'")
    cap = settings.get("must_read_max", 6)
    if must_reads > cap:
        errors.append(f"{must_reads} must-read stories -- at most {cap}; must-read should mean it")
    return errors


def validate_edition(edition, where="edition"):
    """Structural check of a published edition file (used by CI)."""
    errors = []
    for key in ("date", "edition", "brief", "stories"):
        if key not in edition:
            errors.append(f"{where}: missing '{key}'")
    for n, story in enumerate(edition.get("stories", [])):
        at = f"{where}.stories[{n}]"
        for key in ("headline", "dek", "body", "topic", "signal", "url", "sources"):
            if not story.get(key):
                errors.append(f"{at}: missing '{key}'")
        if not str(story.get("url", "")).startswith(("http://", "https://")):
            errors.append(f"{at}.url: not an http(s) URL")
        for field in ("headline", "dek", *[f"body[{i}]" for i in range(len(story.get("body", [])))]):
            value = story.get(field) if "[" not in field else story["body"][int(field[5:-1])]
            if isinstance(value, str) and (PLACEHOLDERS.search(value) or MARKUP.search(value)):
                errors.append(f"{at}.{field}: placeholder or markup in published text")
    return errors
