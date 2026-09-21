"""Gap miner stages stated unknowns; does not promote bridges."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


def _load():
    path = REPO_ROOT / "scripts" / "harvesters" / "mine_unknowns.py"
    spec = importlib.util.spec_from_file_location("mine_unknowns", path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def test_mine_hits_gap_language_and_skips_solved_sounding_titles() -> None:
    mod = _load()
    candidates = [
        {
            "title": "The mechanism of X remains unknown in vivo",
            "doi": "10.9999/gap-test-unknown-miner",
            "abstract_snippet": "Little is known about transport across the barrier.",
            "concepts": ["Biophysics", "Cell biology"],
            "source": "test",
            "year": 2024,
        },
        {
            "title": "Deep Residual Learning for Image Recognition",
            "doi": "10.1109/cvpr.2016.90",
            "abstract_snippet": "We present a residual learning framework to ease training.",
            "concepts": ["Computer science"],
            "source": "test",
            "year": 2016,
        },
    ]
    hits = mod.mine(candidates, top=10)
    assert len(hits) == 1
    assert hits[0]["status"] == "open"
    assert hits[0]["id"].startswith("u-gap-")
    assert "HARVESTED" in hits[0]["summary"]


def test_promote_unknowns_script_has_apply_but_crew_does_not_pass_it() -> None:
    crew = (REPO_ROOT / "scripts" / "run_crew.py").read_text(encoding="utf-8")
    assert "mine_unknowns.py" in crew
    assert "promote_unknowns.py" in crew
    assert '"--apply"' not in crew
    assert "'--apply'" not in crew
    promote = (REPO_ROOT / "scripts" / "harvesters" / "promote_unknowns.py").read_text(
        encoding="utf-8"
    )
    assert "Never moves bridges" in promote or "never moves bridges" in promote.lower()
