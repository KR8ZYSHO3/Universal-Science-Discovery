#!/usr/bin/env python3
"""
Auto-update dashboard/index.html stat counts from actual catalog file counts.

Targets:
  - id="stat-hyp"   — hypotheses count
  - id="stat-unk"   — unknowns count
  - id="stat-bridges" — cross-domain bridges count
  - id="stat-phenom"  — phenomenology entries count
  - id="stat-graph-edges" — edge count from docs/knowledge_graph.json meta (if present)
  - id="kg-node-count" / id="kg-edge-count" — placeholders until JS loads the graph
  - Hero snapshot spans id="snap-bridges", snap-unknowns, snap-hypotheses, snap-phenomena,
    snap-graph-nodes, snap-graph-edges (between HTML markers DASHBOARD_CATALOG_SNAPSHOT_*)
  - pill text "N cross-domain bridges"
  - pill text "N unknowns · N hypotheses · N pre-formal observation"
  - OpenGraph / Twitter meta descriptions (bridges, unknowns, graph nodes)

Run by GitHub Actions after every merge to main (after build_graph regenerates JSON).
Usage:
  python scripts/update_dashboard_stats.py           # dry-run (print counts only)
  python scripts/update_dashboard_stats.py --apply   # write changes to dashboard/index.html
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
GRAPH_JSON = ROOT / "docs" / "knowledge_graph.json"


def count_files(pattern: str) -> int:
    return len(list(ROOT.glob(pattern)))


def replace_stat_id(html: str, stat_id: str, new_value: int) -> str:
    """Replace the number inside <div ... id="stat-id">NUMBER</div>."""
    pattern = rf'(<div[^>]*\bid="{re.escape(stat_id)}"[^>]*>)\d+(</div>)'
    replacement = rf'\g<1>{new_value}\2'
    result, n = re.subn(pattern, replacement, html)
    if n == 0:
        print(f"  WARNING: stat id '{stat_id}' not found in HTML", file=sys.stderr)
    return result


def replace_pill_bridges(html: str, new_value: int) -> str:
    """Replace 'N[+] cross-domain bridges' in pill text (handles trailing + suffix)."""
    pattern = r'\d+\+? cross-domain bridges'
    result, n = re.subn(pattern, rf'{new_value} cross-domain bridges', html)
    if n == 0:
        print("  WARNING: pill 'cross-domain bridges' not found in HTML", file=sys.stderr)
    return result


def load_graph_meta() -> tuple[int | None, int | None]:
    """Return (node_count, edge_count) from built knowledge graph, or (None, None).

    Prefers meta.node_count / meta.edge_count; falls back to len(nodes)/len(edges).
    """
    if not GRAPH_JSON.exists():
        return None, None
    try:
        data = json.loads(GRAPH_JSON.read_text(encoding="utf-8"))
        meta = data.get("meta") or {}
        nc = meta.get("node_count")
        ec = meta.get("edge_count")
        if isinstance(nc, int) and isinstance(ec, int):
            return nc, ec
        nodes = data.get("nodes")
        edges = data.get("edges")
        if isinstance(nodes, list) and isinstance(edges, list):
            return len(nodes), len(edges)
    except (OSError, json.JSONDecodeError, TypeError):
        pass
    return None, None


def replace_span_id(html: str, elem_id: str, new_value: int) -> str:
    """Replace integer inside <span id=\"...\">NUMBER</span>."""
    pattern = rf'(<span[^>]*\bid="{re.escape(elem_id)}"[^>]*>)\d+(</span>)'
    replacement = rf"\g<1>{new_value}\2"
    result, n = re.subn(pattern, replacement, html)
    if n == 0:
        print(f"  WARNING: span id '{elem_id}' not found in HTML", file=sys.stderr)
    return result


def patch_catalog_snapshot_spans(
    html: str,
    bridges: int,
    unknowns: int,
    hypotheses: int,
    phenomena: int,
    graph_nodes: int | None,
    graph_edges: int | None,
) -> str:
    """Update hero catalog snapshot counts (see DASHBOARD_CATALOG_SNAPSHOT_* markers)."""
    html = replace_span_id(html, "snap-bridges", bridges)
    html = replace_span_id(html, "snap-unknowns", unknowns)
    html = replace_span_id(html, "snap-hypotheses", hypotheses)
    html = replace_span_id(html, "snap-phenomena", phenomena)
    if graph_nodes is not None and graph_edges is not None:
        html = replace_span_id(html, "snap-graph-nodes", graph_nodes)
        html = replace_span_id(html, "snap-graph-edges", graph_edges)
    else:
        loose = rf'(<span[^>]*\bid="{re.escape("snap-graph-nodes")}"[^>]*>)[^<]*(</span>)'
        html, _ = re.subn(loose, r"\g<1>—\2", html)
        loose2 = rf'(<span[^>]*\bid="{re.escape("snap-graph-edges")}"[^>]*>)[^<]*(</span>)'
        html, _ = re.subn(loose2, r"\g<1>—\2", html)
    return html


