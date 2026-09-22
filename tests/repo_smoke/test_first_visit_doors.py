"""Hub #start and docs/USE.md must use the same three door titles."""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
DOORS = (
    "Run the test",
    "See how two fields connect",
    "Add an open question",
)


def test_use_md_and_hub_share_door_titles() -> None:
    hub = (REPO_ROOT / "dashboard" / "index.html").read_text(encoding="utf-8")
    use = (REPO_ROOT / "docs" / "USE.md").read_text(encoding="utf-8")
    figure = (REPO_ROOT / "docs" / "figures" / "use-three-doors.svg").read_text(
        encoding="utf-8"
    )
    for title in DOORS:
        assert title in hub, f"hub missing door {title!r}"
        assert title in use, f"USE.md missing door {title!r}"
    assert "Run the test" in figure
    assert "connect" in figure
    assert "Add an open" in figure
    assert "Try an experiment" not in use
    assert "Try an experiment" not in figure


def test_habitat_first_test_landing_exists() -> None:
    landing = (
        REPO_ROOT
        / "repro"
        / "p-b-habitat-percolation-ecology-fss"
        / "index.html"
    )
    assert landing.is_file()
    hub = (REPO_ROOT / "dashboard" / "index.html").read_text(encoding="utf-8")
    assert "p-b-habitat-percolation-ecology-fss/index.html" in hub
