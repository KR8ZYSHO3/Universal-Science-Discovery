#!/usr/bin/env python3
"""
Find unknowns with no associated hypothesis or bridge — prime contribution targets.

An unknown is "orphaned" if no edge in knowledge_graph.json references its id.
These are the highest-priority targets for new contributions.

Usage:
    python scripts/find_orphan_unknowns.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent


def main() -> list[dict]:
    graph = json.loads(
        (ROOT / "docs" / "knowledge_graph.json").read_text(encoding="utf-8")
    )
    nodes: list[dict] = graph["nodes"]
    edges: list[dict] = graph["edges"]

    # Collect every node id that appears in any edge endpoint
    connected_ids: set[str] = set()
    for edge in edges:
        src = edge["source"]
        tgt = edge["target"]
        src_id = src if isinstance(src, str) else src.get("id", "")
        tgt_id = tgt if isinstance(tgt, str) else tgt.get("id", "")
        connected_ids.add(src_id)
        connected_ids.add(tgt_id)

    all_unknowns = [n for n in nodes if n.get("type") == "unknown"]
    orphans = [n for n in all_unknowns if n["id"] not in connected_ids]

    print(f"Total unknowns in graph:                        {len(all_unknowns)}")
    print(f"Connected to ≥1 bridge or hypothesis edge:      {len(all_unknowns) - len(orphans)}")
    print(f"Orphan unknowns (no connections):               {len(orphans)}")
    print(f"\nTop 20 orphan unknowns (priority contribution targets):")
    for n in orphans[:20]:
        print(f"  {n['id']}: {n['title'][:80]}")

    out = ROOT / "docs" / "orphan_unknowns.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Orphan Unknowns — Priority Contribution Targets\n\n",
        f"These **{len(orphans)}** unknowns have no associated hypothesis or bridge edge "
        f"in the knowledge graph.\n",
        "They are the highest-priority targets for new contributions — add a hypothesis "
        "or propose a cross-domain bridge connecting them.\n\n",
        "| ID | Title |\n",
        "|---|---|\n",
    ]
    for n in orphans:
        title = n.get("title", "").strip().replace("|", "\\|")
        lines.append(f"| `{n['id']}` | {title} |\n")

    out.write_text("".join(lines), encoding="utf-8")
    print(f"\nFull list written to {out}")

    return orphans


if __name__ == "__main__":
    main()
