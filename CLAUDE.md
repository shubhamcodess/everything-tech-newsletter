# Tech Newsletter — routine instructions

Generates a daily digest at `docs/index.html`. GitHub Pages is configured
to deploy from the `main` branch's `/docs` folder directly — no build
step, no GitHub Action, no separate deploy trigger. Pushing to `docs/` is
the entire publish step. Runs unattended as a scheduled Claude Code
routine. Follow the steps below in order, exactly — don't explore the
repo beyond what each step names, don't touch files not listed, don't add
prose explanation beyond the final summary in step 11.

## Steps

1. `pip install -q -r scripts/requirements.txt`

2. `python scripts/fetch_all.py` → writes `data/raw_latest.json`. Failed
   sources are logged inside it, not fatal — continue regardless.

3. Read `config/interests.json` (topic whitelist), `config/settings.json`
   (`articles_per_digest`, `fetch_lookback_hours`, `dedup_lookback_days`),
   `data/seen.json` (recently featured stories to avoid repeating).

4. Filter `data/raw_latest.json`'s `articles`: keep only items published
   within `fetch_lookback_hours` AND matching at least one topic in
   `config/interests.json`. Drop everything else, no explanation needed.

5. Cluster: group articles covering the same underlying story (similar
   title/subject, regardless of source). One representative per cluster —
   pick the source with the highest `trust` value in `config/sources.json`.
   List the other sources in that cluster in the story's meta line.

6. Select exactly `articles_per_digest` clusters:
   - Drop any cluster whose title or url already appears in
     `data/seen.json` within the last `dedup_lookback_days` days.
   - Drop ads, coupon/promo posts, game hints/puzzles outright — not news.
   - Rank what's left by importance and substance (a real development beats
     a minor update; a specific, concrete story beats a vague one).
   - Diversity cap: at most `ceil(articles_per_digest / 5)` selected
     clusters per interest topic (5 for a 25-article digest, 2 for a
     10-article one), unless fewer than `articles_per_digest` clusters
     remain in total after the drops above.

7. Archive the outgoing digest, before it gets overwritten:
   - Check whether `docs/index.html` currently contains any
     `<div class="story">` elements. If it doesn't — this is the
     placeholder (first run ever), or a run failed midway last time —
     skip the rest of this step entirely, nothing to archive.
   - Otherwise, read the date from its `<div class="date">` and convert
     it to `YYYY-MM-DD`.
   - Copy `docs/index.html` unchanged to `docs/archive/<that-date>.html`.
   - In `docs/archive/index.html`, prepend one entry to the
     `<ul class="archive-list">`:
     `<li><a href="<date>.html"><date, spelled out></a></li>`. Remove the
     `<p class="empty-note">` line the first time you add an entry.
   - Cap at 7: if the list now has more than 7 `<li>` entries, delete the
     oldest one(s) and their corresponding `docs/archive/<date>.html`
     file(s), so the archive never grows past a week.

8. Write `docs/index.html`. Copy `templates/digest.html.template`'s
   structure and `<style>`/`<script>` exactly — the dark neon theme,
   header brand block, footer block, "how it works" popover, and load-more
   mechanism are fixed, byte-for-byte, on every run. Only the date and
   the story blocks change. One `<div class="story">` per pick, ranked
   order, each with a summary written per "Writing digest summaries"
   below — read that section before writing the first one, it's the part
   of this job that actually matters. Every story headline's
   `<a href="ARTICLE_URL">` must include `target="_blank"
   rel="noopener noreferrer"` — it opens the original source in a new
   tab, not internal links like the archive or repo link, which stay
   same-tab. The first 10 stories get `class="story"`; the
   11th onward get `class="story story-more"` (hidden by default, revealed
   by the template's load-more button) — see the template's comment for
   the exact markup. If `articles_per_digest` is 10 or fewer, every story
   is `class="story"` and the load-more button should not be rendered at
   all (the template shows how to omit it).

## Writing digest summaries

This is the part readers actually judge the digest on — a story with a
lazy summary is worse than no story at all. A real example from a past
run, to never repeat:

> "OpenAI GPT-6 Astra breaks Enigma message that has resisted solution
> since 2005. An important update for the tech industry."

Two failures stacked on top of each other: the first sentence just
restates the title word-for-word, and the second is generic filler that
could be glued onto literally any story unchanged. Do neither.

**Before writing each summary, check `data/raw_latest.json` for that
article's `summary` field** — if it has real content (most RSS sources
do), pull the specific fact from there, don't invent one. If it's empty
(common for Hacker News link posts and GitHub Trending, which have no
article text at all), the title itself is all you have — read it closely
for the specific noun/number/mechanism already in it, and build the
sentence around that, rather than writing something generic that ignores
it.

