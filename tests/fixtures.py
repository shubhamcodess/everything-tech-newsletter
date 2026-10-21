"""Shared test data: a valid draft, its candidates, and a table of ways to break it.

The mutations are the failure classes edition_schema.py exists to catch. The
golden files in tests/golden/ record what the validators said about every one of
them *before* the schema refactor (#26); test_schema.py holds the new validators
to the same answers.
"""
import copy
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

TOPICS = ["AI", "Dev Tools", "Languages", "Open Source", "Startups", "Infra", "Security", "Engineering"]
SETTINGS = {"stories_per_edition": 30, "must_read_max": 6}


def candidates(n=45):
    """Candidate id -> metadata, as data/candidates.json holds it."""
    return {str(i): {"title": f"Zorbex{i} launches Quantum{i} gateway for Plinth{i} clusters",
                     "summary": f"Zorbex{i} announced that the Quantum{i} gateway routes traffic between "
                                f"Plinth{i} clusters while keeping latency under four milliseconds for every region."}
            for i in range(1, n + 1)}


def make_story(i, signal="recommended"):
    return {
        "headline": f"Zorbex{i} ships Quantum{i} gateway to route Plinth{i} clusters",
        "dek": f"The Quantum{i} gateway lets operators move traffic between clusters without a redeploy, which changes how teams plan failovers.",
        "body": [
            f"Zorbex{i} released the Quantum{i} gateway this week. It sits in front of Plinth{i} clusters and moves traffic between them on demand, so operators can drain a region without touching the applications behind it.",
            f"Early users report that failover drills now take minutes instead of an afternoon. The catch is that the gateway needs its own health checks, which teams must write and keep current.",
        ],
        "takeaways": [f"Check whether your Plinth{i} clusters can drain traffic safely before adopting it."],
        "sources": [],
        "ids": [i],
        "topic": "Infra",
        "signal": signal,
        "event": f"zorbex{i} quantum{i} gateway release",
    }


def valid_draft():
    return {
        "brief": [
            "Gateways are becoming the place where failover is decided, not applications.",
            "Teams adopting traffic gateways need health checks they own and maintain.",
            "Release notes now matter less than drills that prove a failover works.",
        ],
        "stories": [make_story(1, "must-read"), make_story(2), make_story(3, "notable")],
    }


def _lead(d):
    return d["stories"][0]


def _many(d, n, signal="recommended"):
    d["stories"] = [make_story(1, "must-read")] + [make_story(i, signal) for i in range(2, n + 1)]


def _set(path, value):
    """Mutation setting a nested value; path like 'stories.0.headline'."""
    def apply(d):
        node = d
        keys = path.split(".")
        for k in keys[:-1]:
            node = node[int(k)] if isinstance(node, list) else node[k]
        last = keys[-1]
        if isinstance(node, list):
            node[int(last)] = value
        else:
            node[last] = value
    return apply


def _drop(path):
    def apply(d):
        node = d
        keys = path.split(".")
        for k in keys[:-1]:
            node = node[int(k)] if isinstance(node, list) else node[k]
        del node[keys[-1]]
    return apply


def _dup_id(d):
    d["stories"][1]["ids"] = [1]


COPIED = ("Zorbex1 announced that the Quantum1 gateway routes traffic between Plinth1 clusters while "
          "keeping latency under four milliseconds for every region")

