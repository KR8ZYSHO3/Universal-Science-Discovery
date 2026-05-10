"""Smoke tests for repo automation used as merge gates (see validate-schemas.yml).

Includes catalog validation, domain page regression, dashboard stat consistency,
and an informational ``build_graph.py --report-orphans`` run.

Run from repo root::

    python -m pytest tests/repo_smoke -v
"""

from __future__ import annotations

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
