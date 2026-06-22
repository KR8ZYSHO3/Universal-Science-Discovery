"""Crosscheck codegen drift gate (see scripts/build_crosscheck.py)."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


def test_crosscheck_artifacts_up_to_date() -> None:
    cmd = [sys.executable, str(REPO_ROOT / "scripts" / "build_crosscheck.py"), "--check"]
    proc = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True, check=False)
    if proc.returncode != 0:
        out = (proc.stdout or "") + (proc.stderr or "")
        raise AssertionError(f"build_crosscheck.py --check failed:\n{out}")