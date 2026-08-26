"""Inventory: CONFIRMED-capable repro scripts must be grepped in crosscheck-repro.yml.

Parse the workflow as UTF-8 text. Do not import yaml and do not yaml.safe_load
the workflow: PyYAML 1.1 turns the top-level on: key into True.
Source of truth is stdout RESULT markers in repro/**/*.py, not YAML status.
"""
from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
REPRO_ROOT = REPO_ROOT / "repro"
WORKFLOW = REPO_ROOT / ".github" / "workflows" / "crosscheck-repro.yml"

CONFIRMED_GREP = 'grep -q "RESULT: CONFIRMED"'

_MARKERS = (
    "'CONFIRMED' if",
    '"CONFIRMED" if',
    'result = "CONFIRMED"',
    "result = 'CONFIRMED'",
    "RESULT: CONFIRMED",
)


def _repro_py_files() -> list[Path]:
    return [
        p
        for p in sorted(REPRO_ROOT.rglob("*.py"))
        if "__pycache__" not in p.parts
    ]


def _is_confirmed_capable(text: str) -> bool:
    return any(marker in text for marker in _MARKERS)


def _posix_rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def _workflow_steps(workflow: str) -> list[str]:
    parts = workflow.split("- name:")
    return parts[1:] if len(parts) > 1 else parts


def test_confirmed_capable_repro_scripts_are_grepped_in_crosscheck_repro_workflow() -> None:
    workflow = WORKFLOW.read_text(encoding="utf-8")
    steps = _workflow_steps(workflow)
    discovered: list[str] = []
    for path in _repro_py_files():
        text = path.read_text(encoding="utf-8")
        if _is_confirmed_capable(text):
            discovered.append(_posix_rel(path))

    missing: list[str] = []
    for rel in discovered:
        paired = any(rel in step and CONFIRMED_GREP in step for step in steps)
        if not paired:
            missing.append(rel)

    grep_count = workflow.count(CONFIRMED_GREP)
    assert not missing, (
        f"CONFIRMED-capable scripts missing a CONFIRMED grep step: {missing}; "
        f"discovered={discovered}; grep_count={grep_count}"
    )
    assert grep_count == len(discovered), (
        f"grep count {grep_count} != discovered {len(discovered)}: {discovered}"
    )


def test_inconclusive_only_scripts_are_not_grepped_confirmed() -> None:
    workflow = WORKFLOW.read_text(encoding="utf-8")
    steps = _workflow_steps(workflow)
    for path in _repro_py_files():
        text = path.read_text(encoding="utf-8")
        if _is_confirmed_capable(text):
            continue
        rel = _posix_rel(path)
        for step in steps:
            assert not (rel in step and CONFIRMED_GREP in step), (
                f"{rel} must not share a step with {CONFIRMED_GREP}"
            )