def replace_og_descriptions(
    html: str,
    bridges: int,
    unknowns: int,
    nodes: int,
) -> str:
    """Sync social preview strings with headline catalog stats."""
    og_simple = (
        f'content="A version-controlled, AI-augmented knowledge engine tracking what humanity doesn\'t yet know. '
        f"{bridges} cross-domain bridges &#9658; {unknowns} open unknowns &#9658; "
        f'{nodes} knowledge graph nodes &#9658; Open source."'
    )
    html2, n1 = re.subn(
        r'<meta property="og:description" content="[^"]*"\s*>',
        f'<meta property="og:description" {og_simple} >',
        html,
        count=1,
    )
    tw_pat = r'<meta name="twitter:description" content="[^"]*"\s*>'
    tw_new = (
        f'<meta name="twitter:description" content="Map the unknowns. Accelerate discovery. '
        f'{bridges} cross-domain bridges, {unknowns} open unknowns, {nodes} knowledge graph nodes. '
        f'All open source.">'
    )
    html3, n2 = re.subn(tw_pat, tw_new, html2, count=1)
    if n1 == 0:
        print("  WARNING: og:description meta not updated", file=sys.stderr)
    if n2 == 0:
        print("  WARNING: twitter:description meta not updated", file=sys.stderr)
    return html3


def replace_api_unknowns_blurb(html: str, unknowns: int) -> str:
    """Fix 'All N open unknowns...' API endpoint description."""
    pattern = r"All \d+ open unknowns with domain"
    result, n = re.subn(pattern, f"All {unknowns} open unknowns with domain", html, count=1)
    if n == 0:
        print("  WARNING: unknowns API blurb not found", file=sys.stderr)
    return result


def replace_api_hypothesis_blurb(html: str, hypotheses: int) -> str:
    """Fix 'All N hypotheses...' API endpoint description."""
    pattern = r"All \d+ hypotheses with priority"
    result, n = re.subn(pattern, f"All {hypotheses} hypotheses with priority", html, count=1)
    if n == 0:
        print("  WARNING: hypotheses API blurb not found", file=sys.stderr)
    return result


def replace_api_graph_blurb(html: str, nodes: int, edges: int) -> str:
    """Fix graph.json endpoint description."""
    pattern = (
        r'(<code>GET /api/v1/graph\.json</code>\s*\n\s*<span>)'
        r'Full knowledge graph — [^<]+</span>'
    )
    repl = (
        rf"\g<1>Full knowledge graph — {nodes} nodes, {edges} edges "
        r"(built from catalog YAML; mirrors docs/knowledge_graph.json)</span>"
    )
    result, n = re.subn(pattern, repl, html)
    if n == 0:
        print("  WARNING: graph API blurb not found", file=sys.stderr)
    return result


def replace_graph_section_desc(html: str) -> str:
    """Remove stale fixed node count from knowledge graph intro paragraph (one-time migration)."""
    pattern = (
        r'Force-directed graph of all \d+ nodes — bridges, unknowns, hypotheses, and phenomena\.'
    )
    repl = (
        "Force-directed graph of the full catalog — bridges, unknowns, hypotheses, and phenomena "
        "(counts update live when the JSON loads)."
    )
    result, n = re.subn(pattern, repl, html)
    return result


def _fmt_commas(n: int) -> str:
    return f"{n:,}"


def replace_hero_prose(
    html: str,
    bridges: int,
    unknowns: int,
    hypotheses: int,
    graph_nodes: int,
) -> str:
    """Sync comma-formatted hero banner, pills, and lead paragraph with catalog counts."""
    banner_pat = (
        r'(<span style="font-size:\.82rem;opacity:\.95">)'
        r'[\d,]+ cross-domain bridges • [\d,]+ open unknowns • [\d,]+ hypotheses • '
        r'[\d,]+-node graph • 0 orphans • Live Wave Factory automation\. Git-native for auditability\.'
        r'(</span>)'
    )
    banner_repl = (
        rf"\g<1>{_fmt_commas(bridges)} cross-domain bridges • {_fmt_commas(unknowns)} open unknowns • "
        rf"{_fmt_commas(hypotheses)} hypotheses • {_fmt_commas(graph_nodes)}-node graph • "
        r"0 orphans • Live Wave Factory automation. Git-native for auditability.\g<2>"
    )
    html, n1 = re.subn(banner_pat, banner_repl, html, count=1)

    pill_bridges_pat = r'(<span class="pill">)[\d,]+ cross-domain bridges(</span>)'
    html, _ = re.subn(pill_bridges_pat, rf"\g<1>{_fmt_commas(bridges)} cross-domain bridges\g<2>", html, count=1)

    pill_unk_hyp_pat = (
        r'(<span class="pill">)[\d,]+ open unknowns • [\d,]+ hypotheses • 0 orphans(</span>)'
    )
    html, _ = re.subn(
        pill_unk_hyp_pat,
        rf"\g<1>{_fmt_commas(unknowns)} open unknowns • {_fmt_commas(hypotheses)} hypotheses • 0 orphans\g<2>",
        html,
        count=1,
    )

    pill_graph_pat = r'(<span class="pill">)[\d,]+-node graph • Live automation • Git-native(</span>)'
    html, _ = re.subn(
        pill_graph_pat,
        rf"\g<1>{_fmt_commas(graph_nodes)}-node graph • Live automation • Git-native\g<2>",
        html,
        count=1,
    )

    lead_pat = (
        r'A git-native, schema-validated catalog of [\d,]+ open research problems, '
        r'[\d,]+ falsifiable hypotheses, and [\d,]+ cross-domain mathematical bridges — '
        r'all connected in a reproducible [\d,]+-node knowledge graph\.'
    )
    lead_repl = (
        f"A git-native, schema-validated catalog of {_fmt_commas(unknowns)} open research problems, "
        f"{_fmt_commas(hypotheses)} falsifiable hypotheses, and {_fmt_commas(bridges)} cross-domain "
        f"mathematical bridges — all connected in a reproducible {_fmt_commas(graph_nodes)}-node knowledge graph."
    )
    html, n2 = re.subn(lead_pat, lead_repl, html, count=1)

    if n1 == 0:
        print("  WARNING: launch banner summary not found in HTML", file=sys.stderr)
    if n2 == 0:
        print("  WARNING: hero-lead prose not found in HTML", file=sys.stderr)
    return html


