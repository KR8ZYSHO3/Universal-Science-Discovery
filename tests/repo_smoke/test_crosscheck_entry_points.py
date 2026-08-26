"""Entry-point smokes for generate_crosscheck.py (dry-run) and oncology GCC."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


def test_generate_crosscheck_dry_run_oncology_prints_protocol_id() -> None:
    cmd = [
        sys.executable,
        str(REPO_ROOT / "scripts" / "generate_crosscheck.py"),
        "--bridge",
        "b-percolation-oncology",
        "--dry-run",
    ]
    proc = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True, check=False)
    assert proc.returncode == 0, (proc.stdout or "") + (proc.stderr or "")
    assert "p-b-" in (proc.stdout or "")
    assert "--write" not in cmd
    assert "--all" not in cmd


def test_giant_component_fraction_prints_inconclusive_and_exits_0() -> None:
    cmd = [
        sys.executable,
        str(REPO_ROOT / "repro" / "p-b-percolation-oncology-gcc" / "giant_component_fraction.py"),
    ]
    proc = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True, check=False)
    assert proc.returncode == 0, (proc.stdout or "") + (proc.stderr or "")
    assert "RESULT: INCONCLUSIVE" in (proc.stdout or "")
    assert "RESULT: CONFIRMED" not in (proc.stdout or "")
