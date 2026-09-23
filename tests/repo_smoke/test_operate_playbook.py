"""OPERATE.md is the single operator list; named scripts exist."""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
OPERATE = REPO_ROOT / "docs" / "OPERATE.md"
FORBIDDEN = ("arxiv", "reddit", "linkedin", "usdr.science", "cold-email")


def test_operate_md_exists_and_is_the_short_list() -> None:
    text = OPERATE.read_text(encoding="utf-8")
    assert "python scripts/validate_schemas.py" in text
    assert "python scripts/verify_dashboard_consistency.py" in text
    assert "apply_crosscheck_result.py" in text
    assert "Skip if" in text
    before, _, after = text.lower().partition("## do not")
    for word in FORBIDDEN:
        assert word not in before, f"launch/outreach in the run list: {word}"
    assert "do not" in after or after is not None


def test_operate_md_scripts_exist() -> None:
    text = OPERATE.read_text(encoding="utf-8")
    names = set(re.findall(r"python(?:\s+-X\s+utf8)?\s+scripts/([a-z0-9_./-]+\.py)", text))
    assert names, "expected at least one scripts/*.py command"
    for name in names:
        path = REPO_ROOT / "scripts" / name
        assert path.is_file(), f"OPERATE.md cites missing {path}"


def test_catalog_batch_is_one_run() -> None:
    text = (REPO_ROOT / "docs" / "CATALOG_BATCH.md").read_text(encoding="utf-8")
    for needle in (
        "python scripts/validate_schemas.py",
        "python -X utf8 scripts/build_graph.py",
        "python scripts/update_dashboard_stats.py --apply",
        "python scripts/verify_dashboard_consistency.py",
        "status: confirmed",
        "PATH_TO_SUCCESS.md",
    ):
        assert needle in text
    before, _, _after = text.lower().partition("## do not")
    for word in ("arxiv", "reddit", "linkedin"):
        assert word not in before
    assert "Do not push straight to `main`" in text


def test_use_md_points_at_operate() -> None:
    use = (REPO_ROOT / "docs" / "USE.md").read_text(encoding="utf-8")
    assert "OPERATE.md" in use
