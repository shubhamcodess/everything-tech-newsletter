<div align="center">

# ⚡ EverythingTech
### all at once.

<a href="https://shubhamcodess.github.io/everything-tech-newsletter/"><img src="https://img.shields.io/badge/live%20site-visit-4dff9e?style=for-the-badge&labelColor=0a0e14" alt="Live site"></a>
<a href="https://github.com/shubhamcodess/everything-tech-newsletter/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/shubhamcodess/everything-tech-newsletter/ci.yml?branch=main&style=for-the-badge&label=CI&labelColor=0a0e14" alt="CI"></a>
<a href="https://github.com/shubhamcodess/everything-tech-newsletter/actions/workflows/auto-merge-routine.yml"><img src="https://img.shields.io/github/actions/workflow/status/shubhamcodess/everything-tech-newsletter/auto-merge-routine.yml?style=for-the-badge&label=auto-merge&labelColor=0a0e14" alt="Auto-merge"></a>
<a href="https://github.com/shubhamcodess/everything-tech-newsletter/deployments"><img src="https://img.shields.io/github/deployments/shubhamcodess/everything-tech-newsletter/github-pages?style=for-the-badge&label=pages&labelColor=0a0e14" alt="GitHub Pages deploy"></a>
<br>
<a href="https://github.com/shubhamcodess/everything-tech-newsletter/commits/main"><img src="https://img.shields.io/github/last-commit/shubhamcodess/everything-tech-newsletter?style=flat-square&labelColor=0a0e14&color=39f6e2" alt="Last commit"></a>
<a href="https://github.com/shubhamcodess/everything-tech-newsletter/stargazers"><img src="https://img.shields.io/github/stars/shubhamcodess/everything-tech-newsletter?style=flat-square&labelColor=0a0e14&color=f0e14d" alt="Stars"></a>
<a href="https://github.com/shubhamcodess/everything-tech-newsletter/fork"><img src="https://img.shields.io/github/forks/shubhamcodess/everything-tech-newsletter?style=flat-square&labelColor=0a0e14&color=4d8dff" alt="Forks"></a>
<a href="https://code.claude.com/docs/en/routines"><img src="https://img.shields.io/badge/built%20with-Claude%20Code-ff3ec8?style=flat-square&labelColor=0a0e14" alt="Built with Claude Code"></a>
<img src="https://img.shields.io/badge/sources-47-4dff9e?style=flat-square&labelColor=0a0e14" alt="47 sources">
<img src="https://img.shields.io/badge/API%20keys-none-39f6e2?style=flat-square&labelColor=0a0e14" alt="No API keys">

<img src="assets/preview.png" alt="EverythingTech — a daily AI-curated tech digest" width="600">

</div>

