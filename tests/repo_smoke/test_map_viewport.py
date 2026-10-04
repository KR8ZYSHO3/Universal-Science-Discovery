"""The computer map is one screen. The wheel moves that map."""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
HUB = REPO_ROOT / "dashboard" / "index.html"


def test_desktop_map_fills_the_screen_and_wheel_pans() -> None:
    html = HUB.read_text(encoding="utf-8")
    assert "height: calc(100dvh - var(--nav-h))" in html
    assert "height: auto !important" in html
    assert "svg.on('wheel.zoom', null)" in html
    assert "zoomBehavior.translateBy" in html
    assert "scroll to move" in html
    start = html.index('body[data-view="map"] #graph-container')
    block = html[start:start + 1600]
    desktop_rule, phone_rule = block.split("@media (max-width: 640px)", 1)
    assert "height: auto !important" in desktop_rule
    assert "height: 100vh !important" not in desktop_rule
    assert "height: 100vh !important" in phone_rule
    assert "touch-action: pan-y" in phone_rule
