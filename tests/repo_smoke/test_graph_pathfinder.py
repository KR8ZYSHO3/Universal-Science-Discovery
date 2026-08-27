"""Smoke tests for knowledge-graph pathfinder (DISC-01)."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT = REPO_ROOT / "scripts" / "graph_pathfinder.py"


def _import_pathfinder():
    import importlib.util

    spec = importlib.util.spec_from_file_location("graph_pathfinder", SCRIPT)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules["graph_pathfinder"] = mod
    spec.loader.exec_module(mod)
    return mod


def test_domain_pair_has_shortest_path() -> None:
    pf = _import_pathfinder()
    nodes, edges, node_map = pf.load_graph()
    adj = pf.build_adjacency(edges)
    paths = pf.find_paths_by_domain(
        nodes, adj, node_map, "statistical-physics", "conservation-biology"
    )
    assert paths, "expected a path between statistical-physics and conservation-biology"
    assert len(paths[0]) >= 2


def test_id_pair_includes_habitat_bridge() -> None:
    pf = _import_pathfinder()
    nodes, edges, node_map = pf.load_graph()
    adj = pf.build_adjacency(edges)
    paths = pf.find_paths_by_id(
        adj,
        node_map,
        "b-habitat-percolation-ecology",
        "u-percolation-epidemic-fss",
    )
    assert paths
    assert "b-habitat-percolation-ecology" in paths[0]


def test_cli_domain_query_exits_zero() -> None:
    proc = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--from",
            "statistical-physics",
            "--to",
            "conservation-biology",
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    assert proc.returncode == 0, proc.stderr
    assert "Pathfinder:" in proc.stdout


def test_cli_unknown_domain_exits_one() -> None:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "--from", "not-a-real-domain-xyz", "--to", "ecology"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    assert proc.returncode == 1
    assert "unknown domain" in proc.stderr.lower()