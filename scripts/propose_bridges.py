#!/usr/bin/env python3
"""
USDR Bridge Proposer - finds novel cross-domain bridge candidates.

Sources proposals from three signals, each with a priority tier:
  1. pioneer_seed    (CRITICAL) — bridge_seeds listed in pioneers/ not yet in cross-domain/
  2. breakthrough_gap (HIGH)   — required_bridges in breakthrough-gaps/ not yet in cross-domain/
  3. domain_gap      (NORMAL)  — domain pairs with high unknown density but few bridges

Usage:
    python scripts/propose_bridges.py [--top N] [--min-unknowns M]
                                      [--output PATH] [--draft-yaml]
"""
import json
import argparse
from pathlib import Path
from collections import defaultdict
from itertools import combinations

try:
    import yaml
    _YAML_OK = True
except ImportError:
    _YAML_OK = False

ROOT = Path(__file__).parent.parent


# ── helpers ─────────────────────────────────────────────────────────────────

def _yaml_load(path: Path) -> dict:
    if _YAML_OK:
        return yaml.safe_load(path.read_text(encoding="utf-8", errors="replace")) or {}
    import re
    text = path.read_text(encoding="utf-8", errors="replace")
    # minimal fallback for key: value lines only
    return {}


def _existing_bridge_ids() -> set[str]:
    """Return the set of all bridge IDs already present in cross-domain/."""
    ids: set[str] = set()
    for p in (ROOT / "cross-domain").rglob("b-*.yaml"):
        # fast heuristic: stem = id (almost always true)
        ids.add(p.stem)
        # verify via YAML id field when yaml is available
        try:
            d = _yaml_load(p)
            if d.get("id"):
                ids.add(d["id"])
        except Exception:
            pass
    return ids


# ── pioneer seeds ────────────────────────────────────────────────────────────

def _pioneer_proposals(existing: set[str]) -> list[dict]:
    """Return high-priority proposals from pioneer bridge_seeds not yet in cross-domain/."""
    proposals: list[dict] = []
    pioneers_dir = ROOT / "pioneers"
    if not pioneers_dir.exists():
        return proposals
    for p in pioneers_dir.glob("pioneer-*.yaml"):
        try:
            d = _yaml_load(p)
        except Exception:
            continue
        pioneer_id = d.get("id", p.stem)
        pioneer_name = d.get("name", pioneer_id)
        for seed in d.get("bridge_seeds", []):
            seed = seed.strip()
            if not seed:
                continue
            proposals.append({
                "bridge_id": seed,
                "priority": "critical",
                "source": "pioneer_seed",
                "source_detail": f"pioneer:{pioneer_id}",
                "source_name": pioneer_name,
                "exists": seed in existing,
                "description": (
                    f"Bridge seed from {pioneer_name} — "
                    f"listed in {p.name} as a bridge this pioneer's work seeds."
                ),
            })
    return proposals


# ── breakthrough gap required bridges ────────────────────────────────────────

def _breakthrough_gap_proposals(existing: set[str]) -> list[dict]:
    """Return proposals from breakthrough-gaps/ required_bridges not yet in cross-domain/."""
    proposals: list[dict] = []
    gaps_dir = ROOT / "breakthrough-gaps"
    if not gaps_dir.exists():
        return proposals
    for p in gaps_dir.glob("bg-*.yaml"):
        try:
            d = _yaml_load(p)
        except Exception:
            continue
        gap_id = d.get("id", p.stem)
        gap_title = d.get("title", gap_id)
        potential = d.get("world_reshaping_potential", "")
        # priority: critical if potential=transformative, else high
        priority = "critical" if potential == "transformative" else "high"
        for bridge in d.get("required_bridges", []):
            bridge = bridge.strip()
            if not bridge:
                continue
            proposals.append({
                "bridge_id": bridge,
                "priority": priority,
                "source": "breakthrough_gap",
                "source_detail": f"breakthrough_gap:{gap_id}",
                "source_name": gap_title,
                "exists": bridge in existing,
                "description": (
                    f"Required bridge for breakthrough gap '{gap_title}' "
                    f"(world-reshaping potential: {potential or 'unspecified'})."
                ),
            })
    return proposals


# ── domain gap proposals ─────────────────────────────────────────────────────