MUTATIONS = {
    "valid": lambda d: None,
    "draft_extra_keys_ignored": _set("stories.0.image", "https://example.com/x.png"),
    "not_a_dict": lambda d: d.clear(),  # replaced below
    "brief_missing": _drop("brief"),
    "brief_two_lines": lambda d: d.update(brief=d["brief"][:2]),
    "brief_seven_lines": lambda d: d.update(brief=d["brief"] * 3),
    "brief_line_short": _set("brief.0", "too short"),
    "brief_line_not_string": _set("brief.0", 5),
    "brief_line_html": _set("brief.0", "Gateways are <b>becoming</b> the place where failover is decided."),
    "stories_missing": _drop("stories"),
    "stories_empty": _set("stories", []),
    "stories_not_list": _set("stories", "nope"),
    "stories_too_many": lambda d: _many(d, 36),
    "stories_at_limit_plus_five": lambda d: _many(d, 35),
    "story_not_object": _set("stories.1", 5),
    "ids_missing": _drop("stories.0.ids"),
    "ids_empty": _set("stories.0.ids", []),
    "ids_strings": _set("stories.0.ids", ["1"]),
    "ids_not_list": _set("stories.0.ids", 1),
    "ids_unknown": _set("stories.0.ids", [999]),
    "ids_duplicate_across_stories": _dup_id,
    "headline_missing": _drop("stories.0.headline"),
    "headline_short": _set("stories.0.headline", "Too short"),
    "headline_long": _set("stories.0.headline", "Zorbex1 " + "very " * 30 + "long headline"),
    "headline_placeholder": _set("stories.0.headline", "ARTICLE_TITLE goes here for the gateway"),
    "headline_html": _set("stories.0.headline", "Zorbex1 ships &amp; <i>routes</i> gateway traffic"),
    "headline_raw_url": _set("stories.0.headline", "Zorbex1 ships gateway https://example.com/gw"),
    "headline_filler": _set("stories.0.headline", "Zorbex1 ships an important update for the gateway"),
    "headline_not_string": _set("stories.0.headline", 12345),
    "dek_missing": _drop("stories.0.dek"),
    "dek_short": _set("stories.0.dek", "Short dek."),
    "dek_copied_from_source": _set("stories.0.dek", COPIED + ", which changes failovers."),
    "dek_not_string": _set("stories.0.dek", ["x"]),
    "body_missing": _drop("stories.0.body"),
    "body_empty": _set("stories.0.body", []),
    "body_seven_paragraphs": lambda d: _lead(d).update(body=_lead(d)["body"] * 4),
    "body_not_list": _set("stories.0.body", "one long string"),
    "body_para_short": _set("stories.0.body.0", "Too short."),
    "body_para_cut_off": _set("stories.0.body.0", "Zorbex1 released the Quantum1 gateway this week and it sits in front of Plinth1 clusters and moves traffic bet"),
    "body_restates_headline": _set("stories.0.body.0", "Zorbex1 ships Quantum1 gateway to route Plinth1 clusters, and operators can now drain a region without touching apps."),
    "body_copied_from_source": _set("stories.0.body.0", "Operators say " + COPIED + " and that is all anyone needs."),
    "body_filler": _set("stories.0.body.1", "Early users report quick drills, which is a growing trend across every team that runs clusters at scale."),
    "body_html": _set("stories.0.body.1", "Early users report <b>quick</b> drills now that the gateway handles the traffic shifts for them automatically."),
    "body_placeholder": _set("stories.0.body.1", "Early users report quick drills now that ARTICLE_URL handles the traffic shifts for them automatically."),
    "takeaways_absent_ok": _drop("stories.0.takeaways"),
    "takeaways_six": lambda d: _lead(d).update(takeaways=["Check whether your clusters can drain safely."] * 6),
    "takeaways_not_list": _set("stories.0.takeaways", "do this"),
    "takeaway_short": _set("stories.0.takeaways.0", "Do it."),
    "takeaway_filler": _set("stories.0.takeaways.0", "Stay tuned for the next gateway release notes."),
    "event_missing": _drop("stories.0.event"),
    "event_empty": _set("stories.0.event", ""),
    "event_two_words": _set("stories.0.event", "zorbex1 gateway"),
    "event_seven_words": _set("stories.0.event", "zorbex1 quantum1 gateway release for plinth1 clusters"),
    "event_punctuation": _set("stories.0.event", "zorbex1, quantum1: gateway!"),
    "event_ungrounded": _set("stories.0.event", "stock market rally today"),
    "event_not_string": _set("stories.0.event", 7),
    "topic_missing": _drop("stories.0.topic"),
    "topic_unknown": _set("stories.0.topic", "Gardening"),
    "signal_missing": _drop("stories.0.signal"),
    "signal_unknown": _set("stories.1.signal", "must-see"),
    "lead_not_must_read": _set("stories.0.signal", "recommended"),
    "seven_must_reads": lambda d: _many(d, 7, "must-read"),
    "six_must_reads_ok": lambda d: _many(d, 6, "must-read"),
    "several_problems_at_once": lambda d: (_set("stories.0.headline", "Short")(d), _set("stories.1.ids", [999])(d),
                                          _set("stories.2.topic", "Nope")(d), _set("brief", ["x"])(d)),
}


def build_case(name):
    """(draft, source_texts) for one mutation; the unmutated draft is always valid."""
    draft = copy.deepcopy(valid_draft())
    MUTATIONS[name](draft)
    if name == "not_a_dict":
        draft = []
    return draft, {"1": "Plinth1 clusters were announced in the release notes of the product, nothing more."}


def published_edition():
    """A published-style edition dict built from real fields (what edition_md.parse returns)."""
    stories = []
    for i in (1, 2):
        s = make_story(i, "must-read" if i == 1 else "recommended")
        s.update(url=f"https://example.com/zorbex{i}", source_title=f"Zorbex{i} launches Quantum{i}",
                 sources=[{"name": "example.com", "url": f"https://example.com/zorbex{i}"}], full_text=True)
        stories.append(s)
    return {"date": "2026-10-01", "edition": 5, "generated_at": "2026-10-01T03:00:00+00:00",
            "sources_ok": 40, "sources_total": 47, "fetched": 300, "candidates": 200, "full_text": 20,
            "brief": copy.deepcopy(valid_draft()["brief"]), "stories": stories, "topics": []}


PUBLISHED_MUTATIONS = {
    "valid": lambda e: None,
    "no_event_legacy_ok": lambda e: [s.pop("event") for s in e["stories"]],
    "missing_date": lambda e: e.pop("date"),
    "missing_edition": lambda e: e.pop("edition"),
    "missing_brief": lambda e: e.pop("brief"),
    "missing_stories": lambda e: e.pop("stories"),
    "story_no_headline": lambda e: e["stories"][0].pop("headline"),
    "story_no_dek": lambda e: e["stories"][0].pop("dek"),
    "story_empty_body": lambda e: e["stories"][0].update(body=[]),
    "story_no_topic": lambda e: e["stories"][0].pop("topic"),
    "story_no_signal": lambda e: e["stories"][0].pop("signal"),
    "story_no_url": lambda e: e["stories"][0].pop("url"),
    "story_no_sources": lambda e: e["stories"][0].update(sources=[]),
    "story_bad_url": lambda e: e["stories"][0].update(url="ftp://example.com/x"),
    "story_relative_url": lambda e: e["stories"][0].update(url="example.com/x"),
    "headline_placeholder": lambda e: e["stories"][0].update(headline="ARTICLE_TITLE for a gateway story"),
    "dek_markup": lambda e: e["stories"][0].update(dek="The <b>gateway</b> moves traffic between regions without redeploys."),
    "body_entity": lambda e: e["stories"][0]["body"].append("Operators &amp; teams love it as the gateway handles every failover for them."),
    "event_bad": lambda e: e["stories"][0].update(event="gateway"),
    "event_fine": lambda e: e["stories"][0].update(event="zorbex1 gateway release"),
}


def build_published_case(name):
    e = copy.deepcopy(published_edition())
    PUBLISHED_MUTATIONS[name](e)
    return e
