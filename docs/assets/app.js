/* EverythingTech -- the one template. Renders any edition, current or
   archived, from docs/data/<date>.json using the render config in
   docs/data/site.json. Editions are data; this file is the only place the
   page layout lives, so a change here applies to every date at once.

   Everything that came from a feed is untrusted: every field goes through
   esc(), every link through safeUrl(). */
(function () {
  "use strict";

  const TOPIC_COLORS = ["violet", "cyan", "amber", "lime", "coral", "blue", "pink", "mint"];
  const app = document.getElementById("app");
  const progress = document.getElementById("progress");
  const toastEl = document.getElementById("toast");
  const state = { site: null, index: null, edition: null, date: null, topic: "", signal: "", cursor: -1 };

  /* ---------- helpers ---------- */
  const esc = (v) => String(v == null ? "" : v).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const safeUrl = (u) => {
    if (!u || typeof u !== "string" || !/^https?:\/\//i.test(u.trim())) return "";
    try { const url = new URL(u.trim()); return /^https?:$/.test(url.protocol) ? url.href : ""; } catch (e) { return ""; }
  };
  const ext = (u, text, cls) => {
    const href = safeUrl(u);
    return href ? `<a href="${esc(href)}" target="_blank" rel="noopener noreferrer"${cls ? ` class="${cls}"` : ""}>${text}</a>` : text;
  };
  const pad = (n, w) => String(n).padStart(w || 2, "0");
  const parseDate = (d) => { const [y, m, day] = d.split("-").map(Number); return new Date(y, m - 1, day); };
  const longDate = (d) => parseDate(d).toLocaleDateString("en-GB", { weekday: "long", day: "numeric", month: "long", year: "numeric" });
  const shortDate = (d) => parseDate(d).toLocaleDateString("en-GB", { weekday: "short", day: "numeric", month: "short" });
  const words = (s) => (String(s || "").match(/\S+/g) || []).length;
  const fmtMinutes = (m) => (m >= 60 ? `${Math.floor(m / 60)}h ${pad(Math.round(m % 60))}m` : `${Math.round(m)} min`);
  const feature = (name) => !state.site || !state.site.features || state.site.features[name] !== false;

  async function getJSON(path) {
    const res = await fetch(path, { cache: "no-cache" });
    if (!res.ok) throw new Error(`${path}: HTTP ${res.status}`);
    return res.json();
  }

  function toast(msg) {
    toastEl.textContent = msg;
    toastEl.classList.add("on");
    clearTimeout(toast.t);
    toast.t = setTimeout(() => toastEl.classList.remove("on"), 1800);
  }

  const ICON = {
    archive: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="4"/><path d="M5 8v12h14V8M10 12h4"/></svg>',
    left: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 5l-7 7 7 7"/></svg>',
    right: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 5l7 7-7 7"/></svg>',
    sun: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
    moon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z"/></svg>',
    rss: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 11a9 9 0 0 1 9 9M4 4a16 16 0 0 1 16 16"/><circle cx="5" cy="19" r="1.5" fill="currentColor"/></svg>',
    github: '<svg viewBox="0 0 24 24"><path d="M12 .5a11.5 11.5 0 0 0-3.64 22.41c.58.1.79-.25.79-.56v-2c-3.2.7-3.88-1.37-3.88-1.37-.53-1.34-1.29-1.7-1.29-1.7-1.05-.72.08-.7.08-.7 1.16.08 1.77 1.19 1.77 1.19 1.03 1.77 2.71 1.26 3.37.96.1-.75.4-1.26.73-1.55-2.56-.29-5.25-1.28-5.25-5.68 0-1.26.45-2.28 1.19-3.09-.12-.29-.52-1.46.11-3.05 0 0 .97-.31 3.17 1.18a11 11 0 0 1 5.77 0c2.2-1.49 3.17-1.18 3.17-1.18.63 1.59.23 2.76.11 3.05.74.81 1.19 1.83 1.19 3.09 0 4.41-2.7 5.38-5.27 5.67.41.36.78 1.06.78 2.14v3.17c0 .31.21.67.8.56A11.5 11.5 0 0 0 12 .5z"/></svg>',
    up: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 12l7-7 7 7"/></svg>',
    coffee: '<svg class="coffee" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path class="steam s1" d="M8 3c-.6 1 .6 2 0 3"/><path class="steam s2" d="M12 2.5c-.6 1 .6 2 0 3"/><path class="steam s3" d="M16 3c-.6 1 .6 2 0 3"/><path d="M4 9h14v6a4 4 0 0 1-4 4H8a4 4 0 0 1-4-4V9z"/><path d="M18 11h1.5a2.5 2.5 0 0 1 0 5H18"/></svg>',
    linkedin: '<svg viewBox="0 0 24 24"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.13 2.06 2.06 0 0 1 0 4.13zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0z"/></svg>',
  };
  const CHIP = '<svg class="chip" viewBox="0 0 8 8" shape-rendering="crispEdges" aria-hidden="true">' +
    '<g class="pin"><rect x="2" y="0" width="1" height="2"/><rect x="5" y="0" width="1" height="2"/><rect x="2" y="6" width="1" height="2"/><rect x="5" y="6" width="1" height="2"/>' +
    '<rect x="0" y="2" width="2" height="1"/><rect x="0" y="5" width="2" height="1"/><rect x="6" y="2" width="2" height="1"/><rect x="6" y="5" width="2" height="1"/></g>' +
    '<rect class="body" x="2" y="2" width="4" height="4"/><rect class="core" x="3" y="3" width="2" height="2"/></svg>';


  const CHIP_MINI = '<svg class="chip-mini" viewBox="0 0 8 8" shape-rendering="crispEdges" aria-hidden="true">' +
    '<g class="pin"><rect x="2" y="0" width="1" height="2"/><rect x="5" y="0" width="1" height="2"/><rect x="2" y="6" width="1" height="2"/><rect x="5" y="6" width="1" height="2"/>' +
    '<rect x="0" y="2" width="2" height="1"/><rect x="0" y="5" width="2" height="1"/><rect x="6" y="2" width="2" height="1"/><rect x="6" y="5" width="2" height="1"/></g>' +
    '<rect class="body" x="2" y="2" width="4" height="4"/><rect class="core" x="3" y="3" width="2" height="2"/></svg>';

  function byBrand() {
    const c = state.site.curator || {};
    const site = state.site;
    const link = c.site || c.linkedin || c.github || "#";
    return `<a class="tb-brand" href="${esc(location.pathname)}" data-date="${esc(state.index.latest || "")}" aria-label="${esc(site.name)}, home">
        ${CHIP_MINI}<span class="tb-brand-name">${esc(site.name)}<span class="cursor">_</span></span>
      </a>
      ${c.name ? `<span class="tb-by">by ${ext(link, esc(c.name), "tb-by-link")}</span>` : ""}`;
  }

  /* ---------- theme ---------- */
  function applyThemeConfig(site) {
    const theme = site.theme || {};
    const decl = (vars) => Object.entries(vars || {}).filter(([k]) => /^--[a-z0-9-]+$/i.test(k))
      .map(([k, v]) => `${k}:${String(v).replace(/[;{}<]/g, "")}`).join(";");
    const dark = decl(theme.dark), light = decl(theme.light);
    if (dark || light) {
      const style = document.createElement("style");
      style.textContent =
        `:root[data-theme="dark"]{${dark}} @media (prefers-color-scheme: dark){:root:not([data-theme="light"]){${dark}}}` +
        `:root[data-theme="light"]{${light}} @media (prefers-color-scheme: light){:root:not([data-theme="dark"]){${light}}}`;
      document.head.appendChild(style);
    }
    let saved = null;
    try { saved = localStorage.getItem("et-theme"); } catch (e) {}
    if (!saved && (theme.default === "dark" || theme.default === "light")) document.documentElement.dataset.theme = theme.default;
  }
  const currentTheme = () => document.documentElement.dataset.theme ||
    (matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark");
  function toggleTheme() {
    const next = currentTheme() === "dark" ? "light" : "dark";
    document.documentElement.dataset.theme = next;
    try { localStorage.setItem("et-theme", next); } catch (e) {}
    const btn = document.getElementById("theme-btn");
    if (btn) btn.innerHTML = themeButton();
    toast(next === "dark" ? "night shift" : "day shift");
  }
  const themeButton = () => (currentTheme() === "dark" ? ICON.sun : ICON.moon) + '<span class="tb-label">' + (currentTheme() === "dark" ? "Day" : "Night") + "</span>";

  /* ---------- routing ---------- */
  function readUrl() {
    const q = new URLSearchParams(location.search);
    return { d: q.get("d"), t: q.get("t") || "", s: q.get("s") || "" };
  }
  function writeUrl(push) {
    const q = new URLSearchParams();
    if (state.date && state.index && state.date !== state.index.latest) q.set("d", state.date);
    if (state.topic) q.set("t", state.topic);
    if (state.signal) q.set("s", state.signal);
    const url = location.pathname + (q.toString() ? "?" + q : "") + location.hash;
    history[push ? "pushState" : "replaceState"](null, "", url);
  }
  const editionUrl = (date) => (date === state.index.latest ? location.pathname : `?d=${encodeURIComponent(date)}`);

  /* ---------- story pieces ---------- */
  function topicColor(topic) {
    const i = (state.edition.topics || []).indexOf(topic);
    return `var(--${TOPIC_COLORS[(i < 0 ? 0 : i) % TOPIC_COLORS.length]})`;
  }

  function byline(s) {
    const bits = [];
    const primary = (s.sources || [])[0];
    if (primary) bits.push(ext(primary.url || s.url, esc(primary.name)));
    if (s.author) bits.push(`<span>by ${esc(s.author)}</span>`);
    if (s.read_minutes) bits.push(`<span>${esc(s.read_minutes)} min original</span>`);
    if (s.discuss_url) {
      const stats = [s.points ? `${s.points} pts` : "", s.comments ? `${s.comments} comments` : ""].filter(Boolean).join(" · ");
      const via = s.discuss_via || "discussion";
      bits.push(ext(s.discuss_url, `${esc(stats || "discuss")} on ${esc(via)}`, "hn"));
    }
    if (s.full_text === false) bits.push('<span class="warn" title="The source blocked automated reading; this write-up is based on the headline and standfirst only.">⚠ from the feed snippet</span>');
    return `<div class="byline mono">${bits.join("")}</div>`;
  }

  function takeaways(s) {
    if (!s.takeaways || !s.takeaways.length) return "";
    return `<div class="takeaways"><h4>Takeaways</h4><ul>${s.takeaways.map((t) => `<li>${esc(t)}</li>`).join("")}</ul></div>`;
  }

  function also(s) {
    const rest = (s.sources || []).slice(1).filter((x) => safeUrl(x.url));
    if (!rest.length) return "";
    return `<div class="also">also covered by ${rest.map((x) => ext(x.url, esc(x.name))).join("")}</div>`;
  }

  function figure(s) {
    const src = safeUrl(s.image);
    if (!src || !feature("images")) return "";
    const name = ((s.sources || [])[0] || {}).name || "";
    return `<figure class="shot" data-src="${esc(name)}"><img src="${esc(src)}" alt="" loading="lazy" referrerpolicy="no-referrer"></figure>`;
  }

  function kicker(s, n) {
    const labels = (state.site && state.site.signals) || {};
    const sig = s.signal === "must-read"
      ? `<span class="stamp">${esc(labels["must-read"] || "Must-read")}</span>`
      : `<span class="sig">${esc(labels[s.signal] || s.signal)}</span>`;
    return `<div class="kicker"><span class="rank">No.${pad(n + 1)}</span><span class="topic">${esc(s.topic)}</span>${sig}</div>`;
  }

  function story(s, n, kind) {
    const body = s.body || [];
    const wireKind = kind.startsWith("w-");
    const keep = kind === "w-wide" || kind === "w-full" ? 2 : kind === "brief-item" ? 0 : 1;
    const collapsible = (wireKind || kind === "feature-rest" || kind === "brief-item") && (body.length > keep || (s.takeaways || []).length);
    const shown = collapsible ? body.slice(0, keep) : body;
    const hidden = collapsible ? body.slice(keep) : [];
    const paras = (list) => list.map((p) => `<p>${esc(p)}</p>`).join("");
    const kindCls = kind === "feature-hero" ? "feature feature-hero" : kind === "feature-rest" ? "feature" : wireKind ? `wire ${kind}` : kind;
    const cls = ["story", kind === "brief-item" ? "" : "box", kindCls, s.signal === "notable" ? "notable" : "", `signal-${s.signal}`].filter(Boolean).join(" ");
    const title = `<h3>${ext(s.url, esc(s.headline))}</h3>`;
    // migrated editions carry one summary as both dek and body; print it once
    const dek = s.dek && s.dek.trim() !== String(body[0] || "").trim() ? `<p class="dek">${esc(s.dek)}</p>` : "";
    const head = `${kicker(s, n)}${title}${dek}${byline(s)}`;
    const bodyCls = kind === "w-wide" || kind === "w-full" ? "body cols2" : "body";
    const rest = collapsible
      ? `${shown.length ? `<div class="${bodyCls}">${paras(shown)}</div>` : ""}<div class="more"><div class="body">${paras(hidden)}</div>${takeaways(s)}</div>`
      : `<div class="body${kind === "lead" ? " dropcap" : ""}${kind === "lead" && body.join(" ").length > 900 ? " cols" : ""}">${paras(shown)}</div>${takeaways(s)}`;
    const actions = `<div class="actions">
        ${ext(s.url, "Read at source ↗", "act primary")}
        ${collapsible ? `<button class="act" data-act="expand" aria-expanded="false">Expand +</button>` : ""}
        <span class="spacer"></span>
        <button class="act ghost" data-act="copy" title="Copy a link to this story">Link #</button>
      </div>`;
    let inner;
    if (kind === "lead" && figure(s)) {
      inner = `<div class="lead-grid"><div>${head}</div>${figure(s)}</div>${rest}${also(s)}${actions}`;
    } else if (kind === "feature-hero") {
      inner = `${head}${figure(s)}${rest}${also(s)}${actions}`;
    } else if (kind === "feature-rest" || kind === "w-half") {
      inner = `${figure(s)}${head}${rest}${also(s)}${actions}`;
    } else if (kind === "w-wide" || kind === "w-full") {
      const fig = figure(s);
      inner = `<div class="wide-top${fig ? " has-fig" : ""}"><div>${head}</div>${fig}</div>${rest}${also(s)}${actions}`;
    } else {
      inner = `${head}${rest}${also(s)}${actions}`;
    }
    return `<article class="${cls}${kind === "lead" && figure(s) ? " has-image" : ""}" id="s-${n + 1}" data-n="${n}"
      data-topic="${esc(s.topic)}" data-signal="${esc(s.signal)}" style="--c:${topicColor(s.topic)}">${inner}</article>`;
  }

  // Right-hand masthead slot: a countdown to the next edition on today's
  // paper, how old it is on an archived one. Times are in the paper's zone.
  function tzNow() {
    const tz = (state.site && state.site.timezone) || "Asia/Kolkata";
    const parts = Object.fromEntries(new Intl.DateTimeFormat("en-CA", { timeZone: tz, year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit", hourCycle: "h23" })
      .formatToParts(new Date()).map((p) => [p.type, p.value]));
    return { date: `${parts.year}-${parts.month}-${parts.day}`, minutes: Number(parts.hour) * 60 + Number(parts.minute) };
  }
  function clockText() {
    if (!state.site) return "";
    let now;
    try { now = tzNow(); } catch (e) { return ""; }
    if (state.index && state.date && state.date !== state.index.latest) {
      const days = Math.round((parseDate(now.date) - parseDate(state.date)) / 864e5);
      return days <= 0 ? "From the archive" : `From the archive · ${days} day${days === 1 ? "" : "s"} ago`;
    }
    const [h, m] = String(state.site.edition_time || "08:30").match(/\d+/g).map(Number);
    const left = ((h * 60 + m) - now.minutes + 1440) % 1440 || 1440;
    return `Next edition in ${Math.floor(left / 60)}h ${pad(left % 60)}m`;
  }
  setInterval(() => { const el = document.getElementById("clock"); if (el) el.textContent = clockText(); }, 30000);

  /* ---------- page sections ---------- */
  function topbar() {
    const eds = state.index.editions;
    const i = eds.findIndex((e) => e.date === state.date);
    const newer = i > 0 ? eds[i - 1] : null, older = i >= 0 && i < eds.length - 1 ? eds[i + 1] : null;
    const count = state.edition ? `${state.edition.stories.length} stories` : "";
    const nav = (e, dir, label) => e
      ? `<a class="tb-btn" href="${esc(editionUrl(e.date))}" data-date="${esc(e.date)}" title="${label}: ${esc(longDate(e.date))}">${dir === "l" ? ICON.left : ""}<span class="tb-label">${label}</span>${dir === "r" ? ICON.right : ""}</a>`
      : `<button class="tb-btn" disabled>${dir === "l" ? ICON.left : ""}<span class="tb-label">${label}</span>${dir === "r" ? ICON.right : ""}</button>`;
    return `<nav class="topbar" aria-label="Edition"><div class="wrap">
      <button class="tb-btn" data-act="archive" title="Archive (a)">${ICON.archive}<span class="tb-label">Archive</span></button>
      ${nav(older, "l", "Older")}
      <span class="tb-date">${state.date ? esc(shortDate(state.date)) : ""}</span>
      ${nav(newer, "r", "Newer")}
      <span class="tb-count">${esc(count)}</span>
      <span class="spacer"></span>
      <button class="tb-btn tb-top" data-act="top" title="Back to top">${ICON.up}<span class="tb-label">Top</span></button>
      <button class="tb-btn tb-how" data-act="how" title="How it works">How it works</button>
      <a class="tb-btn" href="feed.xml" title="RSS feed">${ICON.rss}<span class="tb-label">RSS</span></a>
      <button class="tb-btn" id="theme-btn" data-act="theme" title="Toggle theme (t)">${themeButton()}</button>
      ${feature("keyboard_shortcuts") ? '<button class="tb-btn" data-act="keys" title="Keyboard shortcuts (?)">?</button>' : ""}
    </div></nav>`;
  }

  function ticker(stories) {
    if (!feature("ticker") || !stories.length) return "";
    const items = stories.map((s, n) =>
      `<a class="ticker-item" href="#s-${n + 1}" style="--c:${topicColor(s.topic)}"><i></i>${esc(s.headline)}</a>`).join("");
    const secs = Math.max(60, stories.length * 7);
    return `<div class="ticker" aria-label="Headlines"><span class="ticker-label">LIVE WIRE</span>
      <div class="ticker-track" style="--tick-duration:${secs}s">${items}<span aria-hidden="true" style="display:contents">${items}</span></div></div>`;
  }

  function masthead(ed) {
    const site = state.site;
    const stories = ed ? ed.stories : [];
    const digestWords = stories.reduce((a, s) => a + words(s.dek) + (s.body || []).reduce((b, p) => b + words(p), 0), 0);
    const tz = site.timezone || "Asia/Kolkata", tzLabel = site.timezone_label || "IST";
    let printed = site.edition_time;
    try {
      if (ed && ed.generated_at) printed = new Date(ed.generated_at).toLocaleTimeString("en-GB", { hour: "2-digit", minute: "2-digit", hour12: false, timeZone: tz }) + " " + tzLabel;
    } catch (e) {}
    const line = ed ? [
      `<span>${esc(longDate(ed.date))}</span>`,
      `<span>${stories.length} stories</span>`,
      `<span>${stories.filter((s) => s.signal === "must-read").length} must-read</span>`,
      `<span>~${Math.max(1, Math.round(digestWords / 230))} min read</span>`,
    ].join("") : `<span>${esc(site.description)}</span>`;
    return `<header class="masthead wrap" id="top">
      <div class="masthead-meta"><span>Vol. 1 · No. ${pad(ed ? ed.edition : 0, 3)}</span><span>Printed ${esc(printed || "")}</span><span id="clock">${esc(clockText())}</span></div>
      <a class="brand" href="${esc(location.pathname)}" data-date="${esc(state.index.latest || "")}" aria-label="${esc(site.name)}, latest edition">${CHIP}<span class="brand-name">${esc(site.name)}<span class="cursor">_</span></span></a>
      <p class="tagline"><span class="tag-neon">all at once.</span> <span class="tag-body">${esc(site.tagline)}</span> <span class="coffee-wrap" aria-hidden="true">${ICON.coffee}</span></p>
      ${(function(){const c=state.site.curator||{};const l=c.site||c.linkedin||c.github||"#";return c.name?`<p class="curator-line">curated_by ${ext(l, esc(c.name), "curator-name")}</p>`:"";})()}
      <div class="rule"></div>
      <div class="edition-line">${line}</div>
      ${ed && state.date !== state.index.latest ? `<p class="legacy-note">You're reading an archived edition. <a href="${esc(location.pathname)}" data-date="${esc(state.index.latest)}">Jump to today's →</a></p>` : ""}
    </header>`;
  }

  function brief(ed) {
    if (!feature("brief") || !(ed.brief || []).length) return "";
    return `<section class="brief box" aria-label="The Brief"><div class="brief-head"><h2>The Brief</h2><span>60-second version</span></div>
      <ol>${ed.brief.map((b) => `<li>${esc(b)}</li>`).join("")}</ol></section>`;
  }

  function machineRoom(ed) {
    const st = ed.stats;
    if (!feature("machine_room") || !st || !st.fetched) return "";
    const original = ed.stories.reduce((a, s) => a + (Number(s.read_minutes) || 0), 0);
    const digest = Math.max(1, Math.round(ed.stories.reduce((a, s) => a + words(s.dek) + (s.body || []).reduce((b, p) => b + words(p), 0), 0) / 230));
    const rows = [
      ["fetched", st.fetched, "--blue"],
      ["shortlisted", st.candidates, "--violet"],
      ["read in full", st.full_text, "--cyan"],
      ["printed", st.stories || ed.stories.length, "--pink"],
    ].filter((r) => r[1] != null);
    const max = Math.max(...rows.map((r) => r[1]));
    return `<section class="machine box" aria-label="Machine room"><h3>Machine room <em>● ${esc(st.sources_ok)}/${esc(st.sources_total)} sources up</em></h3>
      <div class="funnel">${rows.map(([label, v, c]) =>
        `<div class="funnel-row"><span>${label}</span><span class="funnel-bar"><i style="--c:var(${c})" data-w="${(100 * v / max).toFixed(1)}"></i></span><b>${esc(v)}</b></div>`).join("")}</div>
      ${original ? `<p><strong>~${fmtMinutes(original)}</strong> of original reading, distilled to <strong>${digest} min</strong>. Nothing here is copied — every word was rewritten from the source.</p>` : ""}
    </section>`;
  }

  function filters(ed) {
    const count = (fn) => ed.stories.filter(fn).length;
    const topics = (ed.topics || []).filter((t) => count((s) => s.topic === t));
    const labels = state.site.signals || {};
    const pill = (kind, value, label, n, color) =>
      `<button class="pill" data-filter="${kind}" data-value="${esc(value)}" aria-pressed="${(kind === "t" ? state.topic : state.signal) === value}"${color ? ` style="--c:${color}"` : ""}>${color ? "<i></i>" : ""}${esc(label)} <small>${n}</small></button>`;
    return `<div class="filters" role="toolbar" aria-label="Filter stories">
      <div class="group"><span class="label">Topic</span>${pill("t", "", "All", ed.stories.length)}${topics.map((t) => pill("t", t, t, count((s) => s.topic === t), topicColor(t))).join("")}</div>
      <div class="group"><span class="label">Signal</span>${["must-read", "recommended", "notable"].filter((g) => count((s) => s.signal === g))
        .map((g) => pill("s", g, labels[g] || g, count((s) => s.signal === g))).join("")}</div>
      <span class="spacer"></span><span class="filter-status" id="filter-status"></span>
    </div>`;
  }

  // Compose the wire like a page, not a grid: each row is picked from the
  // next stories' length -- a long story gets a wide block beside a narrow
  // one, two mid-length stories split the row, short ones go three across.
  const WIRE_INITIAL = 8;
  function wireRows(items) {
    // weights are ranked within the day, so "long" means long for this edition
    const weight = ([st]) => (st.body || []).join(" ").length + (st.takeaways || []).join(" ").length / 2 + (safeUrl(st.image) ? 350 : 0);
    const sorted = items.map(weight).sort((x, y) => y - x);
    const heavy = sorted[Math.floor(sorted.length * 0.3)] ?? Infinity;
    const mid = sorted[Math.floor(sorted.length * 0.65)] ?? Infinity;
    const tier = (it) => (weight(it) > heavy ? 2 : weight(it) > mid ? 1 : 0);
    const rows = [];
    let last = "";
    for (let i = 0; i < items.length;) {
      const [a, b, c] = [items[i], items[i + 1], items[i + 2]];
      let type;
      if (!b) type = "full";
      else if ((tier(a) === 2 || tier(b) === 2) && last !== "wide") type = "wide";
      else if (c && last !== "triple" && (tier(a) + tier(b) + tier(c) <= 3 || last === "half")) type = "triple";
      else if (last !== "half" && tier(a) >= 1 && tier(b) >= 1) type = "half";
      else if (c) type = "triple";
      else type = "half";
      if (type === "full") rows.push([[a, "w-full"]]);
      else if (type === "wide") {
        const aWide = weight(a) >= weight(b);
        rows.push([[a, aWide ? "w-wide" : "w-third"], [b, aWide ? "w-third" : "w-wide"]]);
      } else if (type === "half") rows.push([[a, "w-half"], [b, "w-half"]]);
      else rows.push([[a, "w-third"], [b, "w-third"], [c, "w-third"]]);
      i += rows[rows.length - 1].length;
      last = type;
    }
    return rows;
  }
  function wireSection(items) {
    let shown = 0;
    const cards = wireRows(items).map((row) => {
      const deferred = shown >= WIRE_INITIAL;
      shown += row.length;
      return row.map(([[s, n], kind]) => story(s, n, kind).replace('class="story', `class="${deferred ? "deferred " : ""}story`)).join("");
    }).join("");
    const later = (cards.match(/class="deferred story/g) || []).length;
    return `<section data-section><div class="sec-head"><h2>The Wire</h2><span class="line"></span><span class="note">everything else worth your time</span></div>
      <div class="grid-wire">${cards}</div>
      ${later ? `<div class="more-wrap"><button class="act more-btn" data-act="more-wire">More from the wire <b>+${later}</b></button></div>` : ""}</section>`;
  }

  function editionBody(ed) {
    const [lead, ...rest] = ed.stories;
    const indexed = rest.map((s, i) => [s, i + 1]);
    const features = indexed.filter(([s]) => s.signal === "must-read");
    const wire = indexed.filter(([s]) => s.signal === "recommended");
    const briefs = indexed.filter(([s]) => s.signal !== "must-read" && s.signal !== "recommended");
    const side = brief(ed) + machineRoom(ed);
    return `<main class="wrap">
      <div class="front">${story(lead, 0, "lead")}${side ? `<aside class="side">${side}</aside>` : ""}</div>
      ${filters(ed)}
      ${features.length ? `<section data-section><div class="sec-head"><h2>Must-reads</h2><span class="line"></span><span class="note">${features.length} picks</span></div>
        <div class="grid-feature">
          ${story(features[0][0], features[0][1], "feature-hero")}
          ${features.length > 1 ? `<div class="feature-rest">${features.slice(1).map(([s, n]) => story(s, n, "feature-rest")).join("")}</div>` : ""}
        </div></section>` : ""}
      ${wire.length ? wireSection(wire) : ""}
      ${briefs.length ? `<section data-section><div class="sec-head"><h2>In Brief</h2><span class="line"></span><span class="note">quick hits, one tap to expand</span></div>
        <div class="briefs">${briefs.map(([s, n]) => story(s, n, "brief-item")).join("")}</div></section>` : ""}
      <p class="empty-filter" id="empty-filter">Nothing matches that filter today. <button class="act" data-act="clear">Clear filters</button></p>
    </main>`;
  }

  function awaiting() {
    return `<main class="wrap"><div class="awaiting box"><h2>Awaiting the first edition</h2>
      <p>The presses run every morning at ${esc(state.site.edition_time)}. Check back after the first run.</p></div></main>`;
  }

  function footer() {
    const site = state.site, c = site.curator || {};
    const src = state.date && site.repo ? safeUrl(`${site.repo}/blob/main/editions/${state.date}/edition.md`) : "";
    return `<footer class="site-foot"><div class="wrap">
      <div class="foot-grid">
        <div>
          <p class="signoff"><span class="p">$</span> curated_by <span class="me">${esc(c.name)}</span></p>
          <p>${esc(site.description)}</p>
          <div class="socials">
            ${c.github ? ext(c.github, ICON.github + '<span class="sr-only">GitHub</span>', "social box") : ""}
            ${c.linkedin ? ext(c.linkedin, ICON.linkedin + '<span class="sr-only">LinkedIn</span>', "social box") : ""}
          </div>
        </div>
        <div><h4>Take it with you</h4><ul>
          <li><a href="feed.xml">RSS feed</a></li>
          <li><a href="latest.md">Latest edition as Markdown</a></li>
          <li><a href="latest.json">Latest edition as JSON</a></li>
          ${src ? `<li>${ext(src, "This edition's source file ↗")}</li>` : ""}
        </ul></div>
        <div><h4>How it works</h4><ul>
          <li>Pulls ${esc(state.edition && state.edition.stats ? state.edition.stats.sources_total : "every")} sources overnight</li>
          <li>Groups duplicates, drops the noise</li>
          <li>Reads the full articles</li>
          <li>Writes each one up in plain words</li>
          <li>Prints at ${esc(site.edition_time)}. No ads, no trackers.</li>
        </ul></div>
      </div>
      <div class="colophon"><span>Set in Bricolage Grotesque, Newsreader &amp; JetBrains Mono.</span>
        <span>${site.repo ? ext(site.repo, "Fork it on GitHub ↗") : ""}</span></div>
    </div></footer>`;
  }

  function overlays() {
    const eds = state.index.editions;
    const shortcuts = [["j / k", "next / previous story"], ["o", "open story at source"], ["e", "expand story"], ["c", "copy link to story"],
      ["[ / ]", "older / newer edition"], ["a", "archive"], ["t", "day / night theme"], ["esc", "close, clear filters"], ["?", "this help"]];
    return `<div class="scrim" data-act="close"></div>
      <aside class="drawer" id="drawer" aria-label="Archive" aria-hidden="true">
        <header><h2>Archive</h2><button class="tb-btn" data-act="close">Close ✕</button></header>
        <div class="list">${eds.map((e) => `<a class="ed-card box${e.date === state.date ? " current" : ""}" href="${esc(editionUrl(e.date))}" data-date="${esc(e.date)}">
          <div class="top"><span>${esc(longDate(e.date))}</span><b>No. ${pad(e.edition, 3)}</b></div>
          <p class="lead-line">${esc(e.lead)}</p>
          <div class="top" style="margin-top:8px"><span>${esc(e.stories)} stories · ${esc(e.must_read)} must-read</span>${e.date === state.index.latest ? "<b>today</b>" : ""}</div></a>`).join("")}</div>
        <div class="foot">The paper keeps the last ${eds.length} edition${eds.length === 1 ? "" : "s"}. Every one is drawn fresh from its Markdown file with today's template.</div>
      </aside>
      <div class="dialog box" id="keys" role="dialog" aria-label="Keyboard shortcuts"><h2>Keyboard shortcuts</h2>
        <div class="keys">${shortcuts.map(([k, d]) => `<span>${k.split(" / ").map((x) => `<kbd>${esc(x)}</kbd>`).join(" / ")}</span><span>${esc(d)}</span>`).join("")}</div></div>
      <div class="dialog box" id="how" role="dialog" aria-label="How it works"><h2>How it works</h2>
        <div class="keys">
          <span><kbd>01</kbd></span><span>Every night, ${esc(state.edition && state.edition.stats ? state.edition.stats.sources_total : "dozens of")} sources get pulled: blogs, HN, Reddit, lab news, newsletters.</span>
          <span><kbd>02</kbd></span><span>Duplicates are grouped, repeats and junk are dropped.</span>
          <span><kbd>03</kbd></span><span>An LLM editor picks the stories that matter and reads each one in full.</span>
          <span><kbd>04</kbd></span><span>Each gets written up from scratch, in plain words, with the takeaways.</span>
          <span><kbd>05</kbd></span><span>A script checks the writing, then it's printed here at ${esc(state.site.edition_time)}.</span>
        </div></div>`;
  }

  /* ---------- render ---------- */
  function render() {
    const ed = state.edition;
    document.title = ed ? `${state.site.name} — ${longDate(ed.date)}` : `${state.site.name} — ${state.site.tagline}`;
    app.innerHTML = topbar() + (ed ? ticker(ed.stories) : "") + masthead(ed) + (ed ? editionBody(ed) : awaiting()) + footer() + overlays();
    state.cursor = -1;

    const frame = (img) => { if (img.naturalWidth && img.naturalWidth < 700) img.closest("figure").classList.add("logo"); };
    app.querySelectorAll("figure img").forEach((img) => (img.complete ? frame(img) : img.addEventListener("load", () => frame(img))));
    app.querySelectorAll("img").forEach((img) => img.addEventListener("error", () => {
      const fig = img.closest("figure");
      const card = img.closest(".lead");
      if (fig) fig.remove();
      if (card) card.classList.remove("has-image");
    }));
    requestAnimationFrame(() => app.querySelectorAll(".funnel-bar i").forEach((i) => { i.style.width = i.dataset.w + "%"; }));
    applyFilters();
    onScroll();
  }

  function applyFilters() {
    const cards = app.querySelectorAll(".story");
    let shown = 0;
    const filtered = !!(state.topic || state.signal);
    cards.forEach((card) => {
      const ok = (!state.topic || card.dataset.topic === state.topic) && (!state.signal || card.dataset.signal === state.signal);
      card.hidden = !ok;
      shown += ok;
    });
    app.querySelectorAll("[data-section]").forEach((sec) => {
      sec.hidden = !sec.querySelector(".story:not([hidden])");
      const grid = sec.querySelector(".grid-wire, .grid-feature");
      if (grid) {
        const visible = grid.querySelectorAll(".story:not([hidden])").length;
        if (grid.classList.contains("grid-wire")) grid.classList.toggle("filtering", filtered);
        else grid.classList.toggle("is-filtered", filtered && visible > 0 && visible < 4);
      }
    });
    app.querySelectorAll(".pill").forEach((p) => {
      const cur = p.dataset.filter === "t" ? state.topic : state.signal;
      p.setAttribute("aria-pressed", String(cur === p.dataset.value));
    });
    const status = document.getElementById("filter-status");
    if (status) status.textContent = state.topic || state.signal ? `showing ${shown} of ${cards.length}` : "";
    const empty = document.getElementById("empty-filter");
    if (empty) empty.classList.toggle("on", cards.length > 0 && shown === 0);
  }

  async function loadEdition(date, push) {
    state.date = date;
    try {
      state.edition = date ? await getJSON(`data/${date}.json`) : null;
    } catch (e) {
      if (date !== state.index.latest && state.index.latest) {
        toast(`no edition for ${date} — showing the latest`);
        return loadEdition(state.index.latest, false);
      }
      throw e;
    }
    if (push !== undefined) writeUrl(push);
    render();
  }

  function go(date) {
    if (!date || date === state.date) { closeOverlays(); return; }
    state.topic = state.signal = "";
    history.replaceState(null, "", location.pathname + location.search);
    loadEdition(date, true).then(() => window.scrollTo(0, 0));
  }

  /* ---------- interaction ---------- */
  const visibleCards = () => [...app.querySelectorAll(".story:not([hidden])")].filter((c) => c.offsetParent);
  function focusCard(i) {
    const cards = visibleCards();
    if (!cards.length) return;
    state.cursor = Math.max(0, Math.min(cards.length - 1, i));
    app.querySelectorAll(".story.is-current").forEach((c) => c.classList.remove("is-current"));
    const card = cards[state.cursor];
    card.classList.add("is-current");
    card.scrollIntoView({ block: "start", behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth" });
  }
  const currentCard = () => app.querySelector(".story.is-current");

  function toggleExpand(card) {
    if (!card) return;
    const btn = card.querySelector('[data-act="expand"]');
    if (!btn) return;
    const open = card.classList.toggle("open");
    btn.setAttribute("aria-expanded", String(open));
    btn.textContent = open ? "Collapse −" : "Expand +";
  }

  function copyLink(card) {
    if (!card) return;
    const q = new URLSearchParams();
    q.set("d", state.date);
    const url = `${location.origin}${location.pathname}?${q}#${card.id}`;
    (navigator.clipboard ? navigator.clipboard.writeText(url) : Promise.reject()).then(
      () => toast("link copied"), () => { prompt("Copy this link:", url); });
  }

  function openOverlay(id) {
    closeOverlays();
    const el = document.getElementById(id);
    if (!el) return;
    el.classList.add("on");
    el.setAttribute("aria-hidden", "false");
    app.querySelector(".scrim").classList.add("on");
  }
  function closeOverlays() {
    let closed = false;
    app.querySelectorAll(".drawer.on, .dialog.on, .scrim.on").forEach((el) => { el.classList.remove("on"); closed = true; });
    const drawer = document.getElementById("drawer");
    if (drawer) drawer.setAttribute("aria-hidden", "true");
    return closed;
  }

  app.addEventListener("click", (ev) => {
    const dateLink = ev.target.closest("a[data-date]");
    if (dateLink && !ev.metaKey && !ev.ctrlKey && !ev.shiftKey && ev.button === 0) {
      ev.preventDefault();
      go(dateLink.dataset.date);
      return;
    }
    const pill = ev.target.closest(".pill");
    if (pill) {
      const key = pill.dataset.filter === "t" ? "topic" : "signal";
      state[key] = state[key] === pill.dataset.value ? "" : pill.dataset.value;
      writeUrl(false);
      applyFilters();
      return;
    }
    const act = ev.target.closest("[data-act]");
    if (!act) return;
    const card = act.closest(".story");
    switch (act.dataset.act) {
      case "expand": toggleExpand(card); break;
      case "copy": copyLink(card); break;
      case "archive": openOverlay("drawer"); break;
      case "keys": openOverlay("keys"); break;
      case "how": openOverlay("how"); break;
      case "theme": toggleTheme(); break;
      case "close": closeOverlays(); break;
      case "clear": state.topic = state.signal = ""; writeUrl(false); applyFilters(); break;
      case "more-wire":
        app.querySelectorAll(".grid-wire .deferred").forEach((c) => c.classList.remove("deferred"));
        act.closest(".more-wrap").remove();
        break;
      case "top": window.scrollTo({ top: 0, behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth" }); break;
    }
  });

  document.addEventListener("keydown", (ev) => {
    if (!state.site || !feature("keyboard_shortcuts")) return;
    if (ev.metaKey || ev.ctrlKey || ev.altKey || /INPUT|TEXTAREA|SELECT/.test(ev.target.tagName)) return;
    const eds = state.index ? state.index.editions : [];
    const i = eds.findIndex((e) => e.date === state.date);
    switch (ev.key) {
      case "j": focusCard(state.cursor + 1); break;
      case "k": focusCard(state.cursor - 1); break;
      case "o": { const a = currentCard() && currentCard().querySelector("h3 a"); if (a) window.open(a.href, "_blank", "noopener"); break; }
      case "e": toggleExpand(currentCard()); break;
      case "c": copyLink(currentCard()); break;
      case "[": if (i >= 0 && i < eds.length - 1) go(eds[i + 1].date); break;
      case "]": if (i > 0) go(eds[i - 1].date); break;
      case "a": openOverlay("drawer"); break;
      case "t": toggleTheme(); break;
      case "?": openOverlay("keys"); break;
      case "Escape":
        if (!closeOverlays() && (state.topic || state.signal)) { state.topic = state.signal = ""; writeUrl(false); applyFilters(); }
        break;
      default: return;
    }
    ev.preventDefault();
  });

  function onScroll() {
    const max = document.documentElement.scrollHeight - innerHeight;
    if (feature("reading_progress")) progress.style.width = (max > 0 ? (100 * scrollY) / max : 0) + "%";
    const mast = app.querySelector(".brand");
    document.body.classList.toggle("scrolled", !!mast && mast.getBoundingClientRect().bottom < 52);
  }
  addEventListener("scroll", onScroll, { passive: true });
  addEventListener("popstate", () => {
    const u = readUrl();
    state.topic = u.t; state.signal = u.s;
    const date = u.d || state.index.latest;
    if (date !== state.date) loadEdition(date); else applyFilters();
  });

  /* ---------- boot ---------- */
  (async function boot() {
    try {
      const [site, index] = await Promise.all([getJSON("data/site.json"), getJSON("data/index.json")]);
      state.site = site;
      state.index = index;
      applyThemeConfig(site);
      const u = readUrl();
      state.topic = u.t;
      state.signal = u.s;
      await loadEdition(u.d || index.latest || null);
      if (location.hash) {
        const target = document.querySelector(location.hash.replace(/[^#\w-]/g, ""));
        if (target) {
          target.classList.add("is-current");
          state.cursor = visibleCards().indexOf(target);
          target.scrollIntoView({ block: "start" });
        }
      }
    } catch (e) {
      app.innerHTML = `<div class="boot">the presses jammed: ${esc(e.message)}<br><br>
        try the <a href="latest.md">Markdown edition</a> or the <a href="feed.xml">RSS feed</a>.</div>`;
    }
  })();
})();
