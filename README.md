<div align="center">

# ⚡ EverythingTech
### all at once.

<a href="https://shubhamcodess.github.io/everything-tech-newsletter/"><img src="https://img.shields.io/badge/live%20site-visit-bef264?style=for-the-badge&labelColor=16181f" alt="Live site"></a>
<a href="https://github.com/shubhamcodess/everything-tech-newsletter/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/shubhamcodess/everything-tech-newsletter/ci.yml?branch=main&style=for-the-badge&label=CI&labelColor=16181f" alt="CI"></a>
<a href="https://github.com/shubhamcodess/everything-tech-newsletter/actions/workflows/auto-merge-routine.yml"><img src="https://img.shields.io/github/actions/workflow/status/shubhamcodess/everything-tech-newsletter/auto-merge-routine.yml?style=for-the-badge&label=auto-merge&labelColor=16181f" alt="Auto-merge"></a>
<a href="https://github.com/shubhamcodess/everything-tech-newsletter/deployments"><img src="https://img.shields.io/github/deployments/shubhamcodess/everything-tech-newsletter/github-pages?style=for-the-badge&label=pages&labelColor=16181f" alt="GitHub Pages deploy"></a>
<br>
<a href="https://github.com/shubhamcodess/everything-tech-newsletter/commits/main"><img src="https://img.shields.io/github/last-commit/shubhamcodess/everything-tech-newsletter?style=flat-square&labelColor=16181f&color=5eead4" alt="Last commit"></a>
<a href="https://github.com/shubhamcodess/everything-tech-newsletter/stargazers"><img src="https://img.shields.io/github/stars/shubhamcodess/everything-tech-newsletter?style=flat-square&labelColor=16181f&color=fbbf24" alt="Stars"></a>
<a href="https://github.com/shubhamcodess/everything-tech-newsletter/fork"><img src="https://img.shields.io/github/forks/shubhamcodess/everything-tech-newsletter?style=flat-square&labelColor=16181f&color=7aa2ff" alt="Forks"></a>
<a href="https://code.claude.com/docs/en/routines"><img src="https://img.shields.io/badge/built%20with-Claude%20Code-ff6ec7?style=flat-square&labelColor=16181f" alt="Built with Claude Code"></a>
<img src="https://img.shields.io/badge/sources-47-bef264?style=flat-square&labelColor=16181f" alt="47 sources">
<img src="https://img.shields.io/badge/API%20keys-none-5eead4?style=flat-square&labelColor=16181f" alt="No API keys">

<img src="assets/preview.png" alt="EverythingTech — a daily tech newspaper" width="760">

</div>

