"""Smoke tests for hub first-visit audit (UI-01)."""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
DASHBOARD = REPO_ROOT / "dashboard" / "index.html"
API_DIR = REPO_ROOT / "api" / "v1"

REQUIRED_SECTIONS = (
    "start",
    "crosscheck",
    "catalog-search",
    "impact-router",
    "orphan-unknowns-panel",
    "ai-copilot",
    "developer-api",
    "knowledge-graph",
)

STALE_PATTERNS = (
    r"\b401 catalog entries\b",
    r"\bThree scripts that continuously mine\b",
)

REQUIRED_API_ENDPOINTS = (
    "meta.json",
    "bridges.json",
    "unknowns.json",
    "hypotheses.json",
    "breakthrough_gaps.json",
    "domains.json",
    "graph.json",
    "bridge_proposals.json",
    "orphan_xref_panel.json",
    "orphan_unknowns_panel.json",
)


def _dashboard_html() -> str:
    assert DASHBOARD.is_file(), "dashboard/index.html missing"
    return DASHBOARD.read_text(encoding="utf-8")


def test_dashboard_required_sections_present() -> None:
    html = _dashboard_html()
    for section_id in REQUIRED_SECTIONS:
        assert f'id="{section_id}"' in html, f"missing hub section #{section_id}"


def test_dashboard_no_stale_first_visit_copy() -> None:
    html = _dashboard_html()
    for pattern in STALE_PATTERNS:
        assert not re.search(pattern, html, re.IGNORECASE), f"stale hub copy matched: {pattern}"


def test_dashboard_developer_api_endpoints_exist() -> None:
    html = _dashboard_html()
    for filename in REQUIRED_API_ENDPOINTS:
        href = f"../api/v1/{filename}"
        assert href in html, f"developer API section missing link to {href}"
        api_path = API_DIR / filename
        assert api_path.is_file(), f"{api_path} missing — regenerate API artifacts"


def test_dashboard_discovery_loop_links_present() -> None:
    html = _dashboard_html()
    assert 'href="#impact-router"' in html
    assert 'href="#orphan-unknowns-panel"' in html
    assert "From gap to proof" in html
    assert "Pathfinder" in html