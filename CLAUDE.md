# Tech Newsletter — routine instructions

This repo generates a daily personalized tech-news digest and publishes it via
GitHub Pages from `docs/index.html`. This file is read automatically by the
Claude Code cloud routine on every run — follow the pipeline below exactly.

## Pipeline, every run

1. **Install deps if needed.** `pip install -r scripts/requirements.txt`.

2. **Fetch.** Run `python scripts/fetch_all.py`. This writes
   `data/raw_latest.json`: every source's articles, normalized, plus a log of
   which sources succeeded/failed. A source failing does not stop the run —
   note failures in your final summary but keep going with what you got.

3. **Load config.** Read `config/interests.json` (the topic boundary — the
   user edits this any time), `config/settings.json`
   (`articles_per_digest`, `fetch_lookback_hours`, `dedup_lookback_days`), and
   `data/seen.json` (stories already featured in the last
   `dedup_lookback_days` days — don't feature the same story, or an obvious
   re-report of it by another outlet, again).

4. **Filter to the interest boundary.** Drop articles that don't reasonably
   match any topic in `config/interests.json`. Also drop anything published
   outside `fetch_lookback_hours`.

5. **Cluster duplicates.** Multiple sources often cover the same underlying
   story. Group near-duplicate articles (similar title/topic, same
   event) into one story. Prefer the best-written/highest-trust source as the
   representative; you may note which other outlets also covered it.

6. **Judge and rank.** You are the ranker — there is no scoring formula. Pick
   the `articles_per_digest` best stories using your own judgment of:
   genuine importance/impact, quality and depth (not just clickbait), and
   topical diversity (don't let one topic, like "another LLM release,"
   dominate the whole digest even if it dominates the raw feed — spread
   across the interest list where the day's news allows it). Cross-check
   against `data/seen.json` and skip stories already featured recently.

7. **Write the digest.** Compose `docs/index.html`, following the structure
   and styling in `templates/digest.html.template` (dark-blue neubrutalist
   theme: squarish cards, two-tone hard box-shadows, neon cyan/pink/green
   accents, JetBrains Mono). For each story, write your own brief, engaging
   summary in your own words — don't just paste the source's description.
   Order/group stories however reads best (by topic, by importance — your
   call). Keep the header's brand block (the EverythingTech name, pixel
   chip icon, tagline, and the "view source" link) and the footer block
   (the "curated_by Shubham Prakash" signoff and GitHub/LinkedIn icon
   buttons) exactly as they are in the template — both are fixed content,
   not something to regenerate or drop. Only the date in the header and
   the stories in between change day to day.

8. **Update memory.** Append the day's featured stories (id, title, url,
   source, date) to `data/seen.json`, and prune entries older than
   `dedup_lookback_days`.

9. **Commit and push.** Commit `docs/index.html` and `data/seen.json` (do
   not commit `data/raw_latest.json` — it's regenerated every run and
   gitignored) with a short message like `digest: 2026-09-24`. Push directly
   to `main`. GitHub Pages redeploys automatically on push.

10. **Report.** In your final summary for the run, state: how many sources
    succeeded/failed (and which failed, if any), how many articles were
    fetched, and how many made the final digest.

## Maintenance

- If a source fails repeatedly (check `errors` in `data/raw_latest.json`
  across runs), the site likely changed its feed URL or HTML structure. You
  have full repo access — inspect the source and fix `config/sources.json`
  or the relevant `scripts/fetch_*.py`, then commit the fix as part of the
  same run.
- `scripts/fetch_github_trending.py` and `scripts/fetch_tldr.py` both scrape
  HTML (no official API for either) and are the most likely to break if
  those sites change their markup — check these first if they start
  returning 0 items. `fetch_tldr.py` in particular relies on a specific
  `<article class="mt-3">...` shape; an unpublished day's URL redirects to
  an unrelated page with differently-shaped `<article>` tags, which the
  fetcher already guards against by only accepting a day once the real
  story pattern matches — if TLDR redesigns the page, that guard is where
  to start fixing it.
- A few sources in `config/sources.json` are marked `"verify_url": true`
  (mostly AI-lab company blogs, whose feed URLs move around). If one fails,
  search for that company's current blog RSS URL, update the config, and
  note the fix in your run summary.
