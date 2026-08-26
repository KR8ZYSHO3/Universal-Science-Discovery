---
phase: 2
slug: epidemic-fss-precision
status: approved
nyquist_compliant: true
wave_0_complete: true
created: 2026-08-26
---

# Phase 2 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | pytest (already in `validate-schemas.yml`) |
| **Config file** | none — `python -m pytest tests/repo_smoke` |
| **Quick run command** | `python -m pytest tests/repo_smoke/test_crosscheck_repro_regression.py -q` |
| **Full suite command** | `python -m pytest tests/repo_smoke -q`; `python scripts/validate_schemas.py`; `python scripts/build_crosscheck.py --check` after YAML edits |
| **Estimated runtime** | fit regression: milliseconds; full Monte Carlo: seconds–~1 min after `fast_gnp` |

Existing infrastructure covers Wave 0. Do **not** add a live NetworkX sweep to `tests/repo_smoke`.

---

## Sampling Rate

- **After every task commit:** task `<automated>` command
- **After every plan wave:** `python -m pytest tests/repo_smoke -q`
- **Before `/gsd-verify-work`:** repo_smoke green + local script prints `RESULT: CONFIRMED` + `--check` if YAML changed
- **Max feedback latency:** 30 seconds for pytest; Monte Carlo gated to 02-01 task 2 only

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Threat Ref | Secure Behavior | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|------------|-----------------|-----------|-------------------|-------------|--------|
| 02-01-01 | 01 | 1 | CROSS-04 | T-2-01 | Lazy nx; signed fit vs PC_INF=1/6; NU_THEORY=3 | unit | `python -c` AST + synthetic `fit_nu` in 02-01-PLAN | ✅ | ⬜ pending |
| 02-01-02 | 01 | 1 | CROSS-04 | T-2-01 | Stdout CONFIRMED + SUMMARY freeze | MC + grep | subprocess run of epidemic script asserts `RESULT: CONFIRMED` and `CONFIRMED_FREEZE` | ✅ | ⬜ pending |
| 02-02-01 | 02 | 2 | CROSS-04 | T-2-02 | Frozen p_c vector; no live MC | unit | `pytest ...::test_epidemic_fss_fit_confirmed_on_reference_pcs -q` | ❌ add in 02 | ⬜ pending |
| 02-02-02 | 02 | 2 | CROSS-04 | T-2-08 | CI greps stdout | config | python -c asserts tee+grep in workflow | ✅ | ⬜ pending |
| 02-03-01 | 03 | 2 | CROSS-04 | T-2-11 | YAML honesty; schema valid | schema | yaml string asserts + `python scripts/validate_schemas.py` | ✅ | ⬜ pending |
| 02-03-02 | 03 | 2 | ROADMAP-2.3 | — | Colab still calls canonical `.py` | grep | README + notebook python -c | ✅ | ⬜ pending |
| 02-03-03 | 03 | 2 | D-08 | — | Generated pages match YAML | drift | `python scripts/build_crosscheck.py --check` | ✅ | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

Existing infrastructure covers all phase requirements.

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Hosted Colab kernel | ROADMAP-2.3 | Requires Google account | Optional after merge. Automated substitute: notebook still invokes `python epidemic_percolation_fss.py`. |

---

## Validation Sign-Off

- [x] All tasks have `<automated>` verify
- [x] Sampling continuity: no 3 consecutive tasks without automated verify
- [x] Wave 0 covers all MISSING references
- [x] No watch-mode flags
- [x] 02-01-02 `<automated>` fails unless stdout contains `RESULT: CONFIRMED`
- [x] `nyquist_compliant: true`

**Approval:** 2026-08-26 (post checker revision)
