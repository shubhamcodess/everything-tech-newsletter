"""Builds the site's data from the edition records. No network, no LLM,
safe to run any time:  python scripts/build_site.py

Reads  editions/<date>/edition.md  (one per day, newest archive_days+1 kept)
       config/site.json            (the rendering config: branding, palette, features)
Writes docs/data/<date>.json       what the page renders, one per edition
       docs/data/index.json        the edition manifest (drives archive + prev/next)
       docs/data/site.json         the rendering config, as the page reads it
       docs/latest.md, docs/latest.json, docs/feed.xml

The page itself (docs/index.html + docs/assets/) is a single template that
renders whichever date is requested, so today's edition and every archived
one always share the current design -- nothing per-day is ever baked into HTML.
"""
import glob
import json
import os
import shutil
import sys
from datetime import datetime
from email.utils import format_datetime
from xml.sax.saxutils import escape

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import edition_md  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EDITIONS = os.path.join(ROOT, "editions")
DOCS = os.path.join(ROOT, "docs")
DATA = os.path.join(DOCS, "data")


def load(path):
    with open(path) as f:
        return json.load(f)


def edition_dates():
    return sorted((os.path.basename(os.path.dirname(p)) for p in glob.glob(os.path.join(EDITIONS, "20*", "edition.md"))),
                  reverse=True)


def read_manifest():
    """Edition count + dates currently on disk (used by publish_edition.py)."""
    editions = []
    for date in edition_dates():
        front, _ = edition_md._split_front_matter(open(os.path.join(EDITIONS, date, "edition.md")).read())
        editions.append({"date": date, "edition": int(front.get("edition", 0))})
    return {"count": max((e["edition"] for e in editions), default=0), "editions": editions}


def render_rss(edition, site):
    url = site.get("url", "").rstrip("/") + "/"
    pub = format_datetime(datetime.fromisoformat(edition["generated_at"]))
    items = []
    for rank, story in enumerate(edition["stories"], start=1):
        body = "".join(f"<p>{escape(p)}</p>" for p in [story["dek"], *story["body"]])
        items.append(
            f"<item><title>{escape(story['headline'])}</title><link>{escape(story['url'])}</link>"
            f"<guid isPermaLink=\"false\">{edition['date']}-{rank}</guid><category>{escape(story['topic'])}</category>"
            f"<pubDate>{pub}</pubDate><description>{escape(body)}</description></item>"
        )
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel>'
            f"<title>{escape(site.get('name', ''))}</title><link>{escape(url)}</link>"
            f"<description>{escape(site.get('description', ''))}</description>"
            f"<lastBuildDate>{pub}</lastBuildDate>{''.join(items)}</channel></rss>\n")


SIGNAL_META = {"must-read": ("Must read", "Must reads"),
               "recommended": ("Recommended", "Recommended"),
               "notable": ("Notable", "Quick hits")}


def render_markdown(edition, site):
    """Clean, professional Markdown of one edition. Pure GFM: no emoji, no SVG,
    no inline HTML. The Brief and Takeaways render as GitHub alert callouts and
    degrade to blockquotes elsewhere."""
    stories = edition["stories"]
    stats = edition.get("stats", {})
    day = datetime.fromisoformat(edition["date"])
    pretty = f"{day:%A}, {day.day} {day:%B %Y}"
    url = site.get("url", "")
    name = site.get("name", "")
    tagline = site.get("tagline", "")
    must_count = sum(1 for s in stories if s["signal"] == "must-read")

    def cell(text):
        # Keep table cells tidy: escape pipes, flatten whitespace.
        return " ".join(str(text).replace("|", "\\|").split())

    out = [f"# {name}: No. {edition['edition']}", ""]
    if tagline:
        out += [f"*{tagline}*", ""]
    meta_bits = [pretty, f"{len(stories)} stories",
                 f"{must_count} must-read{'s' if must_count != 1 else ''}"]
    if "sources_ok" in stats and "sources_total" in stats:
        meta_bits.append(f"{stats['sources_ok']}/{stats['sources_total']} sources read")
    out += [" \u00b7 ".join(meta_bits), "", "---", ""]

    if edition.get("brief"):
        out += ["## The Brief", "",
                "> [!NOTE]",
                "> **The day in a few lines.**",
                ">"]
        out += [f"> - {b}" for b in edition["brief"]]
        out += ["", "---", ""]

    out += ["## In this edition", "",
            "| # | Signal | Topic | Read | Story |",
            "|---:|:---|:---|---:|:---|"]
    for rank, st in enumerate(stories, start=1):
        label, _ = SIGNAL_META.get(st["signal"], (st["signal"].title(), ""))
        read_cell = f"{st['read_minutes']} min" if st.get("read_minutes") else "n/a"
        out.append(f"| {rank} | {cell(label)} | {cell(st['topic'])} | {read_cell} | {cell(st['headline'])} |")
    out += ["", "---", ""]

    for signal in ("must-read", "recommended", "notable"):
        group = [(r, st) for r, st in enumerate(stories, start=1) if st["signal"] == signal]
        if not group:
            continue
        label, title = SIGNAL_META[signal]
        out += [f"## {title}", ""]
        for rank, st in group:
            out += [f"### {rank}. {st['headline']}", ""]
            meta = [f"**{label}**", st["topic"]]
            if st.get("read_minutes"):
                meta.append(f"{st['read_minutes']} min read")
            out += [" \u00b7 ".join(meta), ""]
            out += [f"> {st['dek']}", ""]
            for para in st["body"]:
                out += [para, ""]
            if st.get("takeaways"):
                out += ["> [!TIP]", "> **Takeaways**", ">"]
                out += [f"> - {t}" for t in st["takeaways"]]
                out.append("")
            source_links = []
            if st.get("url"):
                source_links.append(f"[Read the original]({st['url']})")
            if st.get("discuss_url"):
                bits = []
                if st.get("points"):
                    bits.append(f"{st['points']} points")
                if st.get("comments"):
                    bits.append(f"{st['comments']} comments")
                detail = f" ({', '.join(bits)})" if bits else ""
                source_links.append(
                    f"[Discuss on {st.get('discuss_via', 'the web')}]({st['discuss_url']}){detail}")
            if source_links:
                out += [" \u00b7 ".join(source_links), ""]
            others = [f"[{x['name']}]({x['url']})" for x in st.get("sources", []) if x["url"] != st.get("url")]
            if others:
                out += [f"Also covered by: {', '.join(others)}", ""]
            out += ["---", ""]

    out += ["## Take it with you", "",
            f"- [Read it on the web]({url})",
            f"- [RSS feed]({url}feed.xml)",
            f"- [Edition as JSON]({url}latest.json)",
            f"- [Raw source]({site.get('repo', '')}/blob/main/editions/{edition['date']}/edition.md)",
            "", "---", ""]
    curator = site.get("curator", {})
    cname = curator.get("name", "")
    out += ["## Curated by " + cname, "",
            f"Pulled from {stats.get('sources_total', 'many')} sources overnight, deduplicated, "
            f"{stats.get('full_text', 'many')} read in full, written up in plain words.", ""]
    links = [f"[{label}]({curator[key]})" for key, label in (("github", "GitHub"), ("linkedin", "LinkedIn")) if curator.get(key)]
    if links:
        out += [f"Find {cname} on " + " and ".join(links) + ".", ""]
    # No em dashes anywhere, including text lifted from the stories.
    return "\n".join(out).replace(" \u2014 ", ", ").replace("\u2014", " - ")


