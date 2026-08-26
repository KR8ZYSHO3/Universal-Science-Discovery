---
phase: 4
slug: ci-trust-hardening
status: approved
nyquist_compliant: true
wave_0_complete: false
created: 2026-08-26
---

# Phase 4 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

Existing pytest (`tests/repo_smoke`) + `validate-schemas.yml` cover epidemic freeze and catalog smokes. Wave 0 adds two new test files; do not install a new framework.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | pytest 8.4.2 (CI unpinned `pytest`) |
| **Config file** | `pyproject.toml` `[tool.pytest.ini_options]` |
| **Quick run command** | `python -m pytest tests/repo_smoke/test_crosscheck_confirmed_gates.py tests/repo_smoke/test_crosscheck_entry_points.py tests/repo_smoke/test_crosscheck_repro_regression.py::test_epidemic_fss_fit_confirmed_on_reference_pcs -x` |
| **Full suite command** | `python -m pytest tests/repo_smoke -v --tb=short` |
| **Estimated runtime** | <30s for quick run; full repo_smoke includes pre-existing cluster pooled histogram |

Also after `docs/` edits: `mkdocs build --strict`.

---

## Sampling Rate

- **After every task commit:** Run that task's `<automated>` command (quick run if the new files exist)
- **After every plan wave:** `python -m pytest tests/repo_smoke -v --tb=short`
- **Before `/gsd-verify-work`:** Full repo_smoke green + `mkdocs build --strict` if `docs/` changed
- **Max feedback latency:** 30 seconds for the quick command (do not locally re-run live `crosscheck-repro.yml` Monte Carlo)

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Threat Ref | Secure Behavior | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|------------|-----------------|-----------|-------------------|-------------|--------|
| 04-01-01 | 01 | 1 | TRUST-02 | T-04-01 | Inventory reads committed files; no `yaml.safe_load` of workflow; no `shell=True` | unit | `python -m pytest tests/repo_smoke/test_crosscheck_confirmed_gates.py -x` | ❌ W0 | ⬜ pending |
| 04-01-02 | 01 | 1 | TRUST-02 | T-04-02 | GCC never shares a CONFIRMED grep step | unit (negative) | same file | ❌ W0 | ⬜ pending |
| 04-01-03 | 01 | 1 | TRUST-02 | — | Docs state CONFIRMED-only grep policy | docs | `mkdocs build --strict` | ✅ CROSSCHECK.md | ⬜ pending |
| 04-02-01 | 02 | 2 | TRUST-03 | T-04-03 | `--dry-run` only; list argv; no `--write` | smoke | `python -m pytest tests/repo_smoke/test_crosscheck_entry_points.py -x` | ❌ W0 | ⬜ pending |
| 04-02-02 | 02 | 2 | TRUST-03 | T-04-04 | GCC asserts INCONCLUSIVE + exit 0 | smoke | same file | ❌ W0 | ⬜ pending |
| 04-02-03 | 02 | 2 | TRUST-03 | — | Keep epidemic freeze `NU_THEORY == 3.0` | unit (existing) | `python -m pytest tests/repo_smoke/test_crosscheck_repro_regression.py::test_epidemic_fss_fit_confirmed_on_reference_pcs -x` | ✅ | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

- [ ] `tests/repo_smoke/test_crosscheck_confirmed_gates.py` — TRUST-02 inventory + negative GCC assertion
- [ ] `tests/repo_smoke/test_crosscheck_entry_points.py` — TRUST-03 generate dry-run + GCC subprocess
- [ ] Framework install: none — pytest + PyYAML already in `validate-schemas.yml`

Existing infrastructure covers epidemic TRUST-03 (`test_epidemic_fss_fit_confirmed_on_reference_pcs`). Cluster live `collect_pooled_sizes()` is a pre-existing anti-pattern — do not “fix” it this phase.

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Live four-seed CONFIRMED greps on GitHub Actions | TRUST-02 / D-02 | Needs networkx + minutes of Monte Carlo; inventory pytest is the local stand-in | After merge, confirm `crosscheck-repro.yml` still has four `grep -q "RESULT: CONFIRMED"` steps and the workflow run is green when those paths change |

All new phase behaviors have automated verification. The table above is a **post-merge** sanity check, not a planner task.

---

## Validation Sign-Off

- [x] All tasks have `<automated>` verify or Wave 0 dependencies
- [x] Sampling continuity: no 3 consecutive tasks without automated verify
- [x] Wave 0 covers all MISSING references
- [x] No watch-mode flags
- [x] Feedback latency < 30s for the quick command
- [x] `nyquist_compliant: true` set in frontmatter

**Approval:** approved 2026-08-26 (plan-checker pass after 1 revision: 04-01 task 2 verify)
