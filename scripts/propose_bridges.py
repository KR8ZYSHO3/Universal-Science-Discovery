#!/usr/bin/env python3
"""
USDR Bridge Proposer — finds domain pairs with high unknown density but few bridges.
Surfaces candidate cross-domain connections for human review.

Domain assignment strategy:
  1. Use node["fields"] array (first element) if non-empty.
  2. Fall back to unknowns-catalog/<domain>/u-*.yaml directory name.
  3. Final fallback: parse last segment of the node id before the first
     recognisable keyword.

Usage:
    python scripts/propose_bridges.py [--top N] [--min-unknowns M] [--output PATH]
"""
import json
import argparse
from pathlib import Path
from collections import defaultdict
from itertools import combinations

ROOT = Path(__file__).parent.parent


def _catalog_domain_map() -> dict[str, str]:
    """Return {node_id: domain} from unknowns-catalog directory structure."""
    mapping: dict[str, str] = {}
    catalog = ROOT / "unknowns-catalog"
    if catalog.exists():
        for yaml_file in catalog.rglob("u-*.yaml"):
            domain = yaml_file.parent.name  # e.g. "astronomy", "biology"
            node_id = yaml_file.stem        # e.g. "u-baryon-asymmetry-origin"
            mapping[node_id] = domain
    return mapping


def _domain_for_node(node: dict, catalog_map: dict[str, str]) -> str:
    """Return the best domain string for a node."""
    fields = node.get("fields") or []
    if isinstance(fields, list) and fields:
        return fields[0]
    nid = node.get("id", "")
    if nid in catalog_map:
        return catalog_map[nid]
    # Generic fallback: second segment of id (u-<domain>-... or b-<domain>-...)
    parts = nid.split("-")
    return parts[1] if len(parts) > 1 else "general"


def main() -> list[dict]:
    parser = argparse.ArgumentParser(description="Propose novel cross-domain bridges")
    parser.add_argument("--top", type=int, default=10, help="Number of candidates to show")
    parser.add_argument("--min-unknowns", type=int, default=3,
                        help="Min unknowns per domain to consider")
    parser.add_argument("--output", type=str, default=None, help="Output JSON file path")
    args = parser.parse_args()

    graph_path = ROOT / "docs" / "knowledge_graph.json"
    data = json.loads(graph_path.read_text(encoding="utf-8"))
    nodes: list[dict] = data["nodes"]
    edges: list[dict] = data["edges"]

    catalog_map = _catalog_domain_map()

    # Group nodes by domain and type
    domain_unknowns: dict[str, list[str]] = defaultdict(list)
    domain_bridges: dict[str, list[str]] = defaultdict(list)

    for node in nodes:
        ntype = node.get("type", "")
        domain = _domain_for_node(node, catalog_map)
        if ntype == "unknown":
            domain_unknowns[domain].append(node["id"])
        elif ntype == "bridge":
            domain_bridges[domain].append(node["id"])

    # Collect domain pairs that already have a bridge linking them
    bridged_pairs: set[frozenset] = set()
    for node in nodes:
        if node.get("type") == "bridge":
            fields = node.get("fields") or []
            if isinstance(fields, list) and len(fields) >= 2:
                for d1, d2 in combinations(fields, 2):
                    bridged_pairs.add(frozenset([d1, d2]))
            # Also parse "↔" in title as a secondary heuristic
            title = node.get("title", "")
            if "↔" in title:
                parts = title.split("↔")
                if len(parts) == 2:
                    d1 = parts[0].strip().lower().split()[-1]
                    d2 = parts[1].strip().lower().split()[0]
                    bridged_pairs.add(frozenset([d1, d2]))

    # Score domain pairs
    qualified = [d for d, uns in domain_unknowns.items()
                 if len(uns) >= args.min_unknowns and d]

    candidates: list[dict] = []
    for d1, d2 in combinations(qualified, 2):
        pair = frozenset([d1, d2])
        unknown_score = len(domain_unknowns[d1]) + len(domain_unknowns[d2])
        bridge_penalty = 20 if pair in bridged_pairs else 0
        score = unknown_score - bridge_penalty

        candidates.append({
            "domain_1": d1,
            "domain_2": d2,
            "unknowns_d1": len(domain_unknowns[d1]),
            "unknowns_d2": len(domain_unknowns[d2]),
            "total_unknown_score": unknown_score,
            "existing_bridges": 1 if pair in bridged_pairs else 0,
            "novelty_score": score,
            "sample_unknowns_d1": domain_unknowns[d1][:3],
            "sample_unknowns_d2": domain_unknowns[d2][:3],
        })

    candidates.sort(key=lambda x: x["novelty_score"], reverse=True)
    top = candidates[:args.top]

    print(f"\n{'='*60}")
    print(f"USDR Bridge Proposer — Top {args.top} Novel Connection Candidates")
    print(f"{'='*60}\n")

    for i, c in enumerate(top, 1):
        print(f"{i}. {c['domain_1']} <-> {c['domain_2']}")
        print(f"   Unknowns: {c['unknowns_d1']} + {c['unknowns_d2']} = {c['total_unknown_score']}")
        print(f"   Existing bridges: {c['existing_bridges']}  |  Novelty score: {c['novelty_score']}")
        print(f"   Sample unknowns ({c['domain_1']}): {', '.join(c['sample_unknowns_d1'])}")
        print(f"   Sample unknowns ({c['domain_2']}): {', '.join(c['sample_unknowns_d2'])}")
        print()

    print(f"Total domain pairs evaluated: {len(candidates)}")

    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            json.dumps(
                {"candidates": top, "total_pairs_evaluated": len(candidates)},
                indent=2,
            ),
            encoding="utf-8",
        )
        print(f"Results written to {out}")

    return top


if __name__ == "__main__":
    main()
