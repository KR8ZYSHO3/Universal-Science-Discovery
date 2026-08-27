"""Smoke tests for impact router data contract (DISC-02)."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
API_PATH = REPO_ROOT / "api" / "v1" / "bridge_proposals.json"
SCRIPT = REPO_ROOT / "scripts" / "propose_bridges.py"


def test_bridge_proposals_json_contract() -> None:
    assert API_PATH.is_file(), "api/v1/bridge_proposals.json missing — run scripts/propose_bridges.py"
    data = json.loads(API_PATH.read_text(encoding="utf-8"))
    assert "generated" in data and "summary" in data and "proposals" in data
    assert isinstance(data["proposals"], list)
    assert data["proposals"], "expected at least one bridge proposal"
    summary = data["summary"]
    for key in ("critical_count", "high_count", "normal_count", "missing_count"):
        assert key in summary
    sample = data["proposals"][0]
    for key in ("bridge_id", "priority", "source", "exists", "description"):
        assert key in sample


def test_propose_bridges_cli_exits_zero() -> None:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "--top", "3"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    assert proc.returncode == 0, proc.stderr
    assert "USDR Enhanced Bridge Proposer" in proc.stdout


def test_breakthrough_gap_proposals_present() -> None:
    data = json.loads(API_PATH.read_text(encoding="utf-8"))
    gap_props = [p for p in data["proposals"] if p.get("source") == "breakthrough_gap"]
    assert gap_props, "expected breakthrough-gap proposals for impact router"
    missing = [p for p in gap_props if not p.get("exists")]
    assert missing, "expected at least one missing breakthrough-gap bridge"