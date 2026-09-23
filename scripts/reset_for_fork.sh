#!/usr/bin/env bash
# Resets generated state so a fresh fork starts clean: an "awaiting first run"
# placeholder as the live page, an empty archive, and no remembered stories.
# Run once from the repo root after forking, then commit.
set -euo pipefail
cd "$(dirname "$0")/.."

cp templates/placeholder.html docs/index.html
sed '1,/^-->$/d' templates/archive.html.template > docs/archive/index.html
find docs/archive -name '20*.html' -delete
rm -f docs/sample-output.html
echo '{"featured": []}' > data/seen.json
echo "Reset done. Now personalize (see README), then commit and push."
