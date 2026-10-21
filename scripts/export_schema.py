"""Writes the edition contract as JSON Schema, for tools that aren't Python.

    python scripts/export_schema.py           # (re)generate schema/*.schema.json
    python scripts/export_schema.py --check   # exit 1 if the committed files are stale

schema/edition.schema.json   a published edition (editions/<date>/edition.md, as parsed)
schema/draft.schema.json     what the routine writes (data/draft.md, as parsed); also what
                             a structured-output API call would have to return

The Python models in edition_model.py are the source of truth; these files are
generated from them. The schema covers structure only -- content rules (copied text,
filler, ids that exist, topic labels) live in edition_schema.py.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from edition_model import SCHEMA_VERSION, DraftEdition, PublishedEdition  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "schema")

TARGETS = {
    "edition.schema.json": (PublishedEdition, "EverythingTech edition",
                            "A published edition, as parsed from editions/<date>/edition.md."),
    "draft.schema.json": (DraftEdition, "EverythingTech edition draft",
                          "What the routine writes to data/draft.md, as parsed."),
}


def render(model, title, description):
    schema = model.model_json_schema()
    schema = {"$schema": "https://json-schema.org/draft/2020-12/schema", "title": title, "description": description,
              "x-schema-version": SCHEMA_VERSION, **schema}
    return json.dumps(schema, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def main():
    check = "--check" in sys.argv
    stale = []
    for name, (model, title, description) in TARGETS.items():
        path = os.path.join(OUT, name)
        text = render(model, title, description)
        if check:
            if not os.path.exists(path) or open(path).read() != text:
                stale.append(name)
        else:
            os.makedirs(OUT, exist_ok=True)
            with open(path, "w") as f:
                f.write(text)
            print(f"wrote schema/{name}")
    if check:
        if stale:
            print(f"stale: {', '.join(stale)} -- run python scripts/export_schema.py and commit")
            sys.exit(1)
        print("schema files are up to date")


if __name__ == "__main__":
    main()
