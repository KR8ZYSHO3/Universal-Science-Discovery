#!/usr/bin/env python3
"""
Generate per-domain landing pages from the USDR catalog.
Output: dashboard/domains/{domain}.html

Bridge counts use `fields` from each bridge YAML (see schemas/bridge.yaml) and
`scripts/domain_matching.py` to align discipline tags with `unknowns-catalog/<domain>/`
folder names — **not** legacy `source_domain` / `target_domain` keys.

Usage:
    python scripts/generate_domain_pages.py
    python scripts/generate_domain_pages.py --domain biology
    python scripts/verify_domain_pages.py
"""
import yaml
import argparse
from pathlib import Path
from datetime import date

from domain_matching import catalog_domain_matches_field_tag, summarize_fields_line

ROOT = Path(__file__).parent.parent

# Filled by build_bridge_index(); avoids scanning cross-domain/ once per domain folder.
_BRIDGE_INDEX: dict[str, list] | None = None


def all_domain_slugs() -> list[str]:
    return sorted([d.name for d in (ROOT / "unknowns-catalog").iterdir() if d.is_dir()])


def build_bridge_index() -> dict[str, list]:
    """Single pass over all bridge YAML: assign each bridge to every matching catalog domain."""
    global _BRIDGE_INDEX
    slugs = all_domain_slugs()
    index: dict[str, list] = {s: [] for s in slugs}
    for p in sorted((ROOT / "cross-domain").rglob("b-*.yaml")):
        data = load_yaml(p)
        if not data:
            continue
        fields = data.get("fields") or []
        if not fields:
            continue
        entry = {
            "id": data.get("id", p.stem),
            "title": data.get("title", p.stem),
            "fields_line": summarize_fields_line(fields),
            "bridge_claim": (data.get("bridge_claim", "") or "")[:200],
            "file": str(p.relative_to(ROOT)),
        }
        for s in slugs:
            if any(catalog_domain_matches_field_tag(s, f) for f in fields):
                index[s].append(entry)
    _BRIDGE_INDEX = index
    return index
DASHBOARD = ROOT / "dashboard"
DOMAINS_DIR = DASHBOARD / "domains"

DOMAIN_META = {
    "biology": {"icon": "🧬", "color": "#22d3b8", "description": "Life, evolution, molecular mechanisms"},
    "physics": {"icon": "⚛️", "color": "#4f9cf9", "description": "Fundamental forces, matter, and energy"},
    "chemistry": {"icon": "🧪", "color": "#a78bfa", "description": "Molecular structure, reactions, and materials"},
    "neuroscience": {"icon": "🧠", "color": "#f43f5e", "description": "Brain, cognition, and neural systems"},
    "ecology": {"icon": "🌿", "color": "#4ade80", "description": "Ecosystems, biodiversity, and environmental dynamics"},
    "computer-science": {"icon": "💻", "color": "#f97316", "description": "Algorithms, computation, and AI"},
    "mathematics": {"icon": "∑", "color": "#fbbf24", "description": "Formal structures, proofs, and abstractions"},
    "materials-science": {"icon": "🔩", "color": "#94a3b8", "description": "Physical properties of matter and new materials"},
    "climate-science": {"icon": "🌍", "color": "#34d399", "description": "Earth's climate system and environmental change"},
    "astronomy": {"icon": "🔭", "color": "#818cf8", "description": "Cosmology, stellar physics, and the observable universe"},
    "medicine": {"icon": "🏥", "color": "#fb7185", "description": "Human health, disease mechanisms, and therapeutics"},
    "cognitive-science": {"icon": "💭", "color": "#c084fc", "description": "Mind, perception, memory, and consciousness"},
    "quantum-physics": {"icon": "〰", "color": "#67e8f9", "description": "Quantum mechanics, entanglement, and quantum computing"},
    "linguistics": {"icon": "🗣", "color": "#fdba74", "description": "Language structure, acquisition, and universals"},
    "social-science": {"icon": "👥", "color": "#86efac", "description": "Society, behavior, and collective dynamics"},
    "economics": {"icon": "📊", "color": "#fde68a", "description": "Markets, incentives, and resource allocation"},
    "geoscience": {"icon": "🌋", "color": "#a3a3a3", "description": "Earth structure, tectonics, and geological processes"},
    "philosophy-of-science": {"icon": "🔍", "color": "#d4d4d4", "description": "Foundations, methodology, and epistemology of science"},
    "engineering": {"icon": "⚙️", "color": "#78716c", "description": "Applied science, systems design, and technology"},
    "art-and-cognition": {"icon": "🎨", "color": "#f9a8d4", "description": "Aesthetics, creativity, and the cognitive basis of art"},
}

