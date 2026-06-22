#!/usr/bin/env python3
"""
Generate rich HTML explainer pages for individual USDR bridges.

Each explainer is a standalone, dark-theme HTML page at:
  dashboard/explainers/{bridge-id}.html

Usage:
    python scripts/generate_explainers.py [bridge-id ...]

Without arguments, generates explainers for the default set of featured bridges.
"""
from __future__ import annotations

import sys
import html
import yaml
import textwrap
from pathlib import Path
from datetime import date

from crosscheck_browser import browser_runner_script, colab_url

ROOT = Path(__file__).parent.parent
EXPLAINER_DIR = ROOT / "dashboard" / "explainers"
CROSS_DOMAIN_DIR = ROOT / "cross-domain"
PROTOCOLS_DIR = ROOT / "protocols-catalog"
GITHUB_REPO = "KR8ZYSHO3/Universal-Science-Discovery"

# Bridges to generate by default
DEFAULT_BRIDGES = [
    "b-habitat-percolation-ecology",
    "b-percolation-epidemiology",
    "b-ising-social-dynamics",
    "b-kibble-zurek-morphogenesis",
    "b-bayesian-brain-predictive-processing",
    "b-replicator-equations-evolutionary-dynamics",
    "b-sir-percolation",
]

# ── YAML loading ────────────────────────────────────────────────────────────

def find_bridge_yaml(bridge_id: str) -> Path | None:
    """Search cross-domain/ recursively for a bridge YAML matching the given id."""
    # Exact filename match first
    for p in CROSS_DOMAIN_DIR.rglob(f"{bridge_id}.yaml"):
        return p
    # Fallback: search by id field inside files
    for p in CROSS_DOMAIN_DIR.rglob("*.yaml"):
        try:
            data = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
            if data.get("id") == bridge_id:
                return p
        except Exception:
            pass
    return None


def load_bridge(bridge_id: str) -> dict:
    path = find_bridge_yaml(bridge_id)
    if path is None:
        raise FileNotFoundError(f"Bridge '{bridge_id}' not found in cross-domain/")
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    data["_source_path"] = str(path)
    return data


def load_protocols_by_bridge() -> dict[str, list[dict]]:
    """Index promoted Crosscheck protocols by source_bridge id."""
    by_bridge: dict[str, list[dict]] = {}
    if not PROTOCOLS_DIR.is_dir():
        return by_bridge
    for path in sorted(PROTOCOLS_DIR.rglob("*.yaml")):
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except Exception:
            continue
        bridge_id = data.get("source_bridge")
        protocol_id = data.get("id")
        if not bridge_id or not protocol_id:
            continue
        data["_catalog_path"] = str(path.relative_to(ROOT)).replace("\\", "/")
        by_bridge.setdefault(bridge_id, []).append(data)
    for protocols in by_bridge.values():
        protocols.sort(key=lambda p: (p.get("pollination_index", 0), p.get("id", "")))
    return by_bridge


def protocols_for_bridge(bridge_id: str, protocols_index: dict[str, list[dict]]) -> list[dict]:
    return protocols_index.get(bridge_id, [])


# ── HTML helpers ─────────────────────────────────────────────────────────────

def h(text: str) -> str:
    """HTML-escape a string."""
    return html.escape(str(text), quote=True)


def format_references(refs: list[dict]) -> str:
    if not refs:
        return "<p>No references recorded.</p>"
    items = []
    for ref in refs:
        parts = []
        if "doi" in ref:
            doi = ref["doi"].lstrip("/")
            parts.append(f'<a href="https://doi.org/{h(doi)}" target="_blank" rel="noopener">DOI:{h(doi)}</a>')
        elif "arxiv" in ref:
            arxiv = ref["arxiv"]
            parts.append(f'<a href="https://arxiv.org/abs/{h(arxiv)}" target="_blank" rel="noopener">arXiv:{h(arxiv)}</a>')
        elif "url" in ref:
            parts.append(f'<a href="{h(ref["url"])}" target="_blank" rel="noopener">{h(ref["url"])}</a>')
        if "note" in ref:
            parts.append(f'<span class="ref-note">{h(ref["note"])}</span>')
        items.append(f'<li>{"&nbsp;·&nbsp;".join(parts) if parts else h(str(ref))}</li>')
    return "<ul class=\"ref-list\">" + "\n".join(items) + "</ul>"