def replace_pill_summary(html: str, unknowns: int, hypotheses: int, phenomena: int) -> str:
    """Replace 'N unknowns · N hypotheses · N pre-formal observation' in pill text."""
    # Match the pattern with any Unicode separator between numbers
    pattern = r'\d+ unknowns[^<]*\d+ hypotheses[^<]*\d+ pre-formal observation'
    new_text = f'{unknowns} unknowns \u00b7 {hypotheses} hypotheses \u00b7 {phenomena} pre-formal observation'
    result, n = re.subn(pattern, new_text, html)
    if n == 0:
        print("  WARNING: pill summary line not found in HTML", file=sys.stderr)
    return result


def main() -> None:
    apply = "--apply" in sys.argv

    unknowns = count_files("unknowns-catalog/**/u-*.yaml")
    hypotheses = count_files("hypotheses/**/*.yaml")
    bridges = count_files("cross-domain/**/b-*.yaml")
    phenomena = count_files("phenomenology/**/p-*.yaml")
    total = unknowns + hypotheses + bridges + phenomena

    print(f"Catalog counts:")
    print(f"  unknowns   = {unknowns}")
    print(f"  hypotheses = {hypotheses}")
    print(f"  bridges    = {bridges}")
    print(f"  phenomena  = {phenomena}")
    print(f"  total      = {total}")

    dashboard = ROOT / "dashboard" / "index.html"
    if not dashboard.exists():
        print(f"ERROR: {dashboard} not found", file=sys.stderr)
        sys.exit(1)

    html = dashboard.read_text(encoding="utf-8")
    original = html

    html = replace_stat_id(html, "stat-unk", unknowns)
    html = replace_stat_id(html, "stat-hyp", hypotheses)
    html = replace_stat_id(html, "stat-bridges", bridges)
    html = replace_stat_id(html, "stat-phenom", phenomena)
    html = replace_pill_bridges(html, bridges)
    html = replace_pill_summary(html, unknowns, hypotheses, phenomena)

    g_nodes, g_edges = load_graph_meta()
    html = patch_catalog_snapshot_spans(
        html, bridges, unknowns, hypotheses, phenomena, g_nodes, g_edges
    )
    if g_nodes is not None and g_edges is not None:
        print(f"  graph meta: nodes={g_nodes}, edges={g_edges}")
        html = replace_stat_id(html, "stat-graph-edges", g_edges)
        html = replace_span_id(html, "kg-node-count", g_nodes)
        html = replace_span_id(html, "kg-edge-count", g_edges)
        html = replace_og_descriptions(html, bridges, unknowns, g_nodes)
        html = replace_api_unknowns_blurb(html, unknowns)
        html = replace_api_hypothesis_blurb(html, hypotheses)
        html = replace_api_graph_blurb(html, g_nodes, g_edges)
        html = replace_graph_section_desc(html)
        html = replace_hero_prose(html, bridges, unknowns, hypotheses, g_nodes)
    else:
        print(
            "  NOTE: docs/knowledge_graph.json missing or unreadable — "
            "graph-derived patches skipped (snapshot graph spans set to em dash)",
            file=sys.stderr,
        )

    if html == original:
        print("\nNo changes needed — dashboard is already up to date.")
        return

    if apply:
        dashboard.write_text(html, encoding="utf-8")
        print(f"\nApplied: updated {dashboard}")
    else:
        print("\nDry-run: pass --apply to write changes to dashboard/index.html")


if __name__ == "__main__":
    main()