A daily tech newsletter with no human editor. Python pulls fresh articles from
47 free sources; a scheduled [Claude Code routine](https://code.claude.com/docs/en/routines)
filters, dedupes, ranks, and writes each story up; GitHub Pages serves the result.
No server, no database, no API key.

## How it works

```
┌──────────────────────────────────────────────────────┐
│                      47 sources                      │
│              RSS · APIs · HTML scrapes               │
└──────────────────────────────────────────────────────┘
                            │  scripts/fetch_all.py
                            ▼
┌──────────────────────────────────────────────────────┐
│                 data/raw_latest.json                 │
│           (normalized, unjudged articles)            │
└──────────────────────────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────┐
│        Claude Code routine  (reads CLAUDE.md)        │
│                                                      │
│  1. filter   -> config/interests.json                │
│  2. cluster  -> same-story coverage                  │
│  3. dedupe   -> data/seen.json                       │
│  4. rank     -> judgment + diversity cap             │
│  5. archive  -> docs/archive/ (7-day cap)            │
└──────────────────────────────────────────────────────┘
                            │  writes, using templates/digest.html.template
                            ▼
┌──────────────────────────────────────────────────────┐
│                   docs/index.html                    │
└──────────────────────────────────────────────────────┘
                            │  git commit + push (or PR -> auto-merge)
                            ▼
┌──────────────────────────────────────────────────────┐
│          GitHub Pages  (auto-deploys /docs)          │
└──────────────────────────────────────────────────────┘
```

Fetching is plain code, so nothing upstream of the LLM can be hallucinated. The
LLM only does what needs judgment. Its instructions live in [`CLAUDE.md`](CLAUDE.md),
versioned like any other code.

- **Deduped** — one story covered by five outlets shows once, crediting all five
- **No repeats** — `data/seen.json` remembers recent picks for a week
- **25 stories, 10 up front** — the rest sit behind a load-more button
- **Self-pruning archive** — the last 7 days, oldest deleted automatically
- **Guarded by CI** — config, fetchers, and the digest itself are validated before anything merges

## Fork it and make it yours

You'll need a Claude plan that includes [routines](https://code.claude.com/docs/en/routines)
(Pro, Max, Team, or Enterprise) and a GitHub account.

**1. Fork and reset.** Fork this repo, clone it, then start clean:

```bash
./scripts/reset_for_fork.sh    # placeholder page, empty archive, no remembered stories
```

**2. Make it yours.** Edit [`config/interests.json`](config/interests.json) for the topics you care about,
and [`config/settings.json`](config/settings.json) for digest size. Then swap my name and links for yours:

```bash
grep -rIl "shubhamcodess\|Shubham Prakash" --exclude-dir=.git .   # every file to update
```

**3. Turn on GitHub Pages.** Repo **Settings → Pages → Deploy from a branch → `main` / `/docs`**.
([Pages docs](https://docs.github.com/en/pages))

**4. Two repo settings for the auto-merge handoff.** The routine can't always push straight to a protected `main`,
so it opens a PR and [`auto-merge-routine.yml`](.github/workflows/auto-merge-routine.yml) merges it.
- **Settings → General → Pull Requests → Allow auto-merge**
- **Settings → Branches → add a rule for `main` → Require status checks → `validate`**
  ([protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches))

**5. Create the routine** at [claude.ai/code/routines/new](https://claude.ai/code/routines/new):

| Field | Value |
|---|---|
| Prompt | the text in [`ROUTINE_PROMPT.md`](ROUTINE_PROMPT.md) |
| Model | Haiku or Sonnet — `CLAUDE.md` is written to work on smaller models |
| Repository | your fork |
| Environment | **Network access → Custom**, paste the domain list from [`SETUP.md`](SETUP.md#custom-allowed-domains) ([why](https://code.claude.com/docs/en/cloud-environments#network-access)) |
| Trigger | Schedule → Daily → your time |
| Connectors | none |

**6. Run it.** Click **Run now**, watch the session, then check your Pages URL. Details and troubleshooting: [`SETUP.md`](SETUP.md).

## Configuration

Edit, commit, push — the next run picks it up. No code changes.

| File | Controls |
|---|---|
| [`config/interests.json`](config/interests.json) | Topic whitelist — anything outside it is filtered out |
| [`config/settings.json`](config/settings.json) | Digest size, lookback windows, items per source |
| [`config/sources.json`](config/sources.json) | Add, remove, or disable sources — RSS needs only a `feed_url` |
| [`templates/`](templates) | Page design — digest, archive, and placeholder |
| [`CLAUDE.md`](CLAUDE.md) | The routine's step-by-step pipeline |

## Project structure

```
.
├── CLAUDE.md                       # the routine's pipeline, step by step
├── ROUTINE_PROMPT.md               # the prompt pasted into the routine
├── SETUP.md                        # one-time setup + troubleshooting
├── .github/workflows/
│   ├── ci.yml                      # validates config, fetchers, digest content
│   └── auto-merge-routine.yml      # merges the routine's claude/* PRs once CI passes
├── config/
│   ├── interests.json              # topic whitelist
│   ├── settings.json               # digest size, lookback windows, items per source
│   └── sources.json                # the 47-source registry
├── scripts/
│   ├── fetch_all.py                # orchestrator
│   ├── fetch_rss.py                # generic RSS/Atom fetcher
│   ├── fetch_hn.py                 # Hacker News (Algolia API)
│   ├── fetch_reddit.py             # Reddit (public .json endpoints)
│   ├── fetch_arxiv.py              # arXiv (Atom API)
│   ├── fetch_devto.py              # Dev.to (public API)
│   ├── fetch_github_trending.py    # GitHub Trending (HTML scrape)
│   ├── fetch_tldr.py               # TLDR editions (HTML scrape)
│   └── reset_for_fork.sh           # clean slate for a fresh fork
├── templates/
│   ├── digest.html.template        # the digest's structure + styling
│   ├── archive.html.template       # the archive listing page
│   └── placeholder.html            # "awaiting first run" page
├── data/
│   └── seen.json                   # memory of recently-featured stories
├── assets/
│   └── preview.png                 # README banner
└── docs/                           # GitHub Pages source (branch deploy)
    ├── index.html                  # today's digest
    ├── sample-output.html          # hand-assembled design sample (not live)
    └── archive/
        ├── index.html              # past-digests list, capped at 7 days
        └── YYYY-MM-DD.html         # one snapshot per archived day
```

---

<div align="center">

**$** curated_by **Shubham Prakash**

<a href="https://github.com/shubhamcodess"><img src="https://img.shields.io/badge/-shubhamcodess-0a0e14?style=for-the-badge&logo=github&logoColor=39f6e2" alt="GitHub"></a>
<a href="https://www.linkedin.com/in/shubham-prakash-dev/"><img src="https://img.shields.io/badge/-shubham--prakash--dev-0a0e14?style=for-the-badge&logo=linkedin&logoColor=4d8dff" alt="LinkedIn"></a>

</div>
