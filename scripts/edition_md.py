"""The edition Markdown format: parse and write.

One format serves two purposes:
  * the draft the routine writes (data/draft.md) -- only ids/topic/signal
    metadata per story, plus the prose;
  * the canonical, self-contained record in editions/<date>/edition.md --
    the same thing with every story's links and metadata filled in by
    publish_edition.py, so build_site.py can rebuild any date from it alone.

    ---
    date: 2026-09-25
    edition: 3
    ---

    # The Brief

    - One line per theme of the day.

    # Stories

    ## Headline written by the editor
    - ids: 6, 15
    - topic: Security
    - signal: must-read
    - source: transluce.org | https://... | via Hacker News      (canonical only)

    > The dek: one sentence under the headline.

    First body paragraph.

    Second body paragraph.

    **Takeaways**
    - A concrete point.
"""
import re

META_KEYS = {
    "ids", "topic", "signal", "url", "source", "author", "image", "read",
    "discuss", "full text", "original title",
}


class ParseError(ValueError):
    pass


def _split_front_matter(text):
    text = text.lstrip("﻿").lstrip()
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        raise ParseError("front matter opened with '---' but never closed")
    front = {}
    for line in text[3:end].strip().splitlines():
        key, _, value = line.partition(":")
        if key.strip():
            front[key.strip()] = value.strip()
    return front, text[end + 4:]


def _blocks(text):
    return [b.strip("\n") for b in re.split(r"\n\s*\n", text) if b.strip()]


def _parse_story(heading, rest, n):
    story = {"headline": heading.strip(), "body": [], "takeaways": [], "sources": []}
    blocks = _blocks(rest)
    if not blocks or not blocks[0].lstrip().startswith("- "):
        raise ParseError(f"story {n} ('{heading[:50]}'): the line right after the headline must start the "
                         "'- ids: ...' / '- topic: ...' / '- signal: ...' list")
    for line in blocks[0].splitlines():
        line = line.strip()
        if not line.startswith("- "):
            raise ParseError(f"story {n}: unexpected line in metadata list: {line[:60]!r}")
        key, sep, value = line[2:].partition(":")
        key, value = key.strip().lower(), value.strip()
        if not sep or key not in META_KEYS:
            raise ParseError(f"story {n}: unknown metadata line {line[:60]!r} "
                             f"(allowed keys: ids, topic, signal)")
        if key == "ids":
            try:
                story["ids"] = [int(x) for x in re.split(r"[,\s]+", value.strip("[] ")) if x]
            except ValueError:
                raise ParseError(f"story {n}: ids must be candidate numbers, e.g. '- ids: 12, 40'") from None
        elif key == "source":
            parts = [p.strip() for p in value.split(" | ")]
            entry = {"name": parts[0], "url": parts[1] if len(parts) > 1 else ""}
            if len(parts) > 2 and parts[2].startswith("via "):
                entry["via"] = parts[2][4:]
            story["sources"].append(entry)
        elif key == "discuss":
            parts = [p.strip() for p in value.split(" | ")]
            story["discuss_url"] = parts[0]
            if len(parts) > 1:
                story["discuss_via"] = parts[1]
            for part in parts[2:]:
                num, _, unit = part.partition(" ")
                if num.isdigit() and unit.startswith("point"):
                    story["points"] = int(num)
                elif num.isdigit() and unit.startswith("comment"):
                    story["comments"] = int(num)
        elif key == "read":
            story["read_minutes"] = int(re.sub(r"\D", "", value) or 0) or None
        elif key == "full text":
            story["full_text"] = value.lower() in ("yes", "true")
        elif key == "original title":
            story["source_title"] = value
        else:
            story[key] = value

    in_takeaways = False
    for block in blocks[1:]:
        lines = block.splitlines()
        if lines[0].strip().strip("*").strip().rstrip(":").lower() == "takeaways":
            in_takeaways = True
            lines = lines[1:]
            if not lines:
                continue
        if in_takeaways and all(l.strip().startswith("- ") for l in lines):
            story["takeaways"] += [l.strip()[2:].strip() for l in lines]
        elif all(l.strip().startswith(">") for l in lines):
            story["dek"] = " ".join(l.strip().lstrip(">").strip() for l in lines)
        else:
            if in_takeaways:
                raise ParseError(f"story {n}: text after **Takeaways** must be '- ' bullets only")
            story["body"].append(" ".join(l.strip() for l in lines))
    story.setdefault("dek", "")
    return story


def parse(text):
    """Markdown -> edition dict. Raises ParseError with a fixable message."""
    front, text = _split_front_matter(text)
    edition = {k: v for k, v in front.items()}
    for key in ("edition", "sources_ok", "sources_total", "fetched", "candidates", "full_text"):
        if key in edition and str(edition[key]).isdigit():
            edition[key] = int(edition[key])

    parts = re.split(r"^# +(.+?)\s*$", text, flags=re.M)
    sections = {parts[i].strip().lower(): parts[i + 1] for i in range(1, len(parts) - 1, 2)}
    if "the brief" not in sections or "stories" not in sections:
        raise ParseError("needs two top-level sections: '# The Brief' and '# Stories'")

    edition["brief"] = [l.strip()[2:].strip() for l in sections["the brief"].splitlines() if l.strip().startswith("- ")]
    chunks = re.split(r"^## +(.+?)\s*$", sections["stories"], flags=re.M)
    edition["stories"] = [_parse_story(chunks[i], chunks[i + 1], (i + 1) // 2) for i in range(1, len(chunks) - 1, 2)]
    return edition


def write(edition):
    """Canonical edition dict -> Markdown."""
    stats = edition.get("stats", {})
    out = ["---", f"date: {edition['date']}", f"edition: {edition['edition']}",
           f"generated_at: {edition['generated_at']}"]
    out += [f"{k}: {v}" for k, v in stats.items()]
    out += ["---", "", "# The Brief", "", *[f"- {b}" for b in edition["brief"]], "", "# Stories", ""]
    for s in edition["stories"]:
        out += [f"## {s['headline']}", f"- ids: {', '.join(str(i) for i in s['ids'])}",
                f"- topic: {s['topic']}", f"- signal: {s['signal']}", f"- url: {s['url']}"]
        if s.get("source_title") and s["source_title"] != s["headline"]:
            out.append(f"- original title: {s['source_title']}")
        for src in s["sources"]:
            out.append(f"- source: {src['name']} | {src['url']}" + (f" | via {src['via']}" if src.get("via") else ""))
        for key, label in (("author", "author"), ("image", "image")):
            if s.get(key):
                out.append(f"- {label}: {s[key]}")
        if s.get("read_minutes"):
            out.append(f"- read: {s['read_minutes']} min")
        if s.get("discuss_url"):
            extra = [s.get("discuss_via") or "discussion"]
            if s.get("points"):
                extra.append(f"{s['points']} points")
            if s.get("comments"):
                extra.append(f"{s['comments']} comments")
            out.append(f"- discuss: {s['discuss_url']} | " + " | ".join(extra))
        out.append(f"- full text: {'yes' if s.get('full_text') else 'no'}")
        out += ["", f"> {s['dek']}", "", *[p + "\n" for p in s["body"]]]
        if s["takeaways"]:
            out += ["**Takeaways**", *[f"- {t}" for t in s["takeaways"]], ""]
    return "\n".join(out).rstrip() + "\n"
