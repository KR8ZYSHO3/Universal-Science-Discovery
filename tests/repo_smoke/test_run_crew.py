"""Night crew: briefing exists; never promotes; skip harvest/scout is fast."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CREW = REPO_ROOT / "scripts" / "run_crew.py"


def test_run_crew_script_never_applies_wave_factory() -> None:
    text = CREW.read_text(encoding="utf-8")
    assert "promote_wave_factory_batch.py" in text
    wf = text.split("promote_wave_factory_batch.py", 1)[1][:500]
    assert "--apply" not in wf
    assert "demand RESULT: CONFIRMED" in text
    assert "--land-unknowns" in text


def test_run_crew_skip_harvest_skip_scout_writes_briefing() -> None:
    cmd = [
        sys.executable,
        str(CREW),
        "--skip-harvest",
        "--skip-scout",
    ]
    proc = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True, check=False)
    assert proc.returncode == 0, (proc.stdout or "") + (proc.stderr or "")
    latest = REPO_ROOT / "drafts" / "crew-reports" / "LATEST.md"
    assert latest.is_file()
    body = latest.read_text(encoding="utf-8")
    assert "Foreman" in body or "crew briefing" in body.lower()
    assert "not auto-promoted" in body or "bridges" in body.lower()
    assert "--apply" not in cmd


def test_crew_ship_allowlist_mailbox_only() -> None:
    import importlib.util

    path = REPO_ROOT / "scripts" / "crew_ship.py"
    spec = importlib.util.spec_from_file_location("crew_ship", path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    ok, _ = mod.shippable(
        [
            "drafts/openalex_candidates.json",
            "drafts/crew-reports/LATEST.md",
            "unknowns-catalog/biophysics/u-gap-example-deadbeef.yaml",
        ]
    )
    assert ok
    hand, why = mod.shippable(["unknowns-catalog/physics/u-habitat-fragmentation.yaml"])
    assert not hand
    bad, reason = mod.shippable(["cross-domain/physics-ecology/b-habitat-percolation-ecology.yaml"])
    assert not bad
    assert "science path" in reason
    bad2, reason2 = mod.shippable(["repro/p-b-habitat-percolation-ecology-fss/simulate_percolation_fss.py"])
    assert not bad2
    assert "science path" in reason2
