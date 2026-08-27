"""Smoke tests for orphan unknowns panel export (DISC-03)."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
API_PATH = REPO_ROOT / "api" / "v1" / "orphan_unknowns_panel.json"
EXPORT_SCRIPT = REPO_ROOT / "scripts" / "export_orphan_unknowns_panel.py"
FIND_SCRIPT = REPO_ROOT / "scripts" / "find_orphan_unknowns.py"


def test_orphan_unknowns_panel_json_contract() -> None:
    assert API_PATH.is_file(), (
        "api/v1/orphan_unknowns_panel.json missing — run scripts/export_orphan_unknowns_panel.py"
    )
    data = json.loads(API_PATH.read_text(encoding="utf-8"))
    assert "generated_at" in data and "source" in data and "items" in data and "meta" in data
    assert isinstance(data["items"], list)
    meta = data["meta"]
    for key in ("total_unknowns", "connected_unknowns", "orphan_count", "item_cap"):
        assert key in meta
    assert meta["orphan_count"] == len(data["items"]) or meta["orphan_count"] > meta["item_cap"]
    for item in data["items"][:3]:
        assert item.get("id", "").startswith("u-")
        assert item.get("reason")
        assert item.get("github_search_url")


def test_export_orphan_unknowns_panel_exits_zero() -> None:
    proc = subprocess.run(
        [sys.executable, str(EXPORT_SCRIPT)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    assert proc.returncode == 0, proc.stderr
    assert "orphan_unknowns_panel.json" in proc.stdout


def test_find_orphan_unknowns_exits_zero() -> None:
    proc = subprocess.run(
        [sys.executable, str(FIND_SCRIPT)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    assert proc.returncode == 0, proc.stderr
    assert "Orphan unknowns" in proc.stdout