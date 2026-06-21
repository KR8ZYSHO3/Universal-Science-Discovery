#!/usr/bin/env python3
"""
Crosscheck generator — draft experiment protocols from USDR bridge YAML.

Reads cross-domain/ bridges and emits one draft protocol per
cross_pollination_opportunities entry into drafts/crosscheck/.

Usage:
    python scripts/generate_crosscheck.py --bridge b-habitat-percolation-ecology --dry-run
    python scripts/generate_crosscheck.py --bridge b-habitat-percolation-ecology --write
    python scripts/generate_crosscheck.py --all --write
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required — pip install pyyaml", file=sys.stderr)
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]
CROSS_DOMAIN = ROOT / "cross-domain"
DRAFTS_DIR = ROOT / "drafts" / "crosscheck"

DESKTOP_KEYWORDS = (
    "monte carlo", "simulation", "simulate", "numerical", "networkx",
    "lattice", "model", "codebase", "algorithm", "closed-form",
)


def load_bridge(bridge_id: str) -> tuple[Path, dict[str, Any]]:
    matches = list(CROSS_DOMAIN.rglob(f"{bridge_id}.yaml"))
    if not matches:
        raise FileNotFoundError(f"Bridge not found: {bridge_id}")
    path = matches[0]
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if data.get("id") != bridge_id:
        raise ValueError(f"{path}: id field is {data.get('id')!r}, expected {bridge_id}")
    return path, data


def slugify(text: str, max_len: int = 40) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return text[:max_len].strip("-") or "test"


def infer_feasibility(text: str) -> str:
    lower = text.lower()
    if any(k in lower for k in DESKTOP_KEYWORDS):
        return "desktop"
    if any(k in lower for k in ("field", "landscape", "population", "clinical")):
        return "field"
    if any(k in lower for k in ("laboratory", "wet lab", "cell culture")):
        return "lab"
    if any(k in lower for k in ("supercomputer", "hpc", "petascale")):
        return "hpc"
    return "desktop"


def default_experimental_design(bridge: dict[str, Any], opportunity: str) -> list[str]:
    fields = bridge.get("fields") or ["field A", "field B"]
    return [
        f"Load bridge {bridge.get('id')} and linked records from USDR.",
        f"Operationalize the cross_pollination_opportunity in {fields[0]} and {fields[1]} terms.",
        "Acquire or simulate data matching translation_mapping variables.",
        "Compute the statistic named in falsifiable_prediction.",
        "Compare result to prediction; record confirmed or falsified.",
    ]


def build_protocol(
    bridge: dict[str, Any],
    opportunity: str,
    index: int,
    *,
    status: str = "draft",
) -> dict[str, Any]:
    bridge_id = bridge["id"]
    slug = slugify(opportunity.split(".")[0].split(",")[0])
    protocol_id = f"p-{bridge_id}-{slug}"

    related_h = (bridge.get("related_hypotheses") or [None])[0]
    related_u = (bridge.get("related_unknowns") or [None])[0]

    translation = []
    for row in bridge.get("translation_table") or []:
        translation.append({
            "field_a_term": row.get("field_a_term", ""),
            "field_b_term": row.get("field_b_term", ""),
            **({"note": row["note"]} if row.get("note") else {}),
        })

    return {
        "id": protocol_id,
        "title": f"[DRAFT] Crosscheck {bridge_id} — opportunity {index + 1}",
        "status": status,
        "source_bridge": bridge_id,
        **({"source_hypothesis": related_h} if related_h else {}),
        **({"source_unknown": related_u} if related_u else {}),
        "pollination_index": index,
        "falsifiable_prediction": opportunity.strip(),
        "null_hypothesis": "TODO: state what outcome would refute the bridge mapping",
        **({"translation_mapping": translation} if translation else {}),
        "experimental_design": default_experimental_design(bridge, opportunity),
        "statistical_analysis_plan": "TODO: specify test statistic and acceptance criteria",
        "feasibility_tier": infer_feasibility(opportunity),
        "last_reviewed": "2026-06-21",
    }


def output_path_for(bridge_path: Path, protocol_id: str) -> Path:
    rel_parent = bridge_path.parent.relative_to(CROSS_DOMAIN)
    return DRAFTS_DIR / rel_parent / f"{protocol_id}.yaml"


def iter_bridges(bridge_id: str | None) -> list[tuple[Path, dict[str, Any]]]:
    if bridge_id:
        path, data = load_bridge(bridge_id)
        return [(path, data)]
    out: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted(CROSS_DOMAIN.rglob("b-*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        if data.get("cross_pollination_opportunities"):
            out.append((path, data))
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Crosscheck protocol drafts from USDR bridges")
    parser.add_argument("--bridge", type=str, help="Single bridge ID (b-...)")
    parser.add_argument("--all", action="store_true", help="All bridges with cross_pollination_opportunities")
    parser.add_argument("--dry-run", action="store_true", help="Print drafts without writing files")
    parser.add_argument("--write", action="store_true", help="Write drafts to drafts/crosscheck/")
    args = parser.parse_args()

    if not args.bridge and not args.all:
        parser.error("Specify --bridge ID or --all")
    if args.dry_run and args.write:
        parser.error("Use either --dry-run or --write, not both")

    bridges = iter_bridges(args.bridge)
    total = 0

    print("Crosscheck protocol generator")
    print("=" * 60)

    for bridge_path, bridge in bridges:
        bridge_id = bridge.get("id", bridge_path.stem)
        opportunities = bridge.get("cross_pollination_opportunities") or []
        print(f"\n{bridge_id}  ({len(opportunities)} opportunities)")
        for i, opp in enumerate(opportunities):
            protocol = build_protocol(bridge, opp, i)
            out_path = output_path_for(bridge_path, protocol["id"])
            total += 1
            print(f"  [{i}] {protocol['id']}  tier={protocol['feasibility_tier']}")
            if args.dry_run:
                print(yaml.dump(protocol, allow_unicode=True, sort_keys=False, default_flow_style=False)[:400] + "...")
            elif args.write:
                out_path.parent.mkdir(parents=True, exist_ok=True)
                if out_path.exists():
                    print(f"      skip (exists): {out_path.relative_to(ROOT)}")
                else:
                    out_path.write_text(
                        yaml.dump(protocol, allow_unicode=True, sort_keys=False),
                        encoding="utf-8",
                    )
                    print(f"      wrote: {out_path.relative_to(ROOT)}")

    print()
    print("=" * 60)
    print(f"Total protocols: {total}")
    if not args.dry_run and not args.write:
        print("Hint: add --dry-run or --write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())