"""Tests for the edition contract (#26): models, migration, validators.

Run:  python -m unittest discover -s tests -t .

The golden files in tests/golden/ were recorded from the validators as they were
before the schema refactor (tests/make_golden.py). Every draft and published case
must still produce exactly the same messages: the routine fixes its drafts by
reading them, so wording and wherever a rule fires are part of the interface.
"""
import copy
import glob
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

from tests import fixtures as fx

import edition_md  # noqa: E402
from edition_model import (SCHEMA_VERSION, DraftEdition, PublishedEdition, PublishedStory,  # noqa: E402
                           SchemaVersionError, migrate)
from edition_schema import validate_draft, validate_edition  # noqa: E402

GOLDEN = os.path.join(fx.ROOT, "tests", "golden")


def golden(name):
    with open(os.path.join(GOLDEN, f"{name}.json")) as f:
        return json.load(f)


def read_bytes(path):
    with open(path, "rb") as f:
        return f.read()


def frozen_editions():
    """Real editions copied into tests/frozen/: the oldest shape of the format, which the
    live archive will eventually prune away."""
    out = {}
    for path in sorted(glob.glob(os.path.join(fx.ROOT, "tests", "frozen", "20*.md"))):
        with open(path) as f:
            out[os.path.basename(path)[:-3]] = f.read()
    return out


def live_editions():
    out = {}
    for path in sorted(glob.glob(os.path.join(fx.ROOT, "editions", "20*", "edition.md"))):
        with open(path) as f:
            out[os.path.basename(os.path.dirname(path))] = f.read()
    return out


class DraftParity(unittest.TestCase):
    def test_every_case_matches_the_recorded_answer(self):
        recorded = golden("draft_errors")
        self.assertGreaterEqual(len(recorded), 60)
        for name, expected in recorded.items():
            with self.subTest(case=name):
                draft, source_texts = fx.build_case(name)
                got = validate_draft(draft, fx.candidates(), fx.TOPICS, fx.SETTINGS, source_texts)
                self.assertEqual(got, expected)

    def test_a_valid_draft_is_valid_for_the_model_too(self):
        DraftEdition.model_validate(fx.valid_draft())

    def test_draft_text_round_trips_through_the_parser(self):
        """What the routine really writes: Markdown, parsed, validated."""
        text = ["# The Brief", ""] + [f"- {b}" for b in fx.valid_draft()["brief"]] + ["", "# Stories", ""]
        for s in fx.valid_draft()["stories"]:
            text += [f"## {s['headline']}", f"- ids: {', '.join(map(str, s['ids']))}", f"- topic: {s['topic']}",
                     f"- signal: {s['signal']}", f"- event: {s['event']}", "", f"> {s['dek']}", ""]
            text += [p + "\n" for p in s["body"]] + ["**Takeaways**"] + [f"- {t}" for t in s["takeaways"]] + [""]
        draft = edition_md.parse("\n".join(text))
        self.assertEqual(validate_draft(draft, fx.candidates(), fx.TOPICS, fx.SETTINGS), [])


class PublishedParity(unittest.TestCase):
    def test_every_case_matches_the_recorded_answer(self):
        for name, expected in golden("published_errors").items():
            with self.subTest(case=name):
                got = validate_edition(fx.build_published_case(name))
                self.assertEqual(sorted(got), sorted(expected))

    def test_build_keys_are_not_part_of_the_contract(self):
        e = fx.published_edition()
        e["stats"] = {"stories": 2}
        e["topics"] = ["AI"]
        self.assertEqual(validate_edition(e), [])


class LiveArchive(unittest.TestCase):
    """Whatever is in editions/ right now, today's included, satisfies the contract."""

    def test_every_published_edition_validates(self):
        for date, text in live_editions().items():
            with self.subTest(date=date):
                edition = edition_md.parse(text)
                self.assertEqual(edition.get("date"), date, "front matter date must match the folder")
                self.assertEqual(validate_edition(edition, where=date), [])


