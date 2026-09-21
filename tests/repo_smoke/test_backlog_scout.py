"""Backlog scout finds work; never promotes science."""
from __future__ import annotations

import importlib.util
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


def _load():
    import sys

    path = REPO_ROOT / "scripts" / "backlog_scout.py"
    spec = importlib.util.spec_from_file_location("backlog_scout", path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def test_scout_script_never_promotes() -> None:
    text = (REPO_ROOT / "scripts" / "backlog_scout.py").read_text(encoding="utf-8")
    assert '"--apply"' not in text
    assert "promote_wave_factory_batch" not in text
    assert "status: confirmed" not in text.lower() or "Do not set" in text or "invent CONFIRMED" in text


def test_scout_collects_findings_and_writes_report(tmp_path: Path) -> None:
    mod = _load()
    findings = mod.collect()
    assert isinstance(findings, list)
    fps = {f.fingerprint for f in findings}
    assert len(fps) == len(findings)
    out = tmp_path / "SCOUT.md"
    report = mod.render_report(findings, [])
    out.write_text(report, encoding="utf-8")
    assert "Backlog scout" in report
    assert "invent CONFIRMED" in report


def test_v13_ui01_is_a_finding_until_audit_exists() -> None:
    mod = _load()
    titles = [f.title for f in mod.scan_v13_gaps()]
    assert any(t.startswith("UI-01") for t in titles)
    assert any(t.startswith("ROBUST-01") for t in titles)
