# Setup

## 1. Repo

Done — [shubhamcodess/everything-tech-newsletter](https://github.com/shubhamcodess/everything-tech-newsletter).

## 2. Enable GitHub Pages

In the repo: **Settings → Pages → Build and deployment → Source: Deploy
from a branch → Branch: `main`, folder: `/docs` → Save.** GitHub's
branch-based Pages deploy only supports the repo root or `/docs` — no
arbitrary folder — which is exactly why this repo publishes from
`docs/`. No GitHub Action is involved in deployment; GitHub redeploys
`/docs` automatically on every push to `main`.

Your digest will be live at `https://<username>.github.io/<repo>/` once
the first commit touching `docs/` lands.

## 3. Enable auto-merge (needed for the routine's branch → main handoff)

A Claude Code routine pushes its commit to a `claude/`-prefixed branch
instead of `main` whenever a direct push to `main` isn't accepted — which
happens whenever `main` has any branch protection at all. When that
happens, the routine opens its own PR (see `CLAUDE.md` step 10) — it can,
because it's authenticated as your real GitHub account through the
routine's GitHub proxy, unlike GitHub Actions' own token, which GitHub
deliberately blocks from creating PRs by default.
`.github/workflows/auto-merge-routine.yml` then just merges that PR once
CI passes. Only one setting is needed for the merge step to work:

**Settings → General → Pull Requests → check "Allow auto-merge".**

Without it, `gh pr merge --auto` in the workflow fails and the PR sits
open until merged by hand.

(Earlier versions of this workflow had the *workflow* open the PR, which
also needed Settings → Actions → General → "Allow GitHub Actions to
create and approve pull requests" — a separate, easy-to-miss gate. Moving
PR creation to the routine itself avoids needing that setting at all.)

## 4. Connect the repo to Claude Code

At [claude.ai/code](https://claude.ai/code), make sure GitHub access is
connected (routines need this to clone/push).

## 5. Create the routine

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

## 6. First run

Open the routine and click **Run now**. Open the run's session to watch it
work; confirm at the end that `docs/index.html`, `docs/archive/`, and
`data/seen.json` were committed, and that the run summary reports source
successes and the article count.

Then check where the commit landed:
- **Directly on `main`** — check the Pages URL; it should already be live.
- **On a `claude/…` branch instead** — check the repo's **Pull requests**
  tab. The routine should have opened one itself as its last action (see
  `CLAUDE.md` step 10), and `auto-merge-routine.yml` should show up in
  its checks within a few seconds of that, enabling auto-merge (visible
  as "Auto-merge enabled" in the PR). It merges itself once `ci.yml`
  passes — typically well under a minute — and the branch is deleted
  after. Check the Pages URL once it merges. If no PR appeared at all,
  re-read the run's transcript for a `gh pr create` error near the end.

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
  step 8 if the structure changes) — the pipeline logic doesn't need to
  change.
- **Archive**: past digests live at `docs/archive/`, capped at the last 7
  days automatically (`CLAUDE.md` step 7 prunes the oldest once there are
  more than 7) — nothing to maintain by hand.
- **Branch → main handoff**: if the routine ever lands on a `claude/…`
  branch instead of `main` (see step 6), that's expected, not an error —
  `auto-merge-routine.yml` handles it every time without you touching
  anything, as long as "Allow auto-merge" (step 3) stays enabled.