def load_yaml(p):
    try:
        return yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    except Exception:
        return {}

def get_domain_unknowns(domain):
    domain_dir = ROOT / "unknowns-catalog" / domain
    if not domain_dir.exists():
        return []
    entries = []
    for p in sorted(domain_dir.glob("u-*.yaml")):
        data = load_yaml(p)
        if data:
            entries.append({
                "id": data.get("id", p.stem),
                "title": data.get("title", p.stem),
                "status": data.get("status", "open"),
                "file": str(p.relative_to(ROOT))
            })
    return entries

def get_domain_bridges(domain: str) -> list:
    """Bridges whose `fields` match this catalog domain (uses cached index)."""
    global _BRIDGE_INDEX
    if _BRIDGE_INDEX is None:
        build_bridge_index()
    return _BRIDGE_INDEX.get(domain, [])

def get_domain_hypotheses(domain, unknowns):
    unknown_ids = {u["id"] for u in unknowns}
    hypotheses = []
    for p in sorted((ROOT / "hypotheses").rglob("h-*.yaml")):
        data = load_yaml(p)
        if not data:
            continue
        addressed = data.get("unknowns_addressed") or []
        related = data.get("related_disciplines") or []
        matched = any(uid in unknown_ids for uid in addressed)
        if not matched:
            matched = any(catalog_domain_matches_field_tag(domain, d) for d in related)
        if not matched:
            continue
        hypotheses.append({
            "id": data.get("id", p.stem),
            "title": data.get("title", p.stem),
            "status": data.get("status", "active"),
            "priority": data.get("priority", "medium"),
            "file": str(p.relative_to(ROOT)),
        })
    return hypotheses[:10]  # cap at 10

