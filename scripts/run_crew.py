#!/usr/bin/env python3
"""USDR night crew — harvest (optional), scout, audit, brief. Never promote.

Roles
  Harvester  OpenAlex / PubMed / Semantic Scholar candidate JSON
  Scout      Wave Factory staged triples under drafts/wave_factory/ (gitignored)
  Auditor    canonical schemas + dry-run promote + quality audit
  Tester     Crosscheck *contracts* only (no Monte Carlo; no RESULT rewrite)
  Foreman    writes drafts/crew-reports/LATEST.md for a human

Never
  --apply on promote_wave_factory_batch.py
  write into cross-domain/, unknowns-catalog/, or hypotheses/ on its own
  emit or demand RESULT: CONFIRMED
"""
from __future__ import annotations

import argparse
import datetime as dt
import subprocess
import sys
from pathlib import Path
from typing import List, Sequence, Tuple

ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "drafts" / "crew-reports"
LATEST = REPORT_DIR / "LATEST.md"
STAGE = ROOT / "drafts" / "wave_factory"

HARVESTERS = (
    (
        "openalex",
        [
            sys.executable,
            str(ROOT / "scripts/harvesters/harvest_openalex.py"),
            "--bridge-scan",
            "--top",
            "20",
            "--output",
            "drafts/openalex_candidates.json",
        ],
    ),
    (
        "pubmed",
        [
            sys.executable,
            str(ROOT / "scripts/harvesters/harvest_pubmed.py"),
            "--bridge-scan",
            "--top",
            "20",
            "--output",
            "drafts/pubmed_candidates.json",
        ],
    ),
    (
        "semantic_scholar",
        [
            sys.executable,
            str(ROOT / "scripts/harvesters/harvest_semantic_scholar.py"),
            "--bridge-scan",
            "--top",
            "20",
            "--output",
            "drafts/semantic_scholar_candidates.json",
        ],
    ),
)


def run_cmd(argv: Sequence[str], timeout: int = 300) -> Tuple[int, str]:
    proc = subprocess.run(
        list(argv),
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=timeout,
        check=False,
    )
    out = (proc.stdout or "") + (proc.stderr or "")
    return proc.returncode, out


def harvest() -> List[str]:
    lines = ["## Harvester", ""]
    for name, argv in HARVESTERS:
        code, out = run_cmd(argv, timeout=180)
        tail = out.strip().splitlines()[-3:] if out.strip() else ["(no output)"]
        status = "ok" if code == 0 else f"failed (exit {code})"
        lines.append(f"- **{name}:** {status}")
        for t in tail:
            lines.append(f"  `{t[:200]}`")
    lines.append("")
    return lines


def scout(top: int, min_citations: int) -> List[str]:
    lines = ["## Scout (Wave Factory)", ""]
    argv = [
        sys.executable,
        str(ROOT / "scripts/harvesters/wave_factory.py"),
        "--top",
        str(top),
        "--min-citations",
        str(min_citations),
        "--sources",
        "openalex,pubmed,semantic_scholar",
        "--output",
        "drafts/wave_factory",
    ]
    code, out = run_cmd(argv, timeout=180)
    n_b = len(list((STAGE / "cross-domain").rglob("b-*.yaml"))) if STAGE.exists() else 0
    n_u = len(list((STAGE / "unknowns-catalog").rglob("u-*.yaml"))) if STAGE.exists() else 0
    n_h = len(list((STAGE / "hypotheses" / "active").rglob("h-*.yaml"))) if STAGE.exists() else 0
    lines.append(f"- wave_factory exit **{code}**")
    lines.append(f"- staged (gitignored): bridges={n_b}, unknowns={n_u}, hypotheses={n_h}")
    lines.append("- these are **candidates**, not findings. Human review before promote.")
    if out.strip():
        for t in out.strip().splitlines()[-8:]:
            lines.append(f"  `{t[:200]}`")
    lines.append("")
    return lines