Rules, every story, no exceptions:
1. Never open by restating the title as a sentence. If you're tempted to
   write "X does Y" where X and Y are just copied from the title, stop —
   add or lead with a specific fact instead (a number, a name, a
   consequence, a comparison).
2. Never close on a sentence that isn't specific to this exact story.
   Banned phrases and close paraphrases of them — if what you wrote
   contains one, delete it and write something real: "important update",
   "significant development", "growing trend", "worth noting", "shows
   how", "highlights the", "underscores", "in the tech industry", "in
   the world of [X]", "continues to evolve".
3. Self-check before moving on: could this exact sentence be pasted
   under a different headline with zero changes? If yes, it's filler —
   rewrite it with something unique to this story.
4. Length is not the goal, coverage is — there is no sentence cap.
   Include everything a reader needs to actually understand the story
   without clicking through: the core action, concrete details (numbers,
   names, dates, technical specifics), why it matters, and any notable
   next steps or open questions the article raises. A short story that's
   genuinely simple can be one tight sentence; a story with real
   substance can run a full paragraph if that's what it takes to cover
   it properly. Never cut real substance just to hit a length target,
   and never pad a simple story with restated filler to look thorough —
   match the length to how much there actually is to say.
5. Plain language, no marketing tone, regardless of length.

Good version of the same story used in the bad example above:

> A cryptography puzzle from 2005 that nobody had cracked finally fell to
> GPT-6 Astra — notable less as a novelty and more as a data point on how
> far model reasoning has moved past what dedicated human cryptanalysts
> could do with two decades to work on it.

If you notice yourself running low on time or context partway through the
list, it is better to feature fewer stories with real summaries than to
hit `articles_per_digest` with filler — cutting the count is fine, cutting
corners on the summaries is not.

9. Update `data/seen.json`: append today's picks (title, url, source,
   date), then remove entries older than `dedup_lookback_days`.

10. Commit `docs/index.html`, `docs/archive/` (everything changed by step
    7), and `data/seen.json` — not `data/raw_latest.json` (gitignored,
    regenerated every run). Commit message: `digest: YYYY-MM-DD`. Push to
    `main`. If that push is rejected and you land on a `claude/`-prefixed
    branch instead, that's fine — do nothing further about it.
    `.github/workflows/auto-merge-routine.yml` opens a PR from that branch
    and merges it automatically once CI passes; don't open the PR
    yourself, don't try to force the push, don't wait around for the
    merge. Either way, GitHub Pages redeploys automatically once the
    commit reaches `main`.

11. Final summary, one short line: sources ok/failed, articles fetched,
    articles featured. Nothing else.

## Scope

Only ever read/write: `config/*.json`, `scripts/*.py`, `data/seen.json`,
`data/raw_latest.json`, `docs/index.html`, `docs/archive/*.html`. Never
touch `.github/workflows/*.yml` or GitHub Pages settings.

## If a source breaks

Check `errors` in `data/raw_latest.json`. One quick fix attempt only — a
stale `feed_url` in `config/sources.json`, or an obvious bug in
`scripts/fetch_github_trending.py` / `scripts/fetch_tldr.py` (the two HTML
scrapers, most likely to break if a site's markup changes). If the cause
isn't obvious immediately, skip it and mention it in the step 11 summary —
don't spend the run debugging it.
