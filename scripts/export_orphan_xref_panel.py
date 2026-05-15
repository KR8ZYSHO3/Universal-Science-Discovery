#!/usr/bin/env python3
"""Export a small JSON panel for the contributor hub: xref hygiene + orphan unknowns.

Reads the same YAML cross-references as ``build_graph.py`` and the filtered
``docs/knowledge_graph.json``. Does **not** re-run the full graph layout in the
browser — output is static ``api/v1/orphan_xref_panel.json`` for the hub to fetch.

Usage (from repo root)::

    python scripts/export_orphan_xref_panel.py

See ``docs/DEV_DASHBOARD.md`` for when to regenerate.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

import build_graph as bg  # noqa: E402

ROOT = bg.ROOT
API_OUT = ROOT / "api" / "v1" / "orphan_xref_panel.json"

GITHUB_OWNER = "KR8ZYSHO3"
GITHUB_REPO = "Universal-Science-Discovery"
GITHUB_BRANCH = "main"

CAP_MISSING = 70
CAP_ORPHAN_UNKNOWN = 30
MAX_TOTAL = 100


def _github_blob(rel_path: str) -> str:
    return f"https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/blob/{GITHUB_BRANCH}/{rel_path}"


def _github_filename_search(node_id: str) -> str:
    q = f"filename:{node_id}.yaml"
    return f"https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/search?q={q}&type=code"


def collect_missing_xref_targets() -> dict[str, dict]:
    """IDs referenced in EDGE_FIELDS but absent from the node set (stale / typo / missing file)."""
    nodes, _raw = bg.build_nodes_and_raw_edges()
    node_ids = {n["id"] for n in nodes}
    agg: dict[str, dict] = {}
    for path, _entry_type in bg.iter_yaml_files():
        data = bg.load_yaml(path)
        if not data:
            continue
        entry_id = data.get("id", "")
        if not entry_id:
            continue
        rel = path.relative_to(ROOT).as_posix()
        for field_name, relation in bg.EDGE_FIELDS:
            targets = bg.extract_ref_ids(data.get(field_name))
            for target_id in targets:
                if target_id in node_ids:
                    continue
                slot = agg.setdefault(
                    target_id,
                    {"count": 0, "samples": []},
                )
                slot["count"] += 1
                if len(slot["samples"]) < 10:
                    slot["samples"].append(
                        {
                            "source_id": entry_id,
                            "source_path": rel,
                            "field": field_name,
                            "relation": relation,
                        }
                    )
    return agg


def _unknown_yaml_path(node_id: str) -> str | None:
    matches = list((ROOT / "unknowns-catalog").rglob(f"{node_id}.yaml"))
    if not matches:
        return None
    return matches[0].relative_to(ROOT).as_posix()


def collect_orphan_unknowns() -> list[dict]:
    """Unknown nodes with no incident edge in the **filtered** graph (same as find_orphan_unknowns)."""
    kg_path = ROOT / "docs" / "knowledge_graph.json"
    if not kg_path.exists():
        return []
    graph = json.loads(kg_path.read_text(encoding="utf-8"))
    nodes: list[dict] = graph.get("nodes") or []
    edges: list[dict] = graph.get("edges") or []
    connected: set[str] = set()
    for edge in edges:
        s, t = edge.get("source"), edge.get("target")
        sid = s if isinstance(s, str) else (s or {}).get("id", "")
        tid = t if isinstance(t, str) else (t or {}).get("id", "")
        if sid:
            connected.add(sid)
        if tid:
            connected.add(tid)
    out: list[dict] = []
    for n in nodes:
        if n.get("type") != "unknown":
            continue
        nid = n.get("id", "")
        if not nid or nid in connected:
            continue
        ypath = _unknown_yaml_path(nid)
        out.append(
            {
                "node": n,
                "yaml_path": ypath,
            }
        )
    out.sort(key=lambda x: x["node"]["id"])
    return out


def build_items() -> list[dict]:
    items: list[dict] = []
    missing = collect_missing_xref_targets()
    ranked = sorted(missing.items(), key=lambda kv: (-kv[1]["count"], kv[0]))
    for target_id, info in ranked[:CAP_MISSING]:
        samples: list[dict] = info["samples"]
        primary = samples[0] if samples else {}
        src_path = primary.get("source_path", "")
        reason = (
            f"Referenced {info['count']}× from catalog YAML as a graph target, "
            f"but `{target_id}` is not in the knowledge graph node set "
            f"(rename, typo, or missing catalog file). "
        )
        if src_path:
            reason += f"Example: `{primary.get('field', '')}` in `{src_path}`."
        items.append(
            {
                "id": f"missing-xref-target:{target_id}",
                "kind": "missing_xref_target",
                "ref_id": target_id,
                "title": None,
                "reason": reason.strip(),
                "referenced_count": info["count"],
                "sample_referrers": samples[:5],
                "suggested_path": src_path or None,
                "github_blob_url": _github_blob(src_path) if src_path else None,
                "github_search_url": _github_filename_search(target_id),
            }
        )

    for row in collect_orphan_unknowns()[:CAP_ORPHAN_UNKNOWN]:
        n = row["node"]
        nid = n["id"]
        ypath = row["yaml_path"]
        title = (n.get("title") or "").strip() or None
        reason = (
            "Unknown is in the graph but has no edges to a bridge or hypothesis yet — "
            "a structural contribution target (not a scientific claim about importance)."
        )
        items.append(
            {
                "id": f"orphan-unknown:{nid}",
                "kind": "orphan_unknown",
                "ref_id": nid,
                "title": title,
                "reason": reason,
                "referenced_count": None,
                "sample_referrers": [],
                "suggested_path": ypath,
                "github_blob_url": _github_blob(ypath) if ypath else None,
                "github_search_url": _github_filename_search(nid),
            }
        )

    return items[:MAX_TOTAL]


def main() -> int:
    generated = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    items = build_items()
    payload = {
        "generated_at": generated,
        "source": "scripts/export_orphan_xref_panel.py (YAML xref scan + docs/knowledge_graph.json; mirrors build_graph orphan filtering)",
        "items": items,
        "meta": {
            "item_cap": MAX_TOTAL,
            "missing_xref_cap": CAP_MISSING,
            "orphan_unknown_cap": CAP_ORPHAN_UNKNOWN,
        },
    }
    API_OUT.parent.mkdir(parents=True, exist_ok=True)
    API_OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {API_OUT.relative_to(ROOT)} ({len(items)} items)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