def generate_page(domain, unknowns, bridges, hypotheses, meta):
    icon = meta.get("icon", "🔬")
    color = meta.get("color", "#4f9cf9")
    description = meta.get("description", "")
    domain_title = domain.replace("-", " ").title()

    gh_base = "https://github.com/KR8ZYSHO3/Universal-Science-Discovery/blob/main"

    unknowns_html = "\n".join([
        f'''<div class="entry-card unknown-card">
          <span class="entry-badge">Unknown</span>
          <a href="{gh_base}/{u["file"]}" target="_blank" class="entry-title">{u["title"]}</a>
          <span class="entry-id">{u["id"]}</span>
        </div>'''
        for u in unknowns[:30]
    ])

    bridges_html = "\n".join([
        f'''<div class="entry-card bridge-card">
          <span class="entry-badge bridge-badge">Bridge</span>
          <a href="{gh_base}/{b["file"]}" target="_blank" class="entry-title">{b["title"]}</a>
          <p class="bridge-other">Fields: {b["fields_line"]}</p>
          {f'<p class="bridge-claim">{b["bridge_claim"]}...</p>' if b["bridge_claim"] else ""}
        </div>'''
        for b in bridges
    ])

    hyp_html = "\n".join([
        f'''<div class="entry-card hyp-card">
          <span class="entry-badge hyp-badge">Hypothesis</span>
          <a href="{gh_base}/{h["file"]}" target="_blank" class="entry-title">{h["title"]}</a>
          <span class="entry-priority priority-{h["priority"]}">{h["priority"]}</span>
        </div>'''
        for h in hypotheses
    ]) or "<p class='empty-state'>No linked hypotheses yet — <a href='../..'>contribute one</a>!</p>"

    og_desc = f"{len(unknowns)} open unknowns, {len(bridges)} cross-domain bridges in {domain_title}. {description}"
    tw_desc = f"{len(unknowns)} open questions in {domain_title} tracked by the Universal Science Discovery Repository."

    return f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{domain_title} — USDR</title>
  <meta name="description" content="Open unknowns in {domain_title}: {description}. Part of the Universal Science Discovery Repository.">
  <link rel="canonical" href="https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/domains/{domain}.html">

  <!-- OpenGraph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/domains/{domain}.html">
  <meta property="og:title" content="{domain_title} — Open Unknowns | USDR">
  <meta property="og:description" content="{og_desc}">
  <meta property="og:image" content="https://opengraph.githubassets.com/1/KR8ZYSHO3/Universal-Science-Discovery">
  <meta property="og:site_name" content="USDR">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{domain_title} Unknowns — USDR">
  <meta name="twitter:description" content="{tw_desc}">
  <meta name="twitter:image" content="https://opengraph.githubassets.com/1/KR8ZYSHO3/Universal-Science-Discovery">

  <link rel="stylesheet" href="../style.css" onerror="this.remove()">
  <style>
    :root {{ --bg: #060d1a; --card: #0d1b2e; --border: #1a2d4a; --text: #e2e8f0; --muted: #64748b; --accent: {color}; }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ background: var(--bg); color: var(--text); font-family: system-ui, sans-serif; min-height: 100vh; }}
    .hero {{ padding: 3rem 2rem 2rem; max-width: 900px; margin: 0 auto; }}
    .domain-icon {{ font-size: 3rem; margin-bottom: 1rem; }}
    .domain-title {{ font-size: 2.5rem; font-weight: 700; color: var(--accent); }}
    .domain-desc {{ color: var(--muted); margin-top: 0.5rem; font-size: 1.1rem; }}
    .stat-row {{ display: flex; gap: 2rem; margin-top: 1.5rem; flex-wrap: wrap; }}
    .stat {{ background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 1rem 1.5rem; }}
    .stat-n {{ font-size: 1.8rem; font-weight: 700; color: var(--accent); }}
    .stat-label {{ color: var(--muted); font-size: 0.85rem; }}
    .section {{ max-width: 900px; margin: 0 auto 2rem; padding: 0 2rem; }}
    .section-title {{ font-size: 1.25rem; font-weight: 600; border-bottom: 1px solid var(--border); padding-bottom: 0.5rem; margin-bottom: 1rem; }}
    .entry-card {{ background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 1rem; margin-bottom: 0.75rem; }}
    .entry-badge {{ font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.05em; padding: 0.2rem 0.5rem; border-radius: 4px; background: var(--accent); color: #000; font-weight: 600; }}
    .bridge-badge {{ background: #4f9cf9; }}
    .hyp-badge {{ background: #22d3b8; }}
    .entry-title {{ display: block; margin-top: 0.5rem; color: var(--text); text-decoration: none; font-weight: 500; }}
    .entry-title:hover {{ color: var(--accent); }}
    .entry-id {{ color: var(--muted); font-size: 0.75rem; font-family: monospace; }}
    .bridge-other {{ color: var(--muted); font-size: 0.85rem; margin-top: 0.25rem; }}
    .bridge-claim {{ color: var(--muted); font-size: 0.8rem; margin-top: 0.5rem; line-height: 1.4; }}
    .empty-state {{ color: var(--muted); }}
    .empty-state a {{ color: var(--accent); }}
    .nav {{ padding: 1rem 2rem; border-bottom: 1px solid var(--border); display: flex; align-items: center; gap: 1rem; }}
    .nav a {{ color: var(--muted); text-decoration: none; font-size: 0.9rem; }}
    .nav a:hover {{ color: var(--accent); }}
    .priority-high {{ color: #f43f5e; }}
    .priority-medium {{ color: #fbbf24; }}
    .priority-low {{ color: #4ade80; }}
  </style>
</head>
<body>
  <nav class="nav">
    <a href="../">← Dashboard</a>
    <span style="color:var(--border)">|</span>
    <a href="https://github.com/KR8ZYSHO3/Universal-Science-Discovery/tree/main/unknowns-catalog/{domain}">View on GitHub</a>
    <span style="color:var(--border)">|</span>
    <a href="https://github.com/KR8ZYSHO3/Universal-Science-Discovery/issues/new?labels=content:unknown&template=new-unknown.md">Add an Unknown</a>
  </nav>

  <div class="hero">
    <div class="domain-icon">{icon}</div>
    <h1 class="domain-title">{domain_title}</h1>
    <p class="domain-desc">{description}</p>
    <div class="stat-row">
      <div class="stat"><div class="stat-n">{len(unknowns)}</div><div class="stat-label">Open Unknowns</div></div>
      <div class="stat"><div class="stat-n">{len(bridges)}</div><div class="stat-label">Cross-Domain Bridges</div></div>
      <div class="stat"><div class="stat-n">{len(hypotheses)}</div><div class="stat-label">Active Hypotheses</div></div>
    </div>
  </div>

  {'<div class="section"><h2 class="section-title">Cross-Domain Bridges</h2>' + bridges_html + '</div>' if bridges_html else ''}

  <div class="section">
    <h2 class="section-title">Open Unknowns ({len(unknowns)}{'+'if len(unknowns)>=30 else ''})</h2>
    {unknowns_html}
    {'<p style="color:var(--muted);font-size:0.85rem;margin-top:0.5rem">Showing first 30 of ' + str(len(unknowns)) + ' unknowns.</p>' if len(unknowns) > 30 else ''}
  </div>

  <div class="section">
    <h2 class="section-title">Active Hypotheses</h2>
    {hyp_html}
  </div>

  <div class="section" style="margin-top:3rem;padding-bottom:3rem;border-top:1px solid var(--border);padding-top:2rem">
    <p style="color:var(--muted)">Know something about {domain_title}? <a href="https://github.com/KR8ZYSHO3/Universal-Science-Discovery/blob/main/CONTRIBUTING.md" style="color:var(--accent)">Contribute an unknown or hypothesis →</a></p>
    <p style="color:var(--muted);margin-top:0.5rem;font-size:0.85rem">Generated {date.today().isoformat()} · <a href="https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/" style="color:var(--accent)">USDR Dashboard</a></p>
  </div>
</body>
</html>'''

def main():
    global _BRIDGE_INDEX
    parser = argparse.ArgumentParser()
    parser.add_argument("--domain", type=str, default=None, help="Generate for a single domain")
    args = parser.parse_args()

    DOMAINS_DIR.mkdir(parents=True, exist_ok=True)

    domains = [d.name for d in (ROOT / "unknowns-catalog").iterdir() if d.is_dir()]
    if args.domain:
        domains = [args.domain]

    _BRIDGE_INDEX = None
    build_bridge_index()

    generated = []
    for domain in sorted(domains):
        unknowns = get_domain_unknowns(domain)
        if not unknowns:
            continue
        bridges = get_domain_bridges(domain)
        hypotheses = get_domain_hypotheses(domain, unknowns)
        meta = DOMAIN_META.get(domain, {"icon": "🔬", "color": "#4f9cf9", "description": ""})

        html = generate_page(domain, unknowns, bridges, hypotheses, meta)
        out = DOMAINS_DIR / f"{domain}.html"
        out.write_text(html, encoding="utf-8")
        generated.append((domain, len(unknowns), len(bridges)))
        print(f"Generated {out.name} ({len(unknowns)} unknowns, {len(bridges)} bridges)")

    unique_bridge_files = sum(1 for _ in (ROOT / "cross-domain").rglob("b-*.yaml"))
    generate_index(generated, unique_bridge_files)
    print(f"\nGenerated {len(generated)} domain pages + index")

def generate_index(domains_data, unique_bridge_yaml: int):
    cards = "\n".join([
        f'''<a href="{domain}.html" class="domain-card" style="--dc:{DOMAIN_META.get(domain, {}).get("color", "#4f9cf9")}">
          <span class="dc-icon">{DOMAIN_META.get(domain, {}).get("icon", "🔬")}</span>
          <h3>{domain.replace("-", " ").title()}</h3>
          <p>{unknowns} unknowns · {bridges} bridges</p>
        </a>'''
        for domain, unknowns, bridges in sorted(domains_data, key=lambda x: -x[1])
    ])

    total_unknowns = sum(u for _, u, _ in domains_data)
    index_html = f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Domains — USDR</title>
  <meta name="description" content="Browse {len(domains_data)} scientific disciplines in the Universal Science Discovery Repository. {total_unknowns}+ open unknowns; {unique_bridge_yaml}+ bridge records (domain cards count bridges touching each discipline — the same bridge may appear on multiple cards).">
  <link rel="canonical" href="https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/domains/">

  <!-- OpenGraph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/domains/">
  <meta property="og:title" content="Science Domains — USDR">
  <meta property="og:description" content="{len(domains_data)} disciplines · {total_unknowns}+ open unknowns · {unique_bridge_yaml}+ bridges in catalog. Domain cards list bridges whose fields touch that discipline.">
  <meta property="og:image" content="https://opengraph.githubassets.com/1/KR8ZYSHO3/Universal-Science-Discovery">
  <meta property="og:site_name" content="USDR">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Science Domains — USDR">
  <meta name="twitter:description" content="Browse {len(domains_data)} disciplines with {total_unknowns}+ open unknowns; {unique_bridge_yaml}+ bridges in catalog.">
  <meta name="twitter:image" content="https://opengraph.githubassets.com/1/KR8ZYSHO3/Universal-Science-Discovery">

  <style>
    :root {{ --bg: #060d1a; --card: #0d1b2e; --border: #1a2d4a; --text: #e2e8f0; --muted: #64748b; }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ background: var(--bg); color: var(--text); font-family: system-ui, sans-serif; padding: 2rem; }}
    h1 {{ font-size: 2rem; margin-bottom: 0.5rem; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 1rem; margin-top: 2rem; }}
    .domain-card {{ background: var(--card); border: 1px solid var(--dc, #1a2d4a); border-radius: 10px; padding: 1.5rem; text-decoration: none; color: var(--text); transition: 0.2s; display: block; }}
    .domain-card:hover {{ border-color: var(--dc); transform: translateY(-2px); }}
    .dc-icon {{ font-size: 2rem; display: block; margin-bottom: 0.5rem; }}
    .domain-card h3 {{ font-size: 1rem; color: var(--dc); margin-bottom: 0.25rem; }}
    .domain-card p {{ color: var(--muted); font-size: 0.8rem; }}
    nav a {{ color: var(--muted); text-decoration: none; margin-right: 1rem; }}
    nav {{ margin-bottom: 2rem; }}
  </style>
</head>
<body>
  <nav><a href="../">← Dashboard</a></nav>
  <h1>Browse by Domain</h1>
  <p style="color:var(--muted);margin-top:0.5rem">{len(domains_data)} disciplines · {unique_bridge_yaml} bridge YAML records · card counts are per-discipline matches (bridges can appear on multiple cards)</p>
  <div class="grid">{cards}</div>
</body>
</html>'''

    (DOMAINS_DIR / "index.html").write_text(index_html, encoding="utf-8")

if __name__ == "__main__":
    main()