class OldEditions(unittest.TestCase):
    """Editions from before the schema existed must keep working, however the archive
    prunes: these are frozen copies."""

    @classmethod
    def setUpClass(cls):
        cls.texts = frozen_editions()
        cls.golden = golden("real_editions")

    def test_the_frozen_set_is_intact(self):
        self.assertEqual(sorted(self.texts), sorted(self.golden))
        self.assertGreaterEqual(len(self.texts), 8)

    def test_parsing_is_unchanged(self):
        for date, text in self.texts.items():
            with self.subTest(date=date):
                edition = edition_md.parse(text)
                digest = __import__("hashlib").sha256(
                    json.dumps(edition, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
                self.assertEqual(digest, self.golden[date]["parsed_sha256"])

    def test_every_edition_validates_with_the_models(self):
        for date, text in self.texts.items():
            with self.subTest(date=date):
                self.assertEqual(validate_edition(edition_md.parse(text), where=date), [])
                self.assertEqual(self.golden[date]["errors"], [])

    def test_every_story_fits_the_published_story_model(self):
        total = 0
        for date, text in self.texts.items():
            for n, story in enumerate(edition_md.parse(text)["stories"]):
                PublishedStory.model_validate(story)
                total += 1
        self.assertGreaterEqual(total, 150)

    def test_old_editions_are_version_zero_and_migrate_to_current(self):
        for date, text in self.texts.items():
            with self.subTest(date=date):
                edition = edition_md.parse(text)
                if "schema_version" in edition:
                    continue  # published after the field existed
                before = copy.deepcopy(edition)
                migrated = migrate(edition)
                self.assertEqual(edition, before, "migrate() must not mutate its input")
                self.assertEqual(migrated["schema_version"], SCHEMA_VERSION)
                self.assertEqual({k: v for k, v in migrated.items() if k != "schema_version"}, before)
                PublishedEdition.model_validate(migrated)

    def test_writing_and_reading_back_is_stable(self):
        """edition_md.write(parse(x)) parses back to the same edition."""
        for date, text in self.texts.items():
            with self.subTest(date=date):
                edition = edition_md.parse(text)
                stats = {k: edition[k] for k in ("sources_ok", "sources_total", "fetched", "candidates", "full_text")
                         if k in edition}
                canonical = {**{k: v for k, v in edition.items() if k not in stats}, "stats": stats}
                again = edition_md.parse(edition_md.write(canonical))
                self.assertEqual(again, edition)

    def test_published_with_a_version_round_trips(self):
        edition = {**fx.published_edition(), "schema_version": SCHEMA_VERSION}
        stats = {k: edition.pop(k) for k in ("sources_ok", "sources_total", "fetched", "candidates", "full_text")}
        edition.pop("topics")
        edition["stats"] = stats
        again = edition_md.parse(edition_md.write(edition))
        self.assertEqual(again["schema_version"], SCHEMA_VERSION)
        self.assertEqual(validate_edition(again), [])

    def test_damaged_old_editions_are_caught(self):
        """Break each real edition in several ways; the validator must notice every time."""
        breakers = {
            "headline removed": lambda e: e["stories"][0].pop("headline"),
            "dek emptied": lambda e: e["stories"][1].update(dek=""),
            "body emptied": lambda e: e["stories"][2].update(body=[]),
            "url not http": lambda e: e["stories"][0].update(url="www.example.com"),
            "sources emptied": lambda e: e["stories"][0].update(sources=[]),
            "signal invalid": lambda e: e["stories"][0].update(signal="urgent"),
            "story id not number": lambda e: e["stories"][0].update(ids=["a"]),
            "points not number": lambda e: e["stories"][0].update(points="many"),
            "unknown field added": lambda e: e["stories"][0].update(headlne="typo"),
            "placeholder text": lambda e: e["stories"][0].update(dek="ARTICLE_TITLE"),
            "markup in body": lambda e: e["stories"][0]["body"].append("&amp; <b>x</b>"),
            "edition number lost": lambda e: e.pop("edition"),
            "future version": lambda e: e.update(schema_version=SCHEMA_VERSION + 1),
        }
        for date, text in self.texts.items():
            for label, apply in breakers.items():
                with self.subTest(date=date, damage=label):
                    edition = edition_md.parse(text)
                    apply(edition)
                    self.assertTrue(validate_edition(edition, where=date), f"{label} went unnoticed in {date}")


class Versions(unittest.TestCase):
    def test_missing_version_means_zero_and_upgrades(self):
        self.assertEqual(migrate({"a": 1})["schema_version"], SCHEMA_VERSION)

    def test_current_version_is_left_alone(self):
        self.assertEqual(migrate({"schema_version": SCHEMA_VERSION, "a": 1}), {"schema_version": SCHEMA_VERSION, "a": 1})

    def test_migration_is_idempotent(self):
        once = migrate({"a": 1})
        self.assertEqual(migrate(once), once)

    def test_newer_than_we_understand_is_a_clear_error(self):
        with self.assertRaises(SchemaVersionError) as ctx:
            migrate({"schema_version": SCHEMA_VERSION + 1})
        self.assertIn("update the scripts", str(ctx.exception))

    def test_nonsense_version_is_an_error(self):
        for bad in ("one", -1, 1.5, None):
            with self.subTest(version=bad), self.assertRaises(SchemaVersionError):
                migrate({"schema_version": bad})

    def test_validator_reports_a_future_version_instead_of_crashing(self):
        e = {**fx.published_edition(), "schema_version": 99}
        self.assertTrue(any("update the scripts" in m for m in validate_edition(e)))


class SiteBuildIsUnchanged(unittest.TestCase):
    def test_rebuilding_the_site_reproduces_the_committed_data(self):
        """The same check CI makes: docs/data is exactly what build_site.py produces."""
        with tempfile.TemporaryDirectory() as tmp:
            for part in ("scripts", "config", "editions", "docs"):
                shutil.copytree(os.path.join(fx.ROOT, part), os.path.join(tmp, part),
                                ignore=shutil.ignore_patterns("__pycache__"))
            subprocess.run([sys.executable, os.path.join(tmp, "scripts", "build_site.py")], check=True,
                           capture_output=True, cwd=tmp)
            for rel in ["latest.json", "feed.xml"] + [os.path.join("data", os.path.basename(p)) for p in
                                                       glob.glob(os.path.join(fx.ROOT, "docs", "data", "*"))]:
                with self.subTest(file=rel):
                    self.assertEqual(read_bytes(os.path.join(tmp, "docs", rel)),
                                     read_bytes(os.path.join(fx.ROOT, "docs", rel)))


class ExportedSchema(unittest.TestCase):
    def test_schema_files_are_up_to_date(self):
        result = subprocess.run([sys.executable, os.path.join(fx.ROOT, "scripts", "export_schema.py"), "--check"],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_schema_describes_the_contract(self):
        with open(os.path.join(fx.ROOT, "schema", "edition.schema.json")) as f:
            schema = json.load(f)
        self.assertEqual(schema["x-schema-version"], SCHEMA_VERSION)
        story = schema["$defs"]["PublishedStory"]
        self.assertIn("headline", story["required"])
        self.assertEqual(story["properties"]["signal"]["enum"], ["must-read", "recommended", "notable"])
        with open(os.path.join(fx.ROOT, "schema", "draft.schema.json")) as f:
            draft = json.load(f)
        self.assertEqual(draft["properties"]["brief"]["minItems"], 3)
        self.assertEqual(draft["$defs"]["DraftStory"]["properties"]["headline"]["maxLength"], 130)


if __name__ == "__main__":
    unittest.main()
