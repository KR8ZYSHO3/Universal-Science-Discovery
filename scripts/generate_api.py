#!/usr/bin/env python3
"""
Generate static JSON API endpoints from the USDR catalog.
Output: api/v1/{endpoint}.json

Endpoints:
  api/v1/meta.json          — catalog statistics and metadata
  api/v1/unknowns.json      — all unknowns (id, title, status, domain)
  api/v1/bridges.json       — all bridges (id, title, source, target, status)
  api/v1/hypotheses.json    — all hypotheses (id, title, status, priority, impact_score)
  api/v1/domains.json       — domain summary stats
  api/v1/graph.json         — same as docs/knowledge_graph.json (symlink/copy)
  api/v1/bridge_proposals.json — co-pilot proposals
  api/v1/orphan_xref_panel.json — hub panel: missing xrefs + orphan unknowns (see export_orphan_xref_panel.py)
  api/v1/breakthrough_gaps.json — breakthrough gap summaries

Usage:
    python scripts/generate_api.py
"""
import yaml, json
from pathlib import Path
from datetime import date, datetime

ROOT = Path(__file__).parent.parent
API_DIR = ROOT / "api" / "v1"

def load_yaml(p):
    try:
        return yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    except Exception as exc:
        import sys
        print(f"  WARNING: could not parse {p}: {exc}", file=sys.stderr)
        return {}

def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  wrote {path.relative_to(ROOT)}")

def main():
    API_DIR.mkdir(parents=True, exist_ok=True)

    # Collect all unknowns
    unknowns = []
    for p in sorted((ROOT / "unknowns-catalog").rglob("u-*.yaml")):
        d = load_yaml(p)
        if d:
            domain = p.parent.name
            unknowns.append({
                "id": d.get("id", p.stem),
                "title": d.get("title", ""),
                "status": d.get("status", "open"),
                "domain": domain,
                "systematic_gaps": d.get("systematic_gaps", []),
                "suggested_hypotheses": d.get("suggested_hypotheses", []),
                "file": str(p.relative_to(ROOT))
            })

    # Collect all bridges
    bridges = []
    for p in sorted((ROOT / "cross-domain").rglob("b-*.yaml")):
        d = load_yaml(p)
        if d:
            bridges.append({
                "id": d.get("id", p.stem),
                "title": d.get("title", ""),
                "source_domain": d.get("source_domain", ""),
                "target_domain": d.get("target_domain", ""),
                "status": d.get("status", "proposed"),
                "bridge_claim": (d.get("bridge_claim", "") or "")[:300],
                "open_unknowns": d.get("open_unknowns", []),
                "related_hypotheses": d.get("related_hypotheses", []),
                "communication_gap": d.get("communication_gap", ""),
                "translation_table": d.get("translation_table", []),
                "references": d.get("references", []),
                "last_reviewed": d.get("last_reviewed", ""),
                "file": str(p.relative_to(ROOT))
            })

    # Breakthrough gaps (world-scale stalled breakthroughs)
    breakthrough_gaps = []
    for p in sorted((ROOT / "breakthrough-gaps").glob("bg-*.yaml")):
        d = load_yaml(p)
        if not d:
            continue
        breakthrough_gaps.append({
            "id": d.get("id", p.stem),
            "title": d.get("title", ""),
            "source_domain": d.get("source_domain", ""),
            "current_trl": d.get("current_trl"),
            "world_reshaping_potential": d.get("world_reshaping_potential", ""),
            "blocking_gap_count": len(d.get("blocking_gaps") or []),
            "required_bridge_count": len(d.get("required_bridges") or []),
            "file": str(p.relative_to(ROOT)),
        })

    # Collect all hypotheses
    hypotheses = []
    for p in sorted((ROOT / "hypotheses").rglob("h-*.yaml")):
        d = load_yaml(p)
        if d:
            hypotheses.append({
                "id": d.get("id", p.stem),
                "title": d.get("title", ""),
                "status": d.get("status", "active"),
                "priority": d.get("priority", "medium"),
                "impact_score": d.get("impact_score", 5),
                "created": str(d.get("created", "")),
                "evidence_links": d.get("evidence_links", []),
                "file": str(p.relative_to(ROOT))
            })

    # Domain summary
    domain_stats = {}
    for u in unknowns:
        dom = u["domain"]
        if dom not in domain_stats:
            domain_stats[dom] = {"unknowns": 0, "bridges": 0}
        domain_stats[dom]["unknowns"] += 1
    for b in bridges:
        for dom in [b["source_domain"], b["target_domain"]]:
            if dom in domain_stats:
                domain_stats[dom]["bridges"] += 1

    domains = [{"domain": k, **v} for k, v in sorted(domain_stats.items(), key=lambda x: -x[1]["unknowns"])]

    # Meta
    meta = {
        "version": "1.0",
        "generated": date.today().isoformat(),
        "repository": "https://github.com/KR8ZYSHO3/Universal-Science-Discovery",
        "dashboard": "https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/",
        "license": "CC-BY-4.0",
        "counts": {
            "unknowns": len(unknowns),
            "bridges": len(bridges),
            "hypotheses": len(hypotheses),
            "breakthrough_gaps": len(breakthrough_gaps),
            "domains": len(domain_stats),
            "total": len(unknowns) + len(bridges) + len(hypotheses)
        },
        "endpoints": {
            "meta": "api/v1/meta.json",
            "unknowns": "api/v1/unknowns.json",
            "bridges": "api/v1/bridges.json",
            "hypotheses": "api/v1/hypotheses.json",
            "breakthrough_gaps": "api/v1/breakthrough_gaps.json",
            "domains": "api/v1/domains.json",
            "graph": "api/v1/graph.json",
            "orphan_xref_panel": "api/v1/orphan_xref_panel.json"
        }
    }

    # Write all endpoints
    write_json(API_DIR / "meta.json", meta)
    write_json(API_DIR / "unknowns.json", {"count": len(unknowns), "items": unknowns})
    write_json(API_DIR / "bridges.json", {"count": len(bridges), "items": bridges})
    write_json(API_DIR / "hypotheses.json", {"count": len(hypotheses), "items": hypotheses})
    write_json(API_DIR / "breakthrough_gaps.json", {"count": len(breakthrough_gaps), "items": breakthrough_gaps})
    write_json(API_DIR / "domains.json", {"count": len(domains), "items": domains})

    # Copy knowledge graph
    kg_src = ROOT / "docs" / "knowledge_graph.json"
    if kg_src.exists():
        import shutil
        shutil.copy2(kg_src, API_DIR / "graph.json")
        print(f"  copied knowledge_graph.json -> api/v1/graph.json")

    # Copy bridge proposals
    proposals_src = ROOT / "docs" / "bridge_proposals.json"
    if proposals_src.exists():
        import shutil
        shutil.copy2(proposals_src, API_DIR / "bridge_proposals.json")
        print(f"  copied bridge_proposals.json -> api/v1/bridge_proposals.json")

    # Copy citation index
    citations_src = ROOT / "docs" / "citation_index.json"
    if citations_src.exists():
        import shutil
        shutil.copy2(citations_src, API_DIR / "citations.json")
        print("  copied citation_index.json -> api/v1/citations.json")

    print(f"\nAPI generated: {len(unknowns)} unknowns, {len(bridges)} bridges, {len(hypotheses)} hypotheses, {len(breakthrough_gaps)} breakthrough gaps")
    print(f"Base URL: https://kr8zysho3.github.io/Universal-Science-Discovery/api/v1/")

if __name__ == "__main__":
    main()