def _catalog_domain_map() -> dict[str, str]:
    mapping: dict[str, str] = {}
    catalog = ROOT / "unknowns-catalog"
    if catalog.exists():
        for yaml_file in catalog.rglob("u-*.yaml"):
            domain = yaml_file.parent.name
            node_id = yaml_file.stem
            mapping[node_id] = domain
    return mapping


def _domain_for_node(node: dict, catalog_map: dict[str, str]) -> str:
    fields = node.get("fields") or []
    if isinstance(fields, list) and fields:
        return fields[0]
    nid = node.get("id", "")
    if nid in catalog_map:
        return catalog_map[nid]
    parts = nid.split("-")
    return parts[1] if len(parts) > 1 else "general"


def _domain_gap_proposals(top_n: int, min_unknowns: int) -> list[dict]:
    graph_path = ROOT / "docs" / "knowledge_graph.json"
    if not graph_path.exists():
        print(f"  [warn] knowledge_graph.json not found — skipping domain-gap proposals")
        return []
    data = json.loads(graph_path.read_text(encoding="utf-8"))
    nodes: list[dict] = data["nodes"]

    catalog_map = _catalog_domain_map()
    domain_unknowns: dict[str, list[str]] = defaultdict(list)
    bridged_pairs: set[frozenset] = set()

    for node in nodes:
        ntype = node.get("type", "")
        domain = _domain_for_node(node, catalog_map)
        if ntype == "unknown":
            domain_unknowns[domain].append(node["id"])
        elif ntype == "bridge":
            fields = node.get("fields") or []
            if isinstance(fields, list) and len(fields) >= 2:
                for d1, d2 in combinations(fields, 2):
                    bridged_pairs.add(frozenset([d1, d2]))

    qualified = [d for d, uns in domain_unknowns.items()
                 if len(uns) >= min_unknowns and d]

    candidates: list[dict] = []
    for d1, d2 in combinations(qualified, 2):
        pair = frozenset([d1, d2])
        unknown_score = len(domain_unknowns[d1]) + len(domain_unknowns[d2])
        bridge_penalty = 20 if pair in bridged_pairs else 0
        score = unknown_score - bridge_penalty
        slug = f"b-{d1}-{d2}".replace(" ", "-").lower()
        candidates.append({
            "bridge_id": slug,
            "priority": "normal",
            "source": "domain_gap",
            "source_detail": f"domains:{d1}+{d2}",
            "source_name": f"{d1} ↔ {d2}",
            "exists": False,
            "novelty_score": score,
            "unknowns_d1": len(domain_unknowns[d1]),
            "unknowns_d2": len(domain_unknowns[d2]),
            "sample_unknowns_d1": domain_unknowns[d1][:3],
            "sample_unknowns_d2": domain_unknowns[d2][:3],
            "description": (
                f"Domain pair with {unknown_score} combined unknowns and "
                f"{'existing' if pair in bridged_pairs else 'no existing'} bridge."
            ),
        })
    candidates.sort(key=lambda x: x["novelty_score"], reverse=True)
    return candidates[:top_n]


# ── draft YAML stubs ─────────────────────────────────────────────────────────

def _write_draft_yamls(proposals: list[dict], drafts_dir: Path) -> None:
    if not _YAML_OK:
        print("  [skip] yaml not available — cannot write draft stubs")
        return
    drafts_dir.mkdir(parents=True, exist_ok=True)
    for c in proposals:
        slug = c["bridge_id"].replace(" ", "-").lower()
        draft = {
            "id": slug,
            "title": f"[DRAFT] {c['source_name']} — bridge claim TBD",
            "source": c["source"],
            "priority": c["priority"],
            "bridge_claim": "TODO: state the mathematical/conceptual bridge",
            "translation_table": [{"source_concept": "TODO", "target_concept": "TODO"}],
            "evidence": ["TODO: cite key papers"],
            "references": [],
            "last_reviewed": "2026-05-06",
        }
        out_path = drafts_dir / f"{slug}.yaml"
        if not out_path.exists():
            out_path.write_text(
                yaml.dump(draft, allow_unicode=True, sort_keys=False),
                encoding="utf-8",
            )
    print(f"\nDraft YAMLs written to {drafts_dir}/")


# ── main ─────────────────────────────────────────────────────────────────────

