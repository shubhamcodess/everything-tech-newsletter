# Prompt to paste into the routine's "Instructions" box

Paste the text below (between the lines) as the routine's prompt at
claude.ai/code/routines/new. It's short because the real detail lives in
this repo's `CLAUDE.md`, which the routine reads automatically once the
repo is attached — that keeps this prompt from going stale if the pipeline
changes later.

---

Run today's tech newsletter for this repo. Follow the pipeline in CLAUDE.md
exactly, in order: install deps, fetch all sources, load config/interests.json
and config/settings.json and data/seen.json, filter to the interest boundary,
cluster duplicate stories, judge and rank the top `articles_per_digest`
stories yourself (there is no scoring formula -- use your own judgment per
CLAUDE.md), write docs/index.html, update data/seen.json, then commit and
push both to main. If a source fails, fix it if the cause is obvious
(see CLAUDE.md's Maintenance section), otherwise skip it and note it. End
with a short summary: sources ok/failed, articles fetched, articles featured.

---
