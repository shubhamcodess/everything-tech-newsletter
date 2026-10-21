"""Spotting a story the paper already ran.

data/seen.json remembers every URL featured in the last dedup_lookback_days, and
build_candidates.py drops those exactly. That misses the usual repeat: the same
event covered again the next day by another outlet, so a different URL. This
module recognises it by wording instead, using three things recorded for each
featured story (see publish_edition.py):

    headline   what the paper called it
    titles     the original titles of every outlet in the story's cluster
    event      3-6 keywords the editor wrote for it (validated in edition_schema.py)

A new candidate cluster "matches" a featured story when one of its titles shares
at least two content words with one of the story's titles/event, and at least one
of those words is distinctive -- rare among today's candidates, so it names the
thing ("deno", "embeddinggemma") and isn't just vocabulary ("model", "openai").

A match never removes anything. It is shown to the editor as a tag, because a
follow-up with new facts is a different story from a second outlet's take, and
wording alone can't always tell them apart (see scripts/eval_dedupe.py).
"""
import re
from collections import Counter, defaultdict

STOP = set(
    "a an and are as at be by for from has have how in into is it its of on or "
    "that the their this to was what when why will with you your new now after "
    "about over says just more than can could may via using use".split()
)

# A word is distinctive when it appears in at most this many stories, counting
# today's candidate clusters and the recently featured ones. A story covered on
# several earlier days counts several times, so this must allow for that.
# Calibrated by replaying past editions: scripts/eval_dedupe.py.
DISTINCT_MAX_DOCS = 5
MIN_SHARED = 2
MIN_DISTINCT = 2


def title_tokens(title: str) -> set:
    words = re.findall(r"[a-z0-9][a-z0-9.+#-]*", title.lower())
    return {w for w in words if len(w) > 2 and w not in STOP}


def stem(word: str) -> str:
    for suffix in ("ing", "ed", "es", "s"):
        if len(word) > 4 and word.endswith(suffix):
            return word[: -len(suffix)]
    return word


def tokens(text: str) -> set:
    return {stem(w) for w in title_tokens(text)}


# ---------------------------------------------------------------- event field

EVENT_WORD = re.compile(r"^[a-z0-9][a-z0-9.+#-]*$")


def normalize_event(text) -> str:
    """'  Cloudflare buys  Deno ' -> 'cloudflare buys deno'."""
    return re.sub(r"\s+", " ", str(text or "").strip().lower())


def event_problem(text, grounding_text="") -> str:
    """Why an event keyword line is unusable, or '' when it's fine.
    grounding_text is the story's headline, dek and candidate titles: the event
    has to be about that story, not a generic label."""
    event = normalize_event(text)
    words = event.split()
    if not 3 <= len(words) <= 6:
        return f"must be 3-6 lowercase keywords naming the event, e.g. 'cloudflare deno acquisition' (got {len(words)} words)"
    bad = [w for w in words if not EVENT_WORD.match(w) or len(w) > 24]
    if bad:
        return f"keywords only -- no punctuation, URLs or long strings (problem: {bad[0]!r})"
    if len(tokens(event)) < 2:
        return "needs at least two content words (who and what), not filler"
    if grounding_text and len(tokens(event) & tokens(grounding_text)) < 2:
        return "keywords don't appear in this story's headline, summary or source titles -- describe this story's event"
    return ""


# ------------------------------------------------------------------- matching

def prior_stories(seen, today, lookback_days=7):
    """Stories featured before today, as {date, headline, event, titles}.
    Reads seen['stories'] when present and falls back to grouping the older
    per-URL 'featured' entries by (date, headline), so seen.json files written
    before the event field existed keep working."""
    cutoff = today.fromordinal(today.toordinal() - lookback_days).isoformat()
    today_s = today.isoformat()
    out, have = [], set()
    for s in seen.get("stories", []):
        if cutoff <= s.get("date", "") < today_s:
            out.append({"date": s["date"], "headline": s.get("headline", ""),
                        "event": s.get("event", ""), "titles": list(s.get("titles", []))})
            have.add((s["date"], s.get("headline", "")))
    legacy = defaultdict(set)
    for item in seen.get("featured", []):
        date, title = item.get("date", ""), item.get("title", "")
        if cutoff <= date < today_s and (date, title) not in have and title:
            legacy[(date, title)].add(title)
    out += [{"date": d, "headline": h, "event": "", "titles": []} for (d, h) in legacy]
    return out


def _story_phrases(story):
    return [p for p in [story["headline"], story["event"], *story["titles"]] if p]


def find_covered(cluster_titles, prior):
    """For each cluster (a list of its members' titles) the best-matching prior
    story, or None. Returns [(prior_story, shared_words) | None, ...]."""
    prior_sets = [(p, [tokens(x) for x in _story_phrases(p)]) for p in prior]
    docs = [set().union(*(tokens(t) for t in titles)) if titles else set() for titles in cluster_titles]
    docs += [set().union(*sets) if sets else set() for _, sets in prior_sets]
    df = Counter(t for d in docs for t in d)

    results = []
    for titles in cluster_titles:
        mine = [tokens(t) for t in titles]
        best, best_score = None, 0.0
        for p, p_sets in prior_sets:
            for a in mine:
                for b in p_sets:
                    shared = a & b
                    if len(shared) < MIN_SHARED:
                        continue
                    distinct = [t for t in shared if df[t] <= DISTINCT_MAX_DOCS]
                    if len(distinct) < MIN_DISTINCT:
                        continue
                    score = len(shared) + len(distinct)
                    if score > best_score:
                        best, best_score = (p, sorted(shared)), score
        results.append(best)
    return results
