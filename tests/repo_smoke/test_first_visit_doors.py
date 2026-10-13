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


def test_visitor_add_copy_avoids_yaml_git() -> None:
    hub = (REPO_ROOT / "dashboard" / "index.html").read_text(encoding="utf-8")
    start = hub.find('id="first-contrib-heading"')
    end = hub.find("Policy tour")
    assert start != -1 and end > start
    chunk = hub[start:end].lower()
    for word in ("yaml", "pull request", "clone", "fork", "ci "):
        assert word not in chunk, f"visitor Add view still says {word!r}"


def test_hub_destination_nav() -> None:
    hub = (REPO_ROOT / "dashboard" / "index.html").read_text(encoding="utf-8")
    for token in (
        'data-view="home"',
        'data-view-link="map"',
        'href="#/map"',
        'href="#/search"',
        'href="#/add"',
        'data-hub-view="map"',
        'id="pathfinder"',
        'id="hub-search-launch"',
    ):
        assert token in hub, f"hub missing {token!r}"
    assert hub.count('class="hub-nav-wrap"') == 1 or hub.count("class=\"hub-nav-wrap\"") >= 1
    assert 'id="pathfinder"' in hub
    # Map is not the first paint; home is.
    home_at = hub.find('data-hub-view="home"')
    map_at = hub.find('data-hub-view="map"')
    assert 0 <= home_at < map_at


def test_what_you_are_looking_at_figure_links_out() -> None:
    fig = (REPO_ROOT / "docs" / "figures" / "what-usdr-is.svg").read_text(
        encoding="utf-8"
    )
    assert "What you are looking at" in fig
    assert "dashboard/#/map" in fig
    assert "dashboard/#/search" in fig
    assert "p-b-habitat-percolation-ecology-fss" in fig
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    assert "](https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/)" in readme


def test_visitor_search_stays_on_the_map() -> None:
    hub = (REPO_ROOT / "dashboard" / "index.html").read_text(encoding="utf-8")
    assert "Show on the map" in hub
    assert "We also call this Crosscheck" not in hub
    assert "Search open questions, claimed links, and testable ideas." in hub
    assert "window.usdrShowRecord = highlightNode" in hub
    assert "bridge: 'Claimed link'" in hub
    assert "unknown: 'Open question'" in hub
    assert "harvested · " not in hub
    assert "classList.contains('visitor-first')" in hub
    assert "flex-wrap: nowrap" in hub
    assert "chipsEl.hidden = typing" in hub
    assert "A few open questions. Type to search the rest." in hub
    assert "titles, claims, domains" not in hub
    assert "min-width: 12rem" in hub
    assert "renderPanel(d, {}, '', edges)" in hub
    assert "topNode.title || topNode.id" in hub


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
    assert 'id="home-lattice"' in hub
    assert "startHabitatPreview" in hub
