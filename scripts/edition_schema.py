"""Validation for the routine's draft (data/draft.md) and for published
editions (editions/<date>/edition.md). Shared by publish_edition.py and
validate_editions.py (CI).

Structure (which fields, types, lengths, allowed values) lives in edition_model.py.
What stays here are the rules that need context or judgment. Every one of them
corresponds to a failure a real run has produced: template placeholders shipped
to production, raw abstracts pasted in and cut off mid-word, escaped HTML dumped
into a summary, a bare URL standing in for a summary, and generic filler closing
lines.
"""
import os
import re
import sys

from pydantic import ValidationError

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dedupe import event_problem  # noqa: E402
from edition_model import (  # noqa: E402
    SIGNALS, DraftEdition, PublishedEdition, SchemaVersionError, draft_errors, edition_errors, migrate)

# keys the site build adds to an edition after parsing; not part of the edition file
BUILD_KEYS = ("topics", "stats")
STORY_FIELD_ORDER = ("ids", "headline", "dek", "body", "takeaways", "event", "topic", "signal")
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


def check_prose(where, text, errors, source_ngrams=None):
    """Content rules for one piece of text. Length and type are the model's job."""
    if not isinstance(text, str):
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


def _order(messages):
    """Stable order a reader can follow: brief, then each story's fields in the order
    they appear in the draft, then whole-draft rules."""
    def key(item):
        index, msg = item
        if msg.startswith("brief"):
            return (0, 0, 0, index)
        m = re.match(r"stories\[(\d+)\]\.?(\w+)?", msg)
        if m:
            field = m.group(2)
            rank = STORY_FIELD_ORDER.index(field) if field in STORY_FIELD_ORDER else len(STORY_FIELD_ORDER)
            return (1, int(m.group(1)), rank, index)
        return (2, 0, 0, index)
    return [msg for _, msg in sorted(enumerate(messages), key=key)]


def validate_draft(draft, candidates, topic_labels, settings, source_texts=None):
    """Returns a list of human-readable errors; empty means valid."""
    source_texts = source_texts or {}
    if not isinstance(draft, dict):
        return ["draft must be a JSON object with 'brief' and 'stories'"]

    # 1. structure, from the models
    bad = set()
    try:
        DraftEdition.model_validate(draft)
        errors, fatal = [], False
    except ValidationError as exc:
        errors, fatal = draft_errors(exc, draft, topic_labels)
        bad = {tuple(e["loc"]) for e in exc.errors()}

    def skip(*loc):
        """True when the model already reported this value (or the list holding it)."""
        return any(tuple(loc[:k]) in bad for k in range(1, len(loc) + 1))

    # 2. content rules
    brief = draft.get("brief")
    if isinstance(brief, list) and not skip("brief"):
        for i, line in enumerate(brief):
            if not skip("brief", i):
                check_prose(f"brief[{i}]", line, errors)

    stories = draft.get("stories")
    limit = settings.get("stories_per_edition", 30)
    if fatal or not isinstance(stories, list) or not stories:
        return _order(errors)
    if len(stories) > limit + 5:
        errors.append(f"stories: {len(stories)} stories, more than stories_per_edition ({limit}) allows")

    used = {}
    must_reads = 0
    for n, story in enumerate(stories):
        where = f"stories[{n}]"
        if not isinstance(story, dict):
            continue
        ids = story.get("ids")
        if skip("stories", n, "ids") or not isinstance(ids, list) or not ids or not all(isinstance(i, int) for i in ids):
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
        if not skip("stories", n, "headline") or isinstance(headline, str) and len(headline.strip()) >= 15:
            check_prose(f"{where}.headline", headline, errors)
        if not skip("stories", n, "dek"):
            check_prose(f"{where}.dek", story.get("dek"), errors, source_ngrams=source_ngrams)

        body = story.get("body")
        if isinstance(body, list) and not skip("stories", n, "body"):
            for p, para in enumerate(body):
                if skip("stories", n, "body", p):
                    continue
                check_prose(f"{where}.body[{p}]", para, errors, source_ngrams=source_ngrams)
                if isinstance(para, str) and not ENDS_CLEANLY.search(para):
                    errors.append(f"{where}.body[{p}]: doesn't end with punctuation -- looks cut off mid-sentence")
            if isinstance(headline, str) and body and isinstance(body[0], str) \
                    and body[0].lower().startswith(headline.lower()[:40]):
                errors.append(f"{where}.body[0]: opens by restating the headline")

        takeaways = story.get("takeaways", [])
        if isinstance(takeaways, list) and not skip("stories", n, "takeaways"):
            for t, item in enumerate(takeaways):
                if not skip("stories", n, "takeaways", t):
                    check_prose(f"{where}.takeaways[{t}]", item, errors, source_ngrams=source_ngrams)

        if not skip("stories", n, "event") and story.get("event"):
            grounding = " ".join([str(headline or ""), str(story.get("dek") or "")]
                                 + [(candidates.get(str(c)) or {}).get("title", "") for c in ids])
            problem = event_problem(story["event"], grounding)
            if problem:
                errors.append(f"{where}.event: {problem}")

        if not skip("stories", n, "topic") and story.get("topic") not in topic_labels:
            errors.append(f"{where}.topic: {story.get('topic')!r} -- must be one of {topic_labels}")
        signal = story.get("signal")
        must_reads += signal == "must-read"

    if isinstance(stories[0], dict) and stories[0].get("signal") != "must-read":
        errors.append("stories[0]: the lead story must be signal 'must-read'")
    cap = settings.get("must_read_max", 6)
    if must_reads > cap:
        errors.append(f"{must_reads} must-read stories -- at most {cap}; must-read should mean it")
    return _order(errors)


def validate_edition(edition, where="edition"):
    """Check of a published edition (used by CI and by publish_edition.py before it
    writes anything): structure from the models, then the placeholder/markup rules."""
    data = {k: v for k, v in edition.items() if k not in BUILD_KEYS}
    try:
        data = migrate(data)
    except SchemaVersionError as exc:
        return [f"{where}: {exc}"]
    errors = []
    try:
        PublishedEdition.model_validate(data)
    except ValidationError as exc:
        errors += edition_errors(exc, where)
    stories = data.get("stories")
    for n, story in enumerate(stories if isinstance(stories, list) else []):
        if not isinstance(story, dict):
            continue
        at = f"{where}.stories[{n}]"
        # optional: editions published before the event field existed don't have one
        if story.get("event") and event_problem(story["event"]):
            errors.append(f"{at}.event: {event_problem(story['event'])}")
        body = story.get("body")
        values = [("headline", story.get("headline")), ("dek", story.get("dek"))]
        values += [(f"body[{i}]", p) for i, p in enumerate(body if isinstance(body, list) else [])]
        for field, value in values:
            if isinstance(value, str) and (PLACEHOLDERS.search(value) or MARKUP.search(value)):
                errors.append(f"{at}.{field}: placeholder or markup in published text")
    return errors
