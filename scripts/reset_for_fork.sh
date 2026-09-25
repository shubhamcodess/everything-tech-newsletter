#!/usr/bin/env bash
# Resets generated state so a fresh fork starts clean: no editions, empty
# archive, no remembered stories. The site shows an "awaiting the first
# edition" page until the routine's first run. Run once after forking, then commit.
set -euo pipefail
cd "$(dirname "$0")/.."

rm -rf editions/20*
echo '{"featured": []}' > data/seen.json
python3 scripts/build_site.py
echo "Reset done. Now edit config/site.json and config/interests.json (see README), then commit and push."
