---
phase: 5
slug: hub-engineering
status: approved
nyquist_compliant: true
wave_0_complete: false
created: 2026-08-26
---

# Phase 5 — Validation Strategy

Existing pytest (`tests/repo_smoke`) + `verify_dashboard_consistency.py` + `mkdocs build --strict` cover Wave 0 mechanism. Add one smoke function to `test_catalog_regression.py`.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | pytest 8.4.2 |
| **Config file** | `pyproject.toml` `[tool.pytest.ini_options]` |
| **Quick run command** | `python -m pytest tests/repo_smoke/test_catalog_regression.py::test_recommendations_json -q` |
| **Full suite command** | `python -m pytest tests/repo_smoke -v --tb=short` |
| **Estimated runtime** | seconds (no Monte Carlo) |

Also: `python scripts/verify_dashboard_consistency.py`; `mkdocs build --strict` after docs/nav edits.

---

## Sampling Rate

- **After every task commit:** that task's `<automated>` command
- **After every plan wave:** full `tests/repo_smoke`
- **Before `/gsd-verify-work`:** repo_smoke + dashboard consistency + mkdocs if docs changed
- **Max feedback latency:** 30 seconds for the quick command

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Threat Ref | Secure Behavior | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|------------|-----------------|-----------|-------------------|-------------|--------|
| 05-01-01 | 01 | 1 | HUB-01 | T-05-03 | Spec names three signals; v1 = undirected_degree; not scientific ranking | docs | `mkdocs build --strict` | ❌ W0 | ⬜ pending |
| 05-01-02 | 01 | 1 | HUB-01 | T-05-02 | Exporter builds github.com URLs only; scores are ints | smoke | `python scripts/export_recommendations.py` then pytest `test_recommendations_json` | ❌ W0 | ⬜ pending |
| 05-01-03 | 01 | 1 | HUB-01 | T-05-01 | Hub uses `textContent`; hrefs github.com only | consistency | `python scripts/verify_dashboard_consistency.py` | ✅ script | ⬜ pending |

---

## Wave 0 Requirements

- [ ] `tests/repo_smoke/test_catalog_regression.py::test_recommendations_json`
- [ ] Framework install: none

Existing infrastructure covers epidemic/Crosscheck; do not add those tests here.

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Hub section visible over HTTP | HUB-01 | Fetch + DOM | `python -m http.server 8765` → `http://localhost:8765/dashboard/#recommendations` |

---

## Validation Sign-Off

- [x] All tasks have `<automated>` verify or Wave 0 dependencies
- [x] Sampling continuity
- [x] Wave 0 covers MISSING references
- [x] No watch-mode flags
- [x] Feedback latency < 30s
- [x] `nyquist_compliant: true` set in frontmatter

**Approval:** approved 2026-08-26 (plan-checker pass)
