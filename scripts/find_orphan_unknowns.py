#!/usr/bin/env python3
"""
Find unknowns with no associated hypothesis or bridge — prime contribution targets.

An unknown is "orphaned" if no edge in knowledge_graph.json references its id.
These are the highest-priority targets for new contributions.

Usage:
    python scripts/find_orphan_unknowns.py
"""
from __future__ import annotations

import io
import json
import sys
from pathlib import Path

# Ensure stdout handles Unicode on Windows (cp1252 terminal can't encode ≥)
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf-8-sig"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
GRAPH_PATH = ROOT / "docs" / "knowledge_graph.json"

GITHUB_OWNER = "KR8ZYSHO3"
GITHUB_REPO = "Universal-Science-Discovery"
GITHUB_BRANCH = "main"


def _unknown_yaml_path(node_id: str) -> str | None:
    matches = list((ROOT / "unknowns-catalog").rglob(f"{node_id}.yaml"))
    if not matches:
        return None
    return matches[0].relative_to(ROOT).as_posix()


def _github_blob(rel_path: str) -> str:
    return (
        f"https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/blob/{GITHUB_BRANCH}/{rel_path}"
    )


def _github_filename_search(node_id: str) -> str:
    q = f"filename:{node_id}.yaml"
    return (
        f"https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/search?q={q}&type=code"
    )


def analyze_orphan_unknowns(
    graph_path: Path = GRAPH_PATH,
) -> dict[str, int | list[dict]]:
    """Scan knowledge graph for unknowns with no incident edges."""
    if not graph_path.exists():
        raise FileNotFoundError(
            f"{graph_path} not found — run build_graph.py first."
        )
    graph = json.loads(graph_path.read_text(encoding="utf-8"))
    nodes: list[dict] = graph.get("nodes") or []
    edges: list[dict] = graph.get("edges") or []

    connected_ids: set[str] = set()
    for edge in edges:
        src = edge.get("source")
        tgt = edge.get("target")
        src_id = src if isinstance(src, str) else (src or {}).get("id", "")
        tgt_id = tgt if isinstance(tgt, str) else (tgt or {}).get("id", "")
        if src_id:
            connected_ids.add(src_id)
        if tgt_id:
            connected_ids.add(tgt_id)

    all_unknowns = [n for n in nodes if n.get("type") == "unknown"]
    orphans: list[dict] = []
    for node in all_unknowns:
        nid = node.get("id", "")
        if not nid or nid in connected_ids:
            continue
        ypath = _unknown_yaml_path(nid)
        fields = node.get("fields") or node.get("disciplines") or []
        if not isinstance(fields, list):
            fields = [fields] if fields else []
        orphans.append(
            {
                "id": nid,
                "title": (node.get("title") or "").strip() or None,
                "fields": [str(f) for f in fields if f],
                "yaml_path": ypath,
                "github_blob_url": _github_blob(ypath) if ypath else None,
                "github_search_url": _github_filename_search(nid),
                "reason": (
                    "Unknown is in the graph but has no edges to a bridge or hypothesis yet — "
                    "add a hypothesis or bridge that references this ID."
                ),
            }
        )

    orphans.sort(key=lambda row: row["id"])
    return {
        "total_unknowns": len(all_unknowns),
        "connected_unknowns": len(all_unknowns) - len(orphans),
        "orphan_count": len(orphans),
        "orphans": orphans,
    }


def collect_orphan_unknown_rows() -> list[dict]:
    """Legacy shape for export_orphan_xref_panel: {node, yaml_path}."""
    analysis = analyze_orphan_unknowns()
    rows: list[dict] = []
    graph = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
    node_map = {n["id"]: n for n in graph.get("nodes") or [] if n.get("id")}
    for item in analysis["orphans"]:
        assert isinstance(item, dict)
        nid = item["id"]
        rows.append({"node": node_map.get(nid, item), "yaml_path": item.get("yaml_path")})
    return rows


def main() -> list[dict]:
    try:
        analysis = analyze_orphan_unknowns()
    except FileNotFoundError as exc:
        print(f"ERROR: {exc}")
        sys.exit(1)
    except (json.JSONDecodeError, OSError) as exc:
        print(f"ERROR: could not read knowledge_graph.json: {exc}")
        sys.exit(1)

    total = int(analysis["total_unknowns"])
    connected = int(analysis["connected_unknowns"])
    orphan_count = int(analysis["orphan_count"])
    orphans = list(analysis["orphans"])

    print(f"Total unknowns in graph:                        {total}")
    print(f"Connected to ≥1 bridge or hypothesis edge:      {connected}")
    print(f"Orphan unknowns (no connections):               {orphan_count}")
    if orphans:
        print("\nTop 20 orphan unknowns (priority contribution targets):")
        for row in orphans[:20]:
            title = (row.get("title") or row["id"])[:80]
            print(f"  {row['id']}: {title}")

    out = ROOT / "docs" / "orphan_unknowns.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Orphan Unknowns — Priority Contribution Targets\n\n",
        f"These **{orphan_count}** unknowns have no associated hypothesis or bridge edge "
        f"in the knowledge graph.\n",
        "They are the highest-priority targets for new contributions — add a hypothesis "
        "or propose a cross-domain bridge connecting them.\n\n",
        "| ID | Title |\n",
        "|---|---|\n",
    ]
    for row in orphans:
        title = (row.get("title") or "").strip().replace("|", "\\|")
        lines.append(f"| `{row['id']}` | {title} |\n")

    out.write_text("".join(lines), encoding="utf-8")
    print(f"\nFull list written to {out}")

    return orphans


if __name__ == "__main__":
    main()