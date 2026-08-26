#!/usr/bin/env python3
"""Export a small JSON panel for the contributor hub: high-degree bridges.

Ranks existing bridge nodes by undirected degree in ``docs/knowledge_graph.json``
(same increment as ``build_graph.top_nodes_by_degree``; bridges only).
Does **not** walk the graph in the browser — output is static
``api/v1/recommendations.json`` for the hub to fetch.

Usage (from repo root)::

    python scripts/export_recommendations.py

See ``docs/HUB_RECOMMENDATIONS.md`` and ``docs/DEV_DASHBOARD.md``.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
API_OUT = ROOT / "api" / "v1" / "recommendations.json"
KG_PATH = ROOT / "docs" / "knowledge_graph.json"

GITHUB_OWNER = "KR8ZYSHO3"
GITHUB_REPO = "Universal-Science-Discovery"
GITHUB_BRANCH = "main"

MAX_ITEMS = 25


def _github_blob(rel_path: str) -> str:
    return f"https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/blob/{GITHUB_BRANCH}/{rel_path}"


def _github_filename_search(node_id: str) -> str:
    q = f"filename:{node_id}.yaml"
    return f"https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/search?q={q}&type=code"


def _bridge_yaml_path(node_id: str) -> str | None:
    matches = list((ROOT / "cross-domain").rglob(f"{node_id}.yaml"))
    if not matches:
        return None
    return matches[0].relative_to(ROOT).as_posix()


def build_items() -> list[dict]:
    graph = json.loads(KG_PATH.read_text(encoding="utf-8"))
    nodes: list[dict] = graph.get("nodes") or []
    edges: list[dict] = graph.get("edges") or []

    degree: dict[str, int] = defaultdict(int)
    for edge in edges:
        s, t = edge.get("source"), edge.get("target")
        sid = s if isinstance(s, str) else (s or {}).get("id", "")
        tid = t if isinstance(t, str) else (t or {}).get("id", "")
        if sid:
            degree[sid] += 1
        if tid:
            degree[tid] += 1

    bridges = [
        n for n in nodes
        if n.get("type") == "bridge" and str(n.get("id", "")).startswith("b-")
    ]
    ranked = sorted(bridges, key=lambda n: (-degree.get(n["id"], 0), n["id"]))[:MAX_ITEMS]

    items: list[dict] = []
    for n in ranked:
        nid = n["id"]
        ypath = _bridge_yaml_path(nid)
        items.append(
            {
                "id": nid,
                "title": (n.get("title") or "").strip(),
                "score": int(degree.get(nid, 0)),
                "kind": "bridge",
                "github_blob_url": _github_blob(ypath) if ypath else None,
                "github_search_url": _github_filename_search(nid),
            }
        )
    return items


def main() -> int:
    if not KG_PATH.is_file():
        print(
            f"error: {KG_PATH.relative_to(ROOT)} is missing — cannot rank bridges",
            file=sys.stderr,
        )
        return 1

    generated = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    items = build_items()
    payload = {
        "generated_at": generated,
        "source": (
            "scripts/export_recommendations.py "
            "(undirected degree from docs/knowledge_graph.json; "
            "same increment as build_graph.top_nodes_by_degree; bridges only)"
        ),
        "ranking": "undirected_degree",
        "disclaimer": (
            "Contributor tooling, not a scientific ranking and not a "
            "CONFIRMED or INCONCLUSIVE Crosscheck outcome. "
            "score is undirected catalog-graph degree (connectivity only). "
            "Harvest rank and curator score are specified for a later phase and are not computed here."
        ),
        "items": items,
        "meta": {
            "item_cap": MAX_ITEMS,
            "ranking_computed": "undirected_degree",
            "ranking_future_slots": ["harvest", "curator_score"],
        },
    }
    API_OUT.parent.mkdir(parents=True, exist_ok=True)
    API_OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {API_OUT.relative_to(ROOT)} ({len(items)} items)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
