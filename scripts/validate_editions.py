"""CI check: every editions/<date>/edition.md parses and is sound, and docs/data
is exactly what build_site.py would produce from them (so nobody ships an
edition or a config change without rebuilding). An empty archive -- a fresh
fork before its first run -- is valid."""
import filecmp
import glob
import json
import os
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import edition_md  # noqa: E402
from edition_schema import validate_edition  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    errors = []
    for path in sorted(glob.glob(os.path.join(ROOT, "editions", "20*", "edition.md"))):
        date = os.path.basename(os.path.dirname(path))
        try:
            edition = edition_md.parse(open(path).read())
        except edition_md.ParseError as exc:
            errors.append(f"editions/{date}/edition.md: {exc}")
            continue
        errors += validate_edition({**edition, "date": date, "topics": []}, where=f"editions/{date}")

    with tempfile.TemporaryDirectory() as tmp:
        shutil.copytree(os.path.join(ROOT, "docs"), os.path.join(tmp, "before"))
        subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "build_site.py")], check=True, capture_output=True)
        diff = filecmp.dircmp(os.path.join(tmp, "before", "data"), os.path.join(ROOT, "docs", "data"))
        changed = diff.diff_files + diff.left_only + diff.right_only
        if changed:
            errors.append(f"docs/data is out of date ({', '.join(changed)}) -- run python scripts/build_site.py and commit")

    if errors:
        print("\n".join(f"- {e}" for e in errors))
        sys.exit(1)
    print("editions and docs/data OK")


if __name__ == "__main__":
    main()
