# Setup

## 1. Repo

Done — [shubhamcodess/everything-tech-newsletter](https://github.com/shubhamcodess/everything-tech-newsletter).

## 2. Enable GitHub Pages

In the repo: **Settings → Pages → Build and deployment → Source: Deploy from
a branch → Branch: `main`, folder: `/docs` → Save.**

Your digest will be live at `https://<username>.github.io/<repo>/` once the
first commit lands.

## 3. Connect the repo to Claude Code

At [claude.ai/code](https://claude.ai/code), make sure GitHub access is
connected (routines need this to clone/push).

## 4. Create the routine

At [claude.ai/code/routines/new](https://claude.ai/code/routines/new):

- **Prompt** — paste the text from `ROUTINE_PROMPT.md`.
- **Model** — Haiku is the intended model for this routine. `CLAUDE.md`'s
  steps are written as a concrete, mostly-deterministic checklist (explicit
  filter/diversity rules instead of open-ended "use your judgment" prose)
  specifically so a smaller model can follow them reliably without drifting
  or overspending tokens reasoning about ambiguous steps. If digest quality
  degrades on Haiku, the first thing to revisit is step 6's ranking rule in
  `CLAUDE.md`, not the model choice.
- **Repository** — select this repo.
- **Environment** — open the environment editor and set **Network access** to
  **Custom**, then paste the domain list below into **Allowed domains**
  (check "Also include default list of common package managers" so pip/apt
  installs in the setup step still work). This is required — none of the
  sources below are in the Trusted default allowlist.
- **Trigger** — Schedule, recurring, daily, your preferred time (e.g. 6:00 AM
  IST — times are entered in your local zone).
- **Connectors** — none needed; leave default or remove all.

Click **Create**.

### Custom allowed domains

```
hn.algolia.com
www.reddit.com
reddit.com
export.arxiv.org
dev.to
github.com
techcrunch.com
www.theverge.com
feeds.arstechnica.com
arstechnica.com
venturebeat.com
www.engadget.com
www.zdnet.com
www.wired.com
www.techradar.com
rss.slashdot.org
thenewstack.io
feeds.dzone.com
www.phoronix.com
feed.infoq.com
www.technologyreview.com
www.smashingmagazine.com
www.freecodecamp.org
changelog.com
stackoverflow.blog
github.blog
hacks.mozilla.org
aws.amazon.com
kubernetes.io
developers.googleblog.com
www.microsoft.com
blogs.nvidia.com
openai.com
www.anthropic.com
deepmind.google
ai.meta.com
www.ycombinator.com
simonwillison.net
www.kdnuggets.com
towardsdatascience.com
bair.berkeley.edu
lobste.rs
tldr.tech
```

## 5. First run

Open the routine and click **Run now**. Open the run's session to watch it
work; confirm at the end that `docs/index.html` and `data/seen.json` were
committed and pushed, and that the run summary reports source successes and
the article count. Then check the Pages URL updated.

A few sources are marked `"verify_url": true` in `config/sources.json` —
watch the first run's source-failure log for those in particular; if any
fail, the routine is instructed (via `CLAUDE.md`) to try fixing the feed URL
itself and note it in the summary.

## Ongoing

- **Change what topics show up**: edit `config/interests.json`, commit, push.
  No routine edit needed.
- **Change how many stories per day**: edit `articles_per_digest` in
  `config/settings.json`.
- **Add/remove a source**: edit `config/sources.json`. If it's RSS, just add
  an entry with `"type": "rss"` and a `feed_url` — no new code needed.
- **Change the visual design**: once you have a specific style in mind,
  replace `templates/digest.html.template` (and mention it in `CLAUDE.md`'s
  step 7 if the structure changes) — the pipeline logic doesn't need to
  change.
