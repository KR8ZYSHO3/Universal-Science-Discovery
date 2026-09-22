"""WORK-01: RESULT write-through does not invent CONFIRMED or rewrite YAML status."""
from __future__ import annotations

import importlib.util
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


def _load():
    path = REPO_ROOT / "scripts" / "apply_crosscheck_result.py"
    spec = importlib.util.spec_from_file_location("apply_crosscheck_result", path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_parse_result_takes_last_token() -> None:
    mod = _load()
    text = "noise\nRESULT: INCONCLUSIVE (smoke)\nRESULT: CONFIRMED\n"
    assert mod.parse_result(text) == "CONFIRMED"
    assert mod.parse_result("RESULT: INCONCLUSIVE\n") == "INCONCLUSIVE"
    assert mod.parse_result("no token here") is None


def test_apply_result_does_not_change_status_or_invent_confirmed() -> None:
    mod = _load()
    src = "id: p-b-example\nstatus: ready\ntitle: hello\n"
    out = mod.apply_result(src, "INCONCLUSIVE", "2026-08-27")
    assert "status: ready" in out
    assert "status: confirmed" not in out
    assert "last_run_result: INCONCLUSIVE" in out
    assert 'last_run_at: "2026-08-27"' in out


def test_hub_cards_show_last_run_without_promoting_status() -> None:
    import importlib.util
    import sys

    scripts = str(REPO_ROOT / "scripts")
    if scripts not in sys.path:
        sys.path.insert(0, scripts)
    path = REPO_ROOT / "scripts" / "render_crosscheck_hub.py"
    spec = importlib.util.spec_from_file_location("render_crosscheck_hub", path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    proto = {
        "id": "p-b-percolation-oncology-gcc",
        "title": "Synthetic-lattice giant-component fraction",
        "status": "ready",
        "last_run_result": "INCONCLUSIVE",
        "source_bridge": "b-percolation-oncology",
        "feasibility_tier": "desktop",
        "repro_bundle": "repro/p-b-percolation-oncology-gcc",
        "_bundle_dir": REPO_ROOT / "repro/p-b-percolation-oncology-gcc",
    }
    html = mod.render_cards([proto])
    assert "ready" in html
    assert "last run: INCONCLUSIVE" in html
    assert "confirmed" not in html.lower() or "last run: CONFIRMED" not in html
