"""On-demand GitHub agents exist and keep the science bans."""
from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

AGENT_FILES = (
    REPO_ROOT / ".github" / "agents" / "dev-fixer.agent.md",
    REPO_ROOT / ".github" / "agents" / "crosscheck-clerk.agent.md",
    REPO_ROOT / ".github" / "agents" / "page-editor.agent.md",
)
INSTRUCTIONS = REPO_ROOT / ".github" / "copilot-instructions.md"
FOUR = (*AGENT_FILES, INSTRUCTIONS)

FORBIDDEN_ASSIGNMENTS = (
    'result: "INCONCLUSIVE"',
    'result: "CONFIRMED"',
)


def _frontmatter(text: str) -> str:
    parts = text.split("---", 2)
    assert len(parts) >= 3, "missing frontmatter"
    return parts[1]


def test_agent_files_exist_with_descriptions() -> None:
    assert INSTRUCTIONS.is_file()
    for path in AGENT_FILES:
        assert path.is_file(), path
        front = _frontmatter(path.read_text(encoding="utf-8"))
        assert any(line.startswith("description:") for line in front.splitlines())


def test_combined_instructions_keep_the_bans() -> None:
    combined = "\n".join(path.read_text(encoding="utf-8") for path in FOUR)
    assert any(
        phrase in combined for phrase in ("Do not set", "Never set", "does not set")
    )
    for needle in ("confirmed", "15%", "Wave Factory", "needs-owner", "YAML"):
        assert needle in combined, needle


def test_agents_do_not_preset_results() -> None:
    for path in FOUR:
        text = path.read_text(encoding="utf-8")
        for bad in FORBIDDEN_ASSIGNMENTS:
            assert bad not in text, f"{path.name} contains {bad}"


def test_crew_doc_separates_on_demand_agents() -> None:
    crew = (REPO_ROOT / "docs" / "CREW.md").read_text(encoding="utf-8")
    assert "page-editor" in crew
    assert "not Night Crew" in crew or "are not Night Crew" in crew