def main():
    settings = load(os.path.join(ROOT, "config", "settings.json"))
    site = load(os.path.join(ROOT, "config", "site.json"))
    topic_order = [t["label"] for t in load(os.path.join(ROOT, "config", "interests.json"))["topics"]]
    keep = settings.get("archive_days", 7) + 1

    dates = edition_dates()
    for old in dates[keep:]:
        shutil.rmtree(os.path.join(EDITIONS, old))
        print(f"pruned editions/{old} (older than archive_days)")
    dates = dates[:keep]

    os.makedirs(DATA, exist_ok=True)
    for stale in glob.glob(os.path.join(DATA, "20*.json")):
        if os.path.basename(stale)[:-5] not in dates:
            os.remove(stale)

    manifest = []
    latest = None
    for date in dates:
        path = os.path.join(EDITIONS, date, "edition.md")
        try:
            edition = edition_md.parse(open(path).read())
        except edition_md.ParseError as exc:
            sys.exit(f"editions/{date}/edition.md: {exc}")
        edition["date"] = date
        edition["stats"] = {k: edition.pop(k) for k in
                            ("sources_ok", "sources_total", "fetched", "candidates", "full_text") if k in edition}
        edition["stats"]["stories"] = len(edition["stories"])
        extra = [s["topic"] for s in edition["stories"] if s["topic"] not in topic_order]
        edition["topics"] = topic_order + sorted(set(extra), key=extra.index)
        with open(os.path.join(DATA, f"{date}.json"), "w") as f:
            json.dump(edition, f, ensure_ascii=False, separators=(",", ":"))
        manifest.append({
            "date": date,
            "edition": edition["edition"],
            "stories": len(edition["stories"]),
            "must_read": sum(1 for s in edition["stories"] if s["signal"] == "must-read"),
            "lead": edition["stories"][0]["headline"] if edition["stories"] else "",
        })
        latest = latest or (edition, path)

    with open(os.path.join(DATA, "index.json"), "w") as f:
        json.dump({"count": max((m["edition"] for m in manifest), default=0),
                   "latest": manifest[0]["date"] if manifest else None,
                   "archive_days": settings.get("archive_days", 7),
                   "editions": manifest}, f, ensure_ascii=False, indent=1)
    with open(os.path.join(DATA, "site.json"), "w") as f:
        json.dump(site, f, ensure_ascii=False, indent=1)

    for name in ("latest.md", "latest.json", "feed.xml"):
        if not latest and os.path.exists(os.path.join(DOCS, name)):
            os.remove(os.path.join(DOCS, name))
    if latest:
        edition, path = latest
        with open(os.path.join(DOCS, "latest.md"), "w", encoding="utf-8-sig") as f:  # BOM: Pages serves .md without a charset
            f.write(render_markdown(edition, site))
        shutil.copy(os.path.join(DATA, f"{edition['date']}.json"), os.path.join(DOCS, "latest.json"))
        with open(os.path.join(DOCS, "feed.xml"), "w") as f:
            f.write(render_rss(edition, site))

    print(f"built docs/data for {len(manifest)} edition(s)"
          + (f"; latest {manifest[0]['date']} (No. {manifest[0]['edition']})" if manifest else "; archive is empty"))


if __name__ == "__main__":
    main()