def main() -> dict:
    parser = argparse.ArgumentParser(description="Propose novel cross-domain bridges")
    parser.add_argument("--top", type=int, default=10,
                        help="Number of domain-gap candidates to include")
    parser.add_argument("--min-unknowns", type=int, default=3,
                        help="Min unknowns per domain for domain-gap proposals")
    parser.add_argument("--output", type=str, default="docs/bridge_proposals.json",
                        help="Output JSON file path")
    parser.add_argument("--draft-yaml", action="store_true",
                        help="Write draft bridge YAML stubs to drafts/bridges/")
    args = parser.parse_args()

    print("\n" + "=" * 65)
    print("USDR Enhanced Bridge Proposer")
    print("Sources: pioneer seeds | breakthrough gaps | domain pairs")
    print("=" * 65)

    existing = _existing_bridge_ids()
    print(f"\n  Existing bridges found: {len(existing)}")

    # ── pioneer seeds ──
    pioneer_props = _pioneer_proposals(existing)
    pioneer_missing = [p for p in pioneer_props if not p["exists"]]
    print(f"\n  Pioneer bridge seeds total  : {len(pioneer_props)}")
    print(f"  Pioneer seeds not yet built : {len(pioneer_missing)}")
    for p in pioneer_missing[:10]:
        print(f"    [CRITICAL] {p['bridge_id']}  (from {p['source_name']})")

    # ── breakthrough gap bridges ──
    gap_props = _breakthrough_gap_proposals(existing)
    gap_missing = [p for p in gap_props if not p["exists"]]
    print(f"\n  Breakthrough gap required bridges total  : {len(gap_props)}")
    print(f"  Breakthrough gap bridges not yet built   : {len(gap_missing)}")
    for p in gap_missing[:10]:
        print(f"    [{p['priority'].upper():8}] {p['bridge_id']}  (for: {p['source_name'][:50]})")

    # ── domain gaps ──
    domain_props = _domain_gap_proposals(args.top, args.min_unknowns)
    print(f"\n  Domain-gap top-{args.top} novel pairs:")
    for p in domain_props:
        print(f"    [NORMAL  ] {p['bridge_id']}  (score={p.get('novelty_score', '?')})")

    # ── summary ──
    all_proposals = pioneer_props + gap_props + domain_props

    # Deduplicate by bridge_id (keep highest priority)
    priority_rank = {"critical": 0, "high": 1, "normal": 2}
    seen: dict[str, dict] = {}
    for prop in all_proposals:
        bid = prop["bridge_id"]
        if bid not in seen or priority_rank[prop["priority"]] < priority_rank[seen[bid]["priority"]]:
            seen[bid] = prop
    deduped = sorted(seen.values(), key=lambda x: (priority_rank[x["priority"]], x["bridge_id"]))

    critical_count = sum(1 for p in deduped if p["priority"] == "critical")
    high_count = sum(1 for p in deduped if p["priority"] == "high")
    normal_count = sum(1 for p in deduped if p["priority"] == "normal")
    missing_count = sum(1 for p in deduped if not p["exists"])

    print("\n" + "-" * 65)
    print(f"  Total unique proposals     : {len(deduped)}")
    print(f"  CRITICAL (pioneer seeds)   : {critical_count}")
    print(f"  HIGH     (breakthrough gaps): {high_count}")
    print(f"  NORMAL   (domain gaps)     : {normal_count}")
    print(f"  Not yet built              : {missing_count}")
    print(f"  Pioneer seed proposals     : {len(pioneer_missing)}")
    print(f"  Breakthrough gap proposals : {len(gap_missing)}")
    print("=" * 65 + "\n")

    output = {
        "generated": "2026-05-06",
        "total_proposals": len(deduped),
        "summary": {
            "critical_count": critical_count,
            "high_count": high_count,
            "normal_count": normal_count,
            "missing_count": missing_count,
            "pioneer_seed_count": len(pioneer_missing),
            "breakthrough_gap_count": len(gap_missing),
        },
        "proposals": deduped,
        # legacy keys for dashboard compatibility
        "candidates": domain_props,
        "total_pairs_evaluated": len(domain_props),
    }

    out_path = ROOT / args.output
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"Results written to {out_path}")

    # Always mirror to api/v1/ for dashboard live fetch
    api_path = ROOT / "api" / "v1" / "bridge_proposals.json"
    api_path.parent.mkdir(parents=True, exist_ok=True)
    api_path.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"Results mirrored to {api_path}")

    if args.draft_yaml:
        _write_draft_yamls(
            [p for p in deduped if not p["exists"] and p["priority"] in ("critical", "high")],
            ROOT / "drafts" / "bridges",
        )

    return output


if __name__ == "__main__":
    main()