def format_translation_table(table: list[dict]) -> str:
    if not table:
        return ""
    rows = ""
    for entry in table:
        a = h(entry.get("field_a_term", ""))
        b = h(entry.get("field_b_term", ""))
        note = h(entry.get("note", ""))
        note_td = f'<td class="note-cell">{note}</td>' if note else '<td class="note-cell">—</td>'
        rows += f"<tr><td>{a}</td><td>{b}</td>{note_td}</tr>\n"
    return f"""
<div class="table-wrap">
<table class="translation-table">
  <thead>
    <tr>
      <th>Domain A Term</th>
      <th>Domain B Term</th>
      <th>Note</th>
    </tr>
  </thead>
  <tbody>
{rows}  </tbody>
</table>
</div>"""


def format_cross_pollination(items: list[str]) -> str:
    if not items:
        return ""
    lis = "\n".join(f"<li>{h(item.strip())}</li>" for item in items)
    return f"<ul class=\"opp-list\">{lis}</ul>"


def format_crosscheck_protocols(protocols: list[dict]) -> str:
    if not protocols:
        return ""
    cards = []
    for proto in protocols:
        pid = proto.get("id", "")
        title = " ".join(str(proto.get("title", pid)).split())
        status = proto.get("status", "draft")
        tier = proto.get("feasibility_tier", "desktop")
        prediction = " ".join(str(proto.get("falsifiable_prediction", "")).split())
        if len(prediction) > 220:
            prediction = prediction[:217] + "..."
        repro = str(proto.get("repro_bundle", "")).strip().rstrip("/")
        repro_href = f"../../{repro}/index.html" if repro else ""
        bundle_dir = ROOT / repro if repro else None
        in_browser = bool(
            bundle_dir and browser_runner_script(bundle_dir, pid)
        )
        in_colab = bool(bundle_dir and colab_url(bundle_dir, pid))
        catalog_path = proto.get("_catalog_path", "")
        yaml_href = (
            f"https://github.com/{GITHUB_REPO}/blob/main/{h(catalog_path)}"
            if catalog_path
            else ""
        )
        if in_browser:
            run_label = "Run in browser"
            run_href = repro_href
        elif in_colab:
            run_label = "Open in Colab"
            run_href = colab_url(bundle_dir, pid) or repro_href
        else:
            run_label = "Run repro bundle"
            run_href = repro_href
        run_link = (
            f'<a class="crosscheck-link" href="{h(run_href)}">{h(run_label)}</a>'
            if run_href
            else ""
        )
        yaml_link = (
            f'<a class="crosscheck-link" href="{yaml_href}" target="_blank" rel="noopener">Protocol YAML</a>'
            if yaml_href
            else ""
        )
        links = " · ".join(link for link in (run_link, yaml_link) if link)
        cards.append(
            f"""<article class="crosscheck-card">
  <div class="crosscheck-card-head">
    <h3 class="crosscheck-title">{h(title)}</h3>
    <div class="crosscheck-badges">
      <span class="badge badge-crosscheck">{h(status.upper())}</span>
      <span class="badge badge-tier">{h(tier)}</span>
    </div>
  </div>
  <p class="crosscheck-prediction">{h(prediction)}</p>
  <p class="crosscheck-meta">Protocol <code>{h(pid)}</code></p>
  <p class="crosscheck-links">{links}</p>
</article>"""
        )
    return "\n".join(cards)


def status_badge(status: str) -> str:
    cls_map = {
        "established": "badge-established",
        "proposed": "badge-proposed",
        "contested": "badge-contested",
        "stale": "badge-stale",
    }
    cls = cls_map.get(status, "badge-proposed")
    return f'<span class="badge {cls}">{h(status.upper())}</span>'


def fields_tags(fields: list[str]) -> str:
    tags = " ".join(f'<span class="field-tag">{h(f)}</span>' for f in fields)
    return f'<div class="field-tags">{tags}</div>'


