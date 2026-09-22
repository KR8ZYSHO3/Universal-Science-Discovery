"""Crosscheck codegen drift gate (see scripts/build_crosscheck.py)."""

from __future__ import annotations

import ast
import py_compile
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
EXPLAINERS = REPO_ROOT / "scripts" / "generate_explainers.py"


def test_generate_explainers_compiles() -> None:
    py_compile.compile(str(EXPLAINERS), doraise=True)


def test_generate_explainers_fstrings_are_py311_safe() -> None:
    """Graph rebuild runs Python 3.11, which rejects \\ inside f-string expressions."""
    src = EXPLAINERS.read_text(encoding="utf-8")
    tree = ast.parse(src)
    bad: list[str] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.JoinedStr):
            continue
        for part in node.values:
            if not isinstance(part, ast.FormattedValue):
                continue
            chunk = ast.get_source_segment(src, part.value) or ast.unparse(part.value)
            if "\\" in chunk:
                bad.append(chunk.strip())
    assert not bad, (
        "Python 3.11 SyntaxError: backslash in f-string expression:\n"
        + "\n".join(bad)
    )


def test_crosscheck_artifacts_up_to_date() -> None:
    cmd = [sys.executable, str(REPO_ROOT / "scripts" / "build_crosscheck.py"), "--check"]
    proc = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True, check=False)
    if proc.returncode != 0:
        out = (proc.stdout or "") + (proc.stderr or "")
        raise AssertionError(f"build_crosscheck.py --check failed:\n{out}")