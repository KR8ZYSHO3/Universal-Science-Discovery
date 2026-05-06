#!/usr/bin/env python3
"""Build a knowledge graph from USDR YAML catalog entries.

Walks cross-domain/b-*.yaml, hypotheses/active/h-*.yaml,
unknowns-catalog/**/u-*.yaml, phenomenology/**/p-*.yaml,
pioneers/pioneer-*.yaml, and breakthrough-gaps/bg-*.yaml.
Outputs docs/knowledge_graph.json.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "knowledge_graph.json"

# Cross-reference field names and their relation label
EDGE_FIELDS: list[tuple[str, str]] = [
    ("related_unknowns",      "related_unknown"),
    ("related_hypotheses",    "related_hypothesis"),
    ("related_bridges",       "related_bridge"),
    ("suggested_hypotheses",  "suggested_hypothesis"),
    ("candidate_bridges",     "candidate_bridge"),
    ("candidate_unknowns",    "candidate_unknown"),
    ("unknowns_addressed",    "addresses_unknown"),
    ("evidence_links",        "evidence_link"),
    ("bridge_seeds",          "seeds_bridge"),
    ("required_bridges",      "requires_bridge"),
]


def load_yaml(path: Path) -> dict | None:
    try:
        with path.open(encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        if isinstance(data, dict):
            return data
    except Exception as exc:  # noqa: BLE001
        print(f"  WARNING: could not parse {path.relative_to(ROOT)}: {exc}", file=sys.stderr)
    return None


def iter_yaml_files():
    """Yield (path, entry_type) for all catalog YAML files."""
    for path in sorted((ROOT / "cross-domain").rglob("b-*.yaml")):
        yield path, "bridge"
    for path in sorted((ROOT / "hypotheses" / "active").glob("h-*.yaml")):
        yield path, "hypothesis"
    for path in sorted((ROOT / "unknowns-catalog").rglob("u-*.yaml")):
        yield path, "unknown"
    for path in sorted((ROOT / "phenomenology").rglob("p-*.yaml")):
        yield path, "phenomenon"
    pioneer_dir = ROOT / "pioneers"
    if pioneer_dir.exists():
        for path in sorted(pioneer_dir.glob("pioneer-*.yaml")):
            yield path, "pioneer"
    bg_dir = ROOT / "breakthrough-gaps"
    if bg_dir.exists():
        for path in sorted(bg_dir.glob("bg-*.yaml")):
            yield path, "breakthrough_gap"


def extract_ref_ids(field_value: list | None) -> list[str]:
    """Extract string IDs from a reference field.

    Handles plain string lists and evidence_links dicts (which have no top-level id).
    """
    if not field_value:
        return []
    ids: list[str] = []
    for item in field_value:
        if isinstance(item, str):
            ids.append(item.strip())
        elif isinstance(item, dict):
            # evidence_links items have no id but have doi/arxiv/url;
            # skip them as graph targets since they don't correspond to catalog nodes.
            pass
    return [i for i in ids if i]


def build_graph() -> tuple[list[dict], list[dict]]:
    nodes: list[dict] = []
    edges: list[dict] = []
    seen_edges: set[tuple[str, str, str]] = set()

    for path, entry_type in iter_yaml_files():
        data = load_yaml(path)
        if data is None:
            continue

        entry_id = data.get("id", "")
        if not entry_id:
            print(f"  WARNING: missing id in {path.relative_to(ROOT)}", file=sys.stderr)
            continue

        # Build node
        node: dict = {
            "id": entry_id,
            "type": entry_type,
            "title": data.get("title", ""),
            "status": data.get("status", ""),
        }

        if entry_type == "bridge":
            node["fields"] = data.get("fields", [])
            node["color"] = "blue"
        elif entry_type in ("unknown", "phenomenon"):
            node["fields"] = data.get("disciplines", [])
            node["color"] = "gray"
        elif entry_type == "hypothesis":
            node["fields"] = data.get("related_disciplines", [])
            node["color"] = "green"
        elif entry_type == "pioneer":
            node["title"] = data.get("name", "")
            node["fields"] = data.get("primary_domains", [])
            node["color"] = "gold"
        elif entry_type == "breakthrough_gap":
            node["fields"] = [data.get("source_domain", "")]
            node["color"] = "red"

        nodes.append(node)

        # Build edges from cross-reference fields
        for field_name, relation in EDGE_FIELDS:
            targets = extract_ref_ids(data.get(field_name))
            for target_id in targets:
                key = (entry_id, target_id, relation)
                if key not in seen_edges:
                    seen_edges.add(key)
                    edges.append({
                        "source": entry_id,
                        "target": target_id,
                        "relation": relation,
                    })

    # Filter out orphan edges (endpoints not present in node set)
    node_ids = {n["id"] for n in nodes}
    valid_edges: list[dict] = []
    orphan_count = 0
    for edge in edges:
        if edge["source"] in node_ids and edge["target"] in node_ids:
            valid_edges.append(edge)
        else:
            orphan_count += 1
    if orphan_count:
        print(
            f"WARNING: filtered {orphan_count} orphan edge(s) "
            "(endpoints not in node set)",
            file=sys.stderr,
        )
    edges = valid_edges

    return nodes, edges


def top_nodes_by_degree(
    nodes: list[dict],
    edges: list[dict],
    n: int = 5,
) -> list[tuple[str, int]]:
    degree: dict[str, int] = defaultdict(int)
    for edge in edges:
        degree[edge["source"]] += 1
        degree[edge["target"]] += 1
    # Restrict to nodes that actually exist in our node set
    node_ids = {node["id"] for node in nodes}
    ranked = sorted(
        [(nid, cnt) for nid, cnt in degree.items() if nid in node_ids],
        key=lambda x: x[1],
        reverse=True,
    )
    return ranked[:n]


def main() -> int:
    print("Building USDR knowledge graph…")
    nodes, edges = build_graph()

    meta = {
        "generated": str(date.today()),
        "node_count": len(nodes),
        "edge_count": len(edges),
    }

    graph = {"nodes": nodes, "edges": edges, "meta": meta}

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8") as fh:
        json.dump(graph, fh, indent=2, ensure_ascii=False)

    print(f"\nGraph written to {OUTPUT.relative_to(ROOT)}")
    print(f"  Nodes : {len(nodes)}")
    print(f"  Edges : {len(edges)}")

    top = top_nodes_by_degree(nodes, edges)
    print("\nTop 5 most-connected nodes (by degree):")
    for rank, (nid, deg) in enumerate(top, 1):
        title = next((n["title"] for n in nodes if n["id"] == nid), "")
        short_title = (title[:70] + "…") if len(title) > 70 else title
        print(f"  {rank}. {nid}  (degree={deg})  {short_title}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