def make_explainer_html(bridge: dict, protocols: list[dict] | None = None) -> str:
    bid = bridge.get("id", "unknown")
    protocols = protocols or []
    title = bridge.get("title", bid).strip()
    status = bridge.get("status", "unknown")
    fields = bridge.get("fields", [])
    bridge_claim = bridge.get("bridge_claim", "").strip()
    translation_table = bridge.get("translation_table", [])
    cross_pollination = bridge.get("cross_pollination_opportunities", [])
    communication_gap = bridge.get("communication_gap", "").strip()
    refs = bridge.get("references", [])
    related_unknowns = bridge.get("related_unknowns", [])
    related_hypotheses = bridge.get("related_hypotheses", [])
    last_reviewed = bridge.get("last_reviewed", str(date.today()))

    # Derive domain pair for the page title
    if len(fields) >= 2:
        domain_a = fields[0].replace("-", " ").title()
        domain_b = fields[1].replace("-", " ").title()
        domain_pair = f"{domain_a} ↔ {domain_b}"
    else:
        domain_pair = " ↔ ".join(f.replace("-", " ").title() for f in fields)

    # Short title (first sentence)
    short_title = title.split(".")[0].split("—")[0].strip()

    # Open Questions from related unknowns/hypotheses
    open_questions_html = ""
    if related_unknowns or related_hypotheses:
        qs = []
        for uid in related_unknowns:
            qs.append(f'<li>Unknown: <code>{h(uid)}</code></li>')
        for hid in related_hypotheses:
            qs.append(f'<li>Hypothesis: <code>{h(hid)}</code></li>')
        open_questions_html = "<ul>" + "\n".join(qs) + "</ul>"

    table_html = format_translation_table(translation_table)
    refs_html = format_references(refs)
    opp_html = format_cross_pollination(cross_pollination)
    crosscheck_html = format_crosscheck_protocols(protocols)
    badge = status_badge(status)
    ftags = fields_tags(fields)

    og_description = short_title[:160]

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{h(domain_pair)}: {h(short_title)} | USDR Explainer</title>
  <meta name="description" content="{h(og_description)}"/>

  <!-- Open Graph / social sharing -->
  <meta property="og:type" content="article"/>
  <meta property="og:title" content="{h(domain_pair)}: {h(short_title)}"/>
  <meta property="og:description" content="{h(og_description)}"/>
  <meta property="og:url" content="https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/explainers/{h(bid)}.html"/>
  <meta property="og:site_name" content="Universal Science Discovery Repository"/>
  <meta name="twitter:card" content="summary"/>
  <meta name="twitter:title" content="{h(short_title)}"/>
  <meta name="twitter:description" content="{h(og_description)}"/>

  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap"/>

  <style>
    /* ── Reset & tokens ───────────────────────────────────────────────── */
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

    :root {{
      --bg:        #0d1117;
      --bg-card:   #161b22;
      --bg-hover:  #1c2230;
      --border:    #30363d;
      --text:      #e6edf3;
      --text-dim:  #8b949e;
      --accent:    #58a6ff;
      --accent2:   #3fb950;
      --accent3:   #f78166;
      --accent4:   #d2a8ff;
      --warn:      #e3b341;
      --radius:    10px;
      --font:      'Inter', system-ui, sans-serif;
      --mono:      'JetBrains Mono', monospace;
      --max-w:     860px;
    }}

    html {{ scroll-behavior: smooth; }}

    body {{
      font-family: var(--font);
      background: var(--bg);
      color: var(--text);
      line-height: 1.7;
      font-size: 16px;
    }}

    /* ── Nav ──────────────────────────────────────────────────────────── */
    .topbar {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(13,17,23,0.92);
      backdrop-filter: blur(8px);
      border-bottom: 1px solid var(--border);
      padding: 0.6rem 1.5rem;
      display: flex;
      align-items: center;
      gap: 1rem;
    }}
    .topbar a {{
      color: var(--accent);
      text-decoration: none;
      font-size: 0.85rem;
      font-weight: 500;
      transition: opacity .15s;
    }}
    .topbar a:hover {{ opacity: .75; }}
    .topbar-sep {{ color: var(--border); }}
    .topbar-title {{ color: var(--text-dim); font-size: 0.85rem; flex: 1; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}

    /* ── Layout ───────────────────────────────────────────────────────── */
    .container {{
      max-width: var(--max-w);
      margin: 0 auto;
      padding: 2.5rem 1.5rem 4rem;
    }}

    /* ── Hero ─────────────────────────────────────────────────────────── */
    .hero {{
      padding: 2.5rem 0 2rem;
      border-bottom: 1px solid var(--border);
      margin-bottom: 2.5rem;
    }}
    .hero-domain {{
      font-size: 0.8rem;
      font-weight: 600;
      letter-spacing: .1em;
      text-transform: uppercase;
      color: var(--accent);
      margin-bottom: 0.6rem;
    }}
    .hero-title {{
      font-size: clamp(1.35rem, 3vw, 1.8rem);
      font-weight: 700;
      line-height: 1.35;
      margin-bottom: 1rem;
      color: var(--text);
    }}
    .hero-meta {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.6rem;
      align-items: center;
    }}

    /* ── Badges ───────────────────────────────────────────────────────── */
    .badge {{
      display: inline-block;
      padding: 0.2rem 0.65rem;
      border-radius: 20px;
      font-size: 0.7rem;
      font-weight: 700;
      letter-spacing: .05em;
    }}
    .badge-established {{ background: rgba(63,185,80,.18); color: var(--accent2); border: 1px solid rgba(63,185,80,.35); }}
    .badge-proposed    {{ background: rgba(88,166,255,.18); color: var(--accent);  border: 1px solid rgba(88,166,255,.35); }}
    .badge-contested   {{ background: rgba(227,179,65,.18); color: var(--warn);    border: 1px solid rgba(227,179,65,.35); }}
    .badge-stale       {{ background: rgba(139,148,158,.18);color: var(--text-dim);border: 1px solid rgba(139,148,158,.35); }}

    .field-tags {{ display: flex; flex-wrap: wrap; gap: 0.4rem; }}
    .field-tag {{
      background: rgba(88,166,255,.12);
      color: var(--accent);
      border: 1px solid rgba(88,166,255,.25);
      padding: 0.15rem 0.55rem;
      border-radius: 6px;
      font-size: 0.72rem;
      font-weight: 500;
    }}

    /* ── Sections ─────────────────────────────────────────────────────── */
    section {{ margin-bottom: 2.5rem; }}

    h2 {{
      font-size: 1.1rem;
      font-weight: 600;
      color: var(--text);
      margin-bottom: 1rem;
      padding-bottom: 0.5rem;
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    h2 .icon {{ font-size: 1.1rem; }}

    p {{ color: var(--text-dim); margin-bottom: 0.8rem; }}
    p:last-child {{ margin-bottom: 0; }}

    /* ── Card ─────────────────────────────────────────────────────────── */
    .card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.4rem 1.5rem;
    }}

    /* ── Key insight callout ──────────────────────────────────────────── */
    .insight {{
      background: linear-gradient(135deg, rgba(88,166,255,.08) 0%, rgba(63,185,80,.06) 100%);
      border: 1px solid rgba(88,166,255,.3);
      border-left: 4px solid var(--accent);
      border-radius: var(--radius);
      padding: 1.2rem 1.5rem;
    }}
    .insight p {{ color: var(--text); }}

    /* ── Translation table ────────────────────────────────────────────── */
    .table-wrap {{ overflow-x: auto; border-radius: var(--radius); }}
    .translation-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
    }}
    .translation-table thead tr {{
      background: rgba(88,166,255,.12);
    }}
    .translation-table th {{
      padding: 0.7rem 1rem;
      text-align: left;
      font-weight: 600;
      color: var(--accent);
      border-bottom: 1px solid var(--border);
      white-space: nowrap;
    }}
    .translation-table td {{
      padding: 0.65rem 1rem;
      border-bottom: 1px solid var(--border);
      color: var(--text);
      vertical-align: top;
    }}
    .translation-table tr:last-child td {{ border-bottom: none; }}
    .translation-table tr:nth-child(odd) {{ background: rgba(255,255,255,.02); }}
    .translation-table tr:hover {{ background: var(--bg-hover); }}
    .note-cell {{ color: var(--text-dim) !important; font-size: 0.82rem; }}

    /* ── References ───────────────────────────────────────────────────── */
    .ref-list {{ list-style: none; display: flex; flex-direction: column; gap: 0.5rem; }}
    .ref-list li {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 0.6rem 0.9rem;
      font-size: 0.84rem;
      display: flex;
      flex-wrap: wrap;
      gap: 0.4rem;
      align-items: center;
    }}
    .ref-list a {{ color: var(--accent); text-decoration: none; }}
    .ref-list a:hover {{ text-decoration: underline; }}
    .ref-note {{ color: var(--text-dim); }}

    /* ── Open questions ───────────────────────────────────────────────── */
    .opp-list, ul {{ padding-left: 1.3rem; display: flex; flex-direction: column; gap: 0.5rem; }}
    .opp-list li, ul li {{ color: var(--text-dim); font-size: 0.9rem; }}
    code {{ font-family: var(--mono); font-size: 0.82rem; background: rgba(88,166,255,.12); color: var(--accent); padding: 0.1rem 0.4rem; border-radius: 4px; }}

    /* ── Crosscheck protocols ─────────────────────────────────────────── */
    .crosscheck-intro {{ color: var(--text-dim); font-size: 0.92rem; margin-bottom: 1rem; }}
    .crosscheck-grid {{ display: flex; flex-direction: column; gap: 1rem; }}
    .crosscheck-card {{
      background: var(--bg-card);
      border: 1px solid rgba(63,185,80,.28);
      border-radius: var(--radius);
      padding: 1rem 1.1rem;
    }}
    .crosscheck-card-head {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 0.75rem;
      flex-wrap: wrap;
      margin-bottom: 0.55rem;
    }}
    .crosscheck-title {{ font-size: 0.98rem; font-weight: 600; line-height: 1.35; margin: 0; }}
    .crosscheck-badges {{ display: flex; gap: 0.4rem; flex-wrap: wrap; }}
    .badge-crosscheck {{ background: rgba(63,185,80,.18); color: #3fb950; border: 1px solid rgba(63,185,80,.35); }}
    .badge-tier {{ background: rgba(210,168,255,.14); color: #d2a8ff; border: 1px solid rgba(210,168,255,.3); }}
    .crosscheck-prediction {{ color: var(--text-dim); font-size: 0.88rem; margin: 0 0 0.55rem; }}
    .crosscheck-meta {{ font-size: 0.78rem; color: var(--text-dim); margin: 0 0 0.35rem; }}
    .crosscheck-links {{ font-size: 0.82rem; margin: 0; }}
    .crosscheck-link {{ color: var(--accent2); text-decoration: none; }}
    .crosscheck-link:hover {{ text-decoration: underline; }}

    /* ── Footer ───────────────────────────────────────────────────────── */
    .explainer-footer {{
      border-top: 1px solid var(--border);
      padding-top: 1.5rem;
      margin-top: 3rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 0.7rem;
    }}
    .explainer-footer p {{ font-size: 0.8rem; color: var(--text-dim); margin: 0; }}
    .explainer-footer a {{ color: var(--accent); text-decoration: none; }}

    /* ── Responsive ───────────────────────────────────────────────────── */
    @media (max-width: 600px) {{
      .container {{ padding: 1.5rem 1rem 3rem; }}
      .hero-title {{ font-size: 1.25rem; }}
      .translation-table th, .translation-table td {{ padding: 0.5rem 0.7rem; }}
    }}
  </style>
</head>
<body>

<!-- Navigation -->
<nav class="topbar">
  <a href="../../dashboard/index.html">← Dashboard</a>
  <span class="topbar-sep">|</span>
  <a href="index.html">All Explainers</a>
  <span class="topbar-sep">|</span>
  <span class="topbar-title">{h(short_title)}</span>
</nav>

<div class="container">

  <!-- Hero -->
  <header class="hero">
    <div class="hero-domain">{h(domain_pair)}</div>
    <h1 class="hero-title">{h(title)}</h1>
    <div class="hero-meta">
      {badge}
      {ftags}
    </div>
  </header>

  <!-- Overview -->
  <section id="overview">
    <h2><span class="icon">🔭</span> Overview</h2>
    <div class="card">
      <p>{h(bridge_claim)}</p>
    </div>
  </section>

  <!-- Mathematical Bridge -->
  <section id="math-bridge">
    <h2><span class="icon">⚙️</span> The Mathematical Bridge</h2>
    <div class="insight">
      <p>
        This bridge connects <strong>{h(fields[0].replace("-"," ").title() if fields else "Domain A")}</strong>
        and <strong>{h(fields[1].replace("-"," ").title() if len(fields)>1 else "Domain B")}</strong>
        through shared mathematical structure.
        {" Status: " + status.title() + " connection." if status else ""}
      </p>
    </div>
  </section>

  <!-- Translation Table -->
  {'''<section id="translation">
    <h2><span class="icon">↔️</span> Translation Table</h2>''' + table_html + "</section>" if table_html else ""}

  <!-- Communication Gap -->
  {'''<section id="comm-gap">
    <h2><span class="icon">🗺️</span> Why Hasn\'t This Been Unified?</h2>
    <div class="card"><p>''' + h(communication_gap) + '''</p></div>
  </section>''' if communication_gap else ""}

  <!-- Cross-pollination opportunities -->
  {'''<section id="opportunities">
    <h2><span class="icon">🌱</span> Cross-Pollination Opportunities</h2>''' + opp_html + "</section>" if opp_html else ""}

  <!-- Crosscheck protocols -->
  {'''<section id="crosscheck">
    <h2><span class="icon">🧪</span> Crosscheck — Prove This Bridge</h2>
    <p class="crosscheck-intro">Runnable experiment protocols promoted from this bridge. USDR maps what connects; Crosscheck proves it.</p>
    <div class="crosscheck-grid">''' + crosscheck_html + '''</div>
    <p class="crosscheck-intro" style="margin-top:1rem;">
      <a href="../../docs/CROSSCHECK.md" class="crosscheck-link">Crosscheck manifesto</a>
      · Generate more drafts: <code>python scripts/generate_crosscheck.py --bridge ''' + h(bid) + ''' --write</code>
    </p>
  </section>''' if crosscheck_html else ""}

  <!-- Open Questions -->
  {'''<section id="open-questions">
    <h2><span class="icon">❓</span> Open Questions</h2>''' + open_questions_html + "</section>" if open_questions_html else ""}

  <!-- References -->
  <section id="references">
    <h2><span class="icon">📚</span> References</h2>
    {refs_html}
  </section>

  <!-- Footer -->
  <footer class="explainer-footer">
    <p>Bridge ID: <code>{h(bid)}</code> · Last reviewed: {h(str(last_reviewed))}</p>
    <p>
      <a href="../../dashboard/index.html">← Back to Dashboard</a> ·
      <a href="https://github.com/KR8ZYSHO3/Universal-Science-Discovery" target="_blank" rel="noopener">GitHub</a>
    </p>
  </footer>

</div>
</body>
</html>
"""


# ── Index page ───────────────────────────────────────────────────────────────

def make_index_html(generated: list[dict], protocols_index: dict[str, list[dict]]) -> str:
    cards = ""
    for b in generated:
        bid = b.get("id", "")
        title = b.get("title", bid).strip()
        short = title.split(".")[0].split("—")[0].strip()[:120]
        status = b.get("status", "unknown")
        proto_count = len(protocols_index.get(bid, []))
        crosscheck_note = (
            f'<span class="crosscheck-pill">{proto_count} Crosscheck protocol{"s" if proto_count != 1 else ""}</span>'
            if proto_count
            else ""
        )
        fields = b.get("fields", [])
        pair = " ↔ ".join(f.replace("-", " ").title() for f in fields[:2]) if fields else ""
        badge = status_badge(status)
        cards += f"""
  <a class="expl-card" href="{h(bid)}.html">
    <div class="expl-pair">{h(pair)}</div>
    <div class="expl-title">{h(short)}</div>
    <div class="expl-badges">{badge}{crosscheck_note}</div>
  </a>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>USDR Explainers — Bridge Explainer Pages</title>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap"/>
  <style>
    *,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
    :root{{--bg:#0d1117;--bg-card:#161b22;--border:#30363d;--text:#e6edf3;--text-dim:#8b949e;--accent:#58a6ff;--radius:10px}}
    body{{font-family:'Inter',system-ui,sans-serif;background:var(--bg);color:var(--text);padding:2rem 1.5rem;}}
    .topbar{{display:flex;align-items:center;gap:.8rem;margin-bottom:2.5rem;padding-bottom:1rem;border-bottom:1px solid var(--border)}}
    .topbar a{{color:var(--accent);text-decoration:none;font-size:.85rem;font-weight:500}}
    h1{{font-size:1.5rem;font-weight:700;margin-bottom:.5rem}}
    p.sub{{color:var(--text-dim);margin-bottom:2rem;font-size:.9rem}}
    .grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:1rem;max-width:1000px}}
    .expl-card{{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:1.2rem;text-decoration:none;color:var(--text);transition:border-color .15s,background .15s;display:flex;flex-direction:column;gap:.5rem}}
    .expl-card:hover{{border-color:var(--accent);background:#1c2230}}
    .expl-pair{{font-size:.72rem;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--accent)}}
    .expl-title{{font-size:.9rem;font-weight:500;line-height:1.4;color:var(--text)}}
    .badge{{display:inline-block;padding:.15rem .55rem;border-radius:20px;font-size:.65rem;font-weight:700;letter-spacing:.05em;width:fit-content}}
    .badge-established{{background:rgba(63,185,80,.18);color:#3fb950;border:1px solid rgba(63,185,80,.35)}}
    .badge-proposed{{background:rgba(88,166,255,.18);color:#58a6ff;border:1px solid rgba(88,166,255,.35)}}
    .badge-contested{{background:rgba(227,179,65,.18);color:#e3b341;border:1px solid rgba(227,179,65,.35)}}
    .badge-stale{{background:rgba(139,148,158,.18);color:#8b949e;border:1px solid rgba(139,148,158,.35)}}
    .expl-badges{{display:flex;flex-wrap:wrap;gap:.35rem;align-items:center}}
    .crosscheck-pill{{display:inline-block;padding:.15rem .55rem;border-radius:20px;font-size:.65rem;font-weight:700;letter-spacing:.05em;background:rgba(63,185,80,.18);color:#3fb950;border:1px solid rgba(63,185,80,.35)}}
  </style>
</head>
<body>
<div class="topbar">
  <a href="../index.html">← Dashboard</a>
  <span style="color:var(--border)">|</span>
  <span style="color:var(--text-dim);font-size:.85rem">Bridge Explainers</span>
</div>
<h1>Bridge Explainer Pages</h1>
<p class="sub">Deep-dive explanations of key cross-domain mathematical bridges in the USDR catalog.</p>
<div class="grid">{cards}
</div>
</body>
</html>
"""


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    bridge_ids = sys.argv[1:] if len(sys.argv) > 1 else DEFAULT_BRIDGES

    EXPLAINER_DIR.mkdir(parents=True, exist_ok=True)
    protocols_index = load_protocols_by_bridge()

    generated = []
    errors = []

    for bid in bridge_ids:
        print(f"  Generating explainer for {bid} ...", end=" ", flush=True)
        try:
            bridge = load_bridge(bid)
            protocols = protocols_for_bridge(bid, protocols_index)
            html_content = make_explainer_html(bridge, protocols)
            out = EXPLAINER_DIR / f"{bid}.html"
            out.write_text(html_content, encoding="utf-8")
            proto_note = f" ({len(protocols)} Crosscheck)" if protocols else ""
            print(f"-> {out.relative_to(ROOT)}{proto_note}")
            generated.append(bridge)
        except Exception as exc:
            print(f"ERROR: {exc}")
            errors.append((bid, str(exc)))

    # Write index
    index_html = make_index_html(generated, protocols_index)
    index_path = EXPLAINER_DIR / "index.html"
    index_path.write_text(index_html, encoding="utf-8")
    print(f"  Index -> {index_path.relative_to(ROOT)}")

    print(f"\nDone: {len(generated)} explainer(s) generated, {len(errors)} error(s).")
    if errors:
        for bid, msg in errors:
            print(f"  ✗ {bid}: {msg}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
