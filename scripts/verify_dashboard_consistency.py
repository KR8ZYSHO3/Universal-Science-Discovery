#!/usr/bin/env python3
"""
Fail if dashboard/index.html headline counts drift from the YAML catalog / graph JSON.

Checks id=snap-* and key stat-* divs against:
  - unknowns-catalog/**/u-*.yaml
  - hypotheses/**/*.yaml
  - cross-domain/**/b-*.yaml
  - phenomenology/**/p-*.yaml
  - docs/knowledge_graph.json node/edge totals (when JSON is present)

Usage:
  python scripts/verify_dashboard_consistency.py

Exit 0 if aligned; exit 1 with stderr details if not.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DASHBOARD = ROOT / "dashboard" / "index.html"
GRAPH_JSON = ROOT / "docs" / "knowledge_graph.json"


def count_globs(rel_patterns: list[str]) -> int:
    n = 0
    for pat in rel_patterns:
        n += len(list(ROOT.glob(pat)))
    return n


def catalog_counts() -> dict[str, int]:
    return {
        "bridges": count_globs(["cross-domain/**/b-*.yaml"]),
        "unknowns": count_globs(["unknowns-catalog/**/u-*.yaml"]),
        "hypotheses": count_globs(["hypotheses/**/*.yaml"]),
        "phenomena": count_globs(["phenomenology/**/p-*.yaml"]),
    }


def load_graph_totals() -> tuple[int | None, int | None]:
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


def parse_span_int(html: str, elem_id: str) -> int | None:
    m = re.search(rf'<span[^>]*\bid="{re.escape(elem_id)}"[^>]*>\s*([^<]+?)\s*</span>', html)
    if not m:
        return None
    inner = m.group(1).strip()
    if inner in ("—", "-", "…", "...") or not inner.isdigit():
        return None
    return int(inner)


def parse_stat_div_int(html: str, elem_id: str) -> int | None:
    m = re.search(rf'<div[^>]*\bid="{re.escape(elem_id)}"[^>]*>\s*(\d+)\s*</div>', html)
    if not m:
        return None
    return int(m.group(1))


def expect_match(errors: list[str], label: str, expected: int, actual: int | None) -> None:
    if actual is None:
        errors.append(f"{label}: could not parse integer from dashboard HTML")
        return
    if expected != actual:
        errors.append(f"{label}: catalog/graph={expected} but dashboard shows {actual}")


def main() -> int:
    if not DASHBOARD.exists():
        print(f"ERROR: missing {DASHBOARD}", file=sys.stderr)
        return 1

    html = DASHBOARD.read_text(encoding="utf-8")
    cat = catalog_counts()
    g_nodes, g_edges = load_graph_totals()
    errors: list[str] = []

    expect_match(errors, "snap-bridges", cat["bridges"], parse_span_int(html, "snap-bridges"))
    expect_match(errors, "stat-bridges", cat["bridges"], parse_stat_div_int(html, "stat-bridges"))
    expect_match(errors, "snap-unknowns", cat["unknowns"], parse_span_int(html, "snap-unknowns"))
    expect_match(errors, "stat-unk", cat["unknowns"], parse_stat_div_int(html, "stat-unk"))
    expect_match(errors, "snap-hypotheses", cat["hypotheses"], parse_span_int(html, "snap-hypotheses"))
    expect_match(errors, "stat-hyp", cat["hypotheses"], parse_stat_div_int(html, "stat-hyp"))
    expect_match(errors, "snap-phenomena", cat["phenomena"], parse_span_int(html, "snap-phenomena"))
    expect_match(errors, "stat-phenom", cat["phenomena"], parse_stat_div_int(html, "stat-phenom"))

    pill_m = re.search(r"(\d+)\s+cross-domain bridges", html)
    if pill_m:
        expect_match(errors, "hero pill (cross-domain bridges)", cat["bridges"], int(pill_m.group(1)))

    if g_nodes is not None:
        expect_match(errors, "snap-graph-nodes", g_nodes, parse_span_int(html, "snap-graph-nodes"))
    if g_edges is not None:
        expect_match(errors, "snap-graph-edges", g_edges, parse_span_int(html, "snap-graph-edges"))
        expect_match(errors, "stat-graph-edges", g_edges, parse_stat_div_int(html, "stat-graph-edges"))

    if errors:
        print("verify_dashboard_consistency: FAILED", file=sys.stderr)
        for line in errors:
            print(f"  - {line}", file=sys.stderr)
        print(
            "\nFix: rebuild docs/knowledge_graph.json if needed, then "
            "python scripts/update_dashboard_stats.py --apply",
            file=sys.stderr,
        )
        return 1

    ok_tail = ""
    if g_nodes is not None and g_edges is not None:
        ok_tail = f", graph_nodes={g_nodes}, graph_edges={g_edges}"
    else:
        ok_tail = " (graph JSON absent — skipped node/edge checks)"
    print(
        "verify_dashboard_consistency: OK "
        f"(bridges={cat['bridges']}, unknowns={cat['unknowns']}, "
        f"hypotheses={cat['hypotheses']}, phenomena={cat['phenomena']}"
        f"{ok_tail})",
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
