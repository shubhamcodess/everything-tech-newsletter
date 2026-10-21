"""Records what the validators say today. Run ONCE, on the pre-refactor code:

    python tests/make_golden.py

and commit tests/golden/. tests/frozen/ holds copies of real editions, version 0 of
the format, kept so old editions stay tested after the archive prunes them. test_schema.py then holds every later version of the
validators to these answers. Re-run it only when a validation rule is changed on
purpose, and review the diff of tests/golden/ like any other change.
"""
import glob
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tests import fixtures as fx  # noqa: E402

import edition_md  # noqa: E402
from edition_schema import validate_draft, validate_edition  # noqa: E402

GOLDEN = os.path.join(fx.ROOT, "tests", "golden")


def digest(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def main():
    os.makedirs(GOLDEN, exist_ok=True)
    drafts = {}
    for name in fx.MUTATIONS:
        draft, source_texts = fx.build_case(name)
        drafts[name] = validate_draft(draft, fx.candidates(), fx.TOPICS, fx.SETTINGS, source_texts)
    published = {name: validate_edition(fx.build_published_case(name)) for name in fx.PUBLISHED_MUTATIONS}
    real = {}
    for path in sorted(glob.glob(os.path.join(fx.ROOT, "tests", "frozen", "20*.md"))):
        date = os.path.basename(path)[:-3]
        with open(path) as f:
            edition = edition_md.parse(f.read())
        real[date] = {"parsed_sha256": digest(edition),
                      "errors": validate_edition({**edition, "date": date, "topics": []}, where=f"editions/{date}")}
    for name, data in (("draft_errors", drafts), ("published_errors", published), ("real_editions", real)):
        with open(os.path.join(GOLDEN, f"{name}.json"), "w") as f:
            json.dump(data, f, indent=1, ensure_ascii=False, sort_keys=True)
            f.write("\n")
    bad = [d for d, v in real.items() if v["errors"]]
    print(f"{len(drafts)} draft cases, {len(published)} published cases, {len(real)} real editions "
          f"({len(bad)} with errors: {bad})")
    print("valid draft ->", drafts["valid"], "| valid published ->", published["valid"])


if __name__ == "__main__":
    main()