def auditor() -> List[str]:
    lines = ["## Auditor", ""]
    code_s, out_s = run_cmd(
        [sys.executable, str(ROOT / "scripts/validate_schemas.py")], timeout=180
    )
    lines.append(f"- `validate_schemas.py` exit **{code_s}**")
    if out_s.strip():
        lines.append(f"  `{out_s.strip().splitlines()[-1][:240]}`")

    promote = ROOT / "scripts/harvesters/promote_wave_factory_batch.py"
    code_p, out_p = run_cmd(
        [sys.executable, str(promote), "--stage", "drafts/wave_factory"], timeout=120
    )
    lines.append(f"- `promote_wave_factory_batch.py` dry-run exit **{code_p}** (never `--apply`)")
    for t in (out_p.strip().splitlines()[-4:] if out_p.strip() else []):
        lines.append(f"  `{t[:200]}`")

    qpath = REPORT_DIR / "quality.md"
    code_q, out_q = run_cmd(
        [
            sys.executable,
            str(ROOT / "scripts/audit_quality.py"),
            "--report",
            str(qpath.relative_to(ROOT).as_posix()),
        ],
        timeout=180,
    )
    lines.append(f"- `audit_quality.py` exit **{code_q}**")
    for t in (out_q.strip().splitlines()[-6:] if out_q.strip() else []):
        if t.strip():
            lines.append(f"  `{t[:200]}`")
    lines.append("")
    return lines


def tester_contracts() -> List[str]:
    """Static Crosscheck honesty checks. No Monte Carlo."""
    lines = ["## Tester (contracts only — no live exponent run)", ""]
    js = ROOT / "repro/p-b-habitat-percolation-ecology-fss/simulate_percolation_fss.js"
    py = ROOT / "repro/p-b-habitat-percolation-ecology-fss/simulate_percolation_fss.py"
    js_txt = js.read_text(encoding="utf-8") if js.is_file() else ""
    py_txt = py.read_text(encoding="utf-8") if py.is_file() else ""
    js_ok = 'result: "INCONCLUSIVE"' in js_txt and 'result: "CONFIRMED"' not in js_txt
    py_ok = "mean-first-either-wrap" in py_txt or "first wrapping in either direction" in py_txt
    lines.append(f"- habitat JS cannot emit CONFIRMED: **{'yes' if js_ok else 'NO — fix'}**")
    lines.append(f"- habitat Python either-wrap estimator present: **{'yes' if py_ok else 'NO — check'}**")
    workflow = ROOT / ".github/workflows/crosscheck-repro.yml"
    wf = workflow.read_text(encoding="utf-8") if workflow.is_file() else ""
    lines.append(
        f"- Crosscheck CI workflow present: **{'yes' if 'RESULT: CONFIRMED' in wf else 'missing'}**"
    )
    lines.append("- live Crosscheck Monte Carlo is **not** this crew's job (too long; human/CI).")
    lines.append("")
    return lines


def write_report(sections: List[str], skip_harvest: bool, skip_scout: bool) -> Path:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    parts = [
        "# USDR crew briefing",
        "",
        f"Generated **{now}**. Foreman only; not a scientific result.",
        "",
        "**Do not promote this run to `cross-domain/`, `unknowns-catalog/`, or `hypotheses/` without a human.**",
        "Wave Factory output stays in gitignored `drafts/wave_factory/`.",
        "",
        f"Flags: skip_harvest={skip_harvest}, skip_scout={skip_scout}",
        "",
    ]
    parts.extend(sections)
    parts.extend(
        [
            "## What you do next",
            "",
            "1. Read this briefing (and the bot PR if one opened).",
            "2. Open interesting staged YAML under `drafts/wave_factory/` locally.",
            "3. If a triple is real math, promote with "
            "`python scripts/harvesters/promote_wave_factory_batch.py --stage drafts/wave_factory --apply` "
            "**after** you edited the translation table — never blindly.",
            "4. Do not loosen Crosscheck gates so the night job looks greener.",
            "",
        ]
    )
    text = "\n".join(parts)
    LATEST.write_text(text, encoding="utf-8")
    return LATEST


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="USDR night crew (never promotes)")
    p.add_argument("--skip-harvest", action="store_true")
    p.add_argument("--skip-scout", action="store_true", help="Skip Wave Factory (offline audit+brief)")
    p.add_argument("--top", type=int, default=30)
    p.add_argument("--min-citations", type=int, default=50)
    return p.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    sections: List[str] = []
    if not args.skip_harvest:
        sections.extend(harvest())
    else:
        sections.extend(["## Harvester", "", "- skipped (`--skip-harvest`)", ""])
    if not args.skip_scout:
        sections.extend(scout(args.top, args.min_citations))
    else:
        sections.extend(["## Scout (Wave Factory)", "", "- skipped (`--skip-scout`)", ""])
    sections.extend(auditor())
    sections.extend(tester_contracts())
    path = write_report(sections, args.skip_harvest, args.skip_scout)
    print(path.read_text(encoding="utf-8"))
    print(f"[crew] wrote {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