A daily tech newspaper with no human editor. Python pulls fresh articles from
47 free sources, groups duplicate coverage, and fetches the full text of the
stories that matter. A scheduled [Claude Code routine](https://code.claude.com/docs/en/routines)
picks, ranks, and writes each one up from the actual article: a headline, a
dek, a few real paragraphs, and takeaways. GitHub Pages serves it. No server,
no database, no API key.

## How it works

```
┌──────────────────────────────────────────────────────┐
│                      47 sources                      │
│              RSS · APIs · HTML scrapes               │
└──────────────────────────────────────────────────────┘
                            │  fetch_all.py
                            ▼
┌──────────────────────────────────────────────────────┐
│  build_candidates.py -> data/candidates.md (~14K tk) │
│  drop stale / seen / junk · cluster same-story news  │
└──────────────────────────────────────────────────────┘
                            │  routine picks + ranks
                            ▼
┌──────────────────────────────────────────────────────┐
│  fetch_articles.py -> data/articles.md   (~19K tk)   │
│  full article text, fallback to other outlets        │
└──────────────────────────────────────────────────────┘
                            │  routine writes data/draft.md
                            ▼
┌──────────────────────────────────────────────────────┐
│  publish_edition.py                                  │
│  validate prose · fill links/authors/images          │
│  -> editions/<date>/edition.md  (the durable record) │
└──────────────────────────────────────────────────────┘
                            │  build_site.py
                            ▼
┌──────────────────────────────────────────────────────┐
│  docs/data/*.json + feed.xml  ──►  one template      │
│  (docs/assets) renders today and every archive date  │
└──────────────────────────────────────────────────────┘
                            │  commit + push (or PR -> auto-merge)
                            ▼
┌──────────────────────────────────────────────────────┐
│          GitHub Pages  (serves main:/docs)           │
└──────────────────────────────────────────────────────┘
```

Scripts do everything mechanical; the LLM only picks, ranks, and writes. It
never writes HTML: each edition is a Markdown file, and one client-side
template draws every date from it. Change the design once and every edition,
today's and archived, changes with it. Its instructions live in
[`CLAUDE.md`](CLAUDE.md), versioned like any other code.

- **Written from the source.** Full article text, not a feed blurb, and a validator rejects copied sentences, filler, and cut-off prose.
- **Deduped.** One story covered by five outlets shows once, crediting all five.
- **Ranked.** The lead, must-reads, and the wire, plus a 60-second Brief.
- **Readable.** Night and day themes, topic and signal filters, keyboard shortcuts (`?`), and a live ticker.
- **Portable.** Every edition also comes as [Markdown](https://shubhamcodess.github.io/everything-tech-newsletter/latest.md), [JSON](https://shubhamcodess.github.io/everything-tech-newsletter/latest.json) and [RSS](https://shubhamcodess.github.io/everything-tech-newsletter/feed.xml).
- **Self-pruning archive.** The last 7 days; older editions stay in git history.

## Fork it and make it yours

You'll need a Claude plan that includes [routines](https://code.claude.com/docs/en/routines)
(Pro, Max, Team, or Enterprise) and a GitHub account.

**1. Fork and reset.** Fork this repo, clone it, then start clean:

```bash
./scripts/reset_for_fork.sh    # empty archive, no remembered stories
```

**2. Make it yours.** Name, tagline, curator links and colours live in [`config/site.json`](config/site.json).
Topics go in [`config/interests.json`](config/interests.json), and edition size in [`config/settings.json`](config/settings.json). Then rebuild the site data:

```bash
python scripts/build_site.py
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
| Model | Sonnet for the best writing; Haiku works |
| Repository | your fork |
| Environment | **Network access → Full** (it reads articles on any site), or **Custom** with the list in [`SETUP.md`](SETUP.md#custom-allowed-domains) ([why](https://code.claude.com/docs/en/cloud-environments#network-access)) |
| Trigger | Schedule → Daily → your time |
| Connectors | none |

**6. Run it.** Click **Run now**, watch the session, then check your Pages URL. Details and troubleshooting: [`SETUP.md`](SETUP.md).

## Configuration

Edit, commit, push. The next run picks it up.

| File | Controls |
|---|---|
| [`config/site.json`](config/site.json) | Render config: name, tagline, curator links, theme colours, features (run `build_site.py` after) |
| [`config/interests.json`](config/interests.json) | Topics, and what each covers |
| [`config/settings.json`](config/settings.json) | Stories per edition, must-read cap, lookback, token budgets, archive days |
| [`config/sources.json`](config/sources.json) | Add, remove, or disable sources; RSS needs only a `feed_url` |
| [`docs/assets/`](docs/assets) | The one template: every edition renders through it |
| [`CLAUDE.md`](CLAUDE.md) | The routine's step-by-step pipeline and writing rules |

## Project structure

```
.
├── CLAUDE.md                       # the routine's pipeline + writing rules
├── ROUTINE_PROMPT.md               # the prompt pasted into the routine
├── SETUP.md                        # one-time setup + troubleshooting
├── .github/workflows/
│   ├── ci.yml                      # validates config, fetchers, editions, site data
│   └── auto-merge-routine.yml      # merges the routine's claude/* PRs once CI passes
├── config/
│   ├── site.json                   # render config for the whole site
│   ├── interests.json              # topics
│   ├── settings.json               # edition size, budgets, windows
│   └── sources.json                # the 47-source registry
├── scripts/
│   ├── fetch_all.py                # runs every fetcher -> data/raw_latest.json
│   ├── fetch_*.py                  # RSS, HN, Reddit, arXiv, Dev.to, GitHub Trending, TLDR
│   ├── build_candidates.py         # filter + cluster -> data/candidates.md
│   ├── fetch_articles.py           # full text of the picks -> data/articles.md
│   ├── publish_edition.py          # validate draft -> editions/<date>/
│   ├── build_site.py               # editions -> docs/data, feed.xml, latest.*
│   ├── edition_md.py               # the edition Markdown format
│   ├── edition_schema.py           # prose + structure validation
│   ├── validate_editions.py        # CI check
│   └── reset_for_fork.sh           # clean slate for a fresh fork
├── editions/
│   └── YYYY-MM-DD/
│       ├── edition.md              # the day's paper, self-contained
│       ├── sources.md              # full text the stories were written from
│       └── candidates.md           # everything that was considered
├── data/
│   └── seen.json                   # recently featured stories (no repeats)
├── assets/
│   └── preview.png                 # README banner
└── docs/                           # GitHub Pages source (branch deploy)
    ├── index.html                  # app shell
    ├── assets/                     # app.css + app.js: the one template
    ├── data/                       # site.json, index.json, <date>.json
    ├── feed.xml                    # RSS
    └── latest.md / latest.json     # today's edition, machine-readable
```

---

<div align="center">

**$** curated_by **Shubham Prakash**

<a href="https://github.com/shubhamcodess"><img src="https://img.shields.io/badge/-shubhamcodess-16181f?style=for-the-badge&logo=github&logoColor=5eead4" alt="GitHub"></a>
<a href="https://www.linkedin.com/in/shubham-prakash-dev/"><img src="https://img.shields.io/badge/-shubham--prakash--dev-16181f?style=for-the-badge&logo=linkedin&logoColor=7aa2ff" alt="LinkedIn"></a>

</div>
