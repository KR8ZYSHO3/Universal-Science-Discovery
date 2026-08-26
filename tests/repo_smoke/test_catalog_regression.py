"""Smoke tests for repo automation used as merge gates (see validate-schemas.yml).

Includes catalog validation, domain page regression, dashboard stat consistency,
an informational ``build_graph.py --report-orphans`` run, and shape checks for
``api/v1/orphan_xref_panel.json`` and ``api/v1/recommendations.json``.

Run from repo root::

    python -m pytest tests/repo_smoke -v
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


def _run_script(name: str, *extra_args: str) -> None:
    cmd = [sys.executable, str(REPO_ROOT / "scripts" / name), *extra_args]
    proc = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True, check=False)
    if proc.returncode != 0:
        out = (proc.stdout or "") + (proc.stderr or "")
        raise AssertionError(f"{name} exited {proc.returncode}:\n{out}")


def test_validate_schemas() -> None:
    _run_script("validate_schemas.py")


def test_verify_domain_pages() -> None:
    _run_script("verify_domain_pages.py")


def test_verify_dashboard_consistency() -> None:
    _run_script("verify_dashboard_consistency.py")


def test_build_graph_report_orphans() -> None:
    """Ensures orphan xref reporter runs (does not fail on existing xref drift)."""
    _run_script("build_graph.py", "--report-orphans")


def test_orphan_xref_panel_json() -> None:
    """Committed hub panel JSON parses and matches the export contract."""
    path = REPO_ROOT / "api" / "v1" / "orphan_xref_panel.json"
    assert path.is_file(), "api/v1/orphan_xref_panel.json missing — run scripts/export_orphan_xref_panel.py"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert "generated_at" in data and "source" in data and "items" in data
    assert isinstance(data["items"], list)
    for item in data["items"][:5]:
        assert item.get("id")
        assert item.get("kind") in ("missing_xref_target", "orphan_unknown")
        assert item.get("reason")
        assert item.get("github_search_url")


def test_recommendations_json() -> None:
    """Committed hub recommendations JSON parses and matches the export contract."""
    path = REPO_ROOT / "api" / "v1" / "recommendations.json"
    assert path.is_file(), "api/v1/recommendations.json missing — run scripts/export_recommendations.py"
    data = json.loads(path.read_text(encoding="utf-8"))
    for key in ("generated_at", "source", "ranking", "disclaimer", "items"):
        assert key in data
    assert data["ranking"] == "undirected_degree"
    assert "not a scientific ranking" in data["disclaimer"]
    assert isinstance(data["items"], list)
    assert len(data["items"]) <= 25
    for item in data["items"]:
        assert str(item.get("id", "")).startswith("b-")
        assert item.get("kind") == "bridge"
        assert isinstance(item.get("score"), int) and not isinstance(item.get("score"), bool)
        assert "harvest_rank" not in item
        assert "curator_score" not in item
        blob = item.get("github_blob_url")
        search = item.get("github_search_url")
        assert search or blob
        for url in (blob, search):
            if url:
                assert str(url).startswith("https://github.com/")
    meta = json.loads((REPO_ROOT / "api" / "v1" / "meta.json").read_text(encoding="utf-8"))
    assert meta.get("endpoints", {}).get("recommendations") == "api/v1/recommendations.json"
