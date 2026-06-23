# Requirements: USDR Launch Execution (v1.1)

**Defined:** 2026-06-23
**Core Value:** Researchers can run falsifiable Crosscheck experiments in minutes.

## v1.1 Requirements (Launch Execution milestone)

### Crosscheck credibility

- [x] **CROSS-01**: Habitat percolation FSS repro prints `RESULT: CONFIRMED` — Phase 1 (#298)
- [x] **CROSS-02**: Ising EWI repro prints `RESULT: CONFIRMED` — Phase 1 (#297)
- [x] **CROSS-03**: Cluster exponent repro prints `RESULT: CONFIRMED` — Phase 1 (#302)
- [ ] **CROSS-04**: Epidemic FSS repro prints `RESULT: CONFIRMED` — Phase 5
- [x] **CROSS-05**: `build_crosscheck.py --check` in CI with regression tests — Phase 1 (#299–#301)

### Launch execution (human-calendar)

- [ ] **LAUNCH-01**: Public posts live with accurate Crosscheck outcomes (3 CONFIRMED) — Phase 2
- [ ] **LAUNCH-02**: Reddit r/OpenScience post from approved copy — Phase 2
- [ ] **LAUNCH-03**: `usdr.science` DNS + GitHub Pages HTTPS — Phase 3
- [ ] **LAUNCH-04**: arXiv preprint v1.2 submitted — Phase 3
- [ ] **LAUNCH-05**: 5 personal DMs to cited authors — Phase 4
- [ ] **LAUNCH-06**: First external contributor signal documented — Phase 4

### Trust surfaces

- [x] **TRUST-01**: Stale `dashboard/knowledge_graph.json` removed; single graph source — Phase 1 (#300)
- [ ] **TRUST-02**: Outreach/preprint numbers match `verify_dashboard_consistency.py` — Phase 2–3

## v2 Requirements (deferred)

- Bounded content wave from `drafts/` (maintainer review gate)
- Dashboard Phase C smart recommendations
- LinkedIn institutional prospectus campaign

## Out of Scope

| Feature | Reason |
|---------|--------|
| New bridge waves during launch sprint | Focus external traction first |
| GSD as contributor requirement | Optional maintainer tooling only |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| CROSS-01–03, CROSS-05, TRUST-01 | Phase 1 | Complete |
| LAUNCH-01, LAUNCH-02, TRUST-02 | Phase 2 | Pending |
| LAUNCH-03, LAUNCH-04 | Phase 3 | Pending |
| LAUNCH-05, LAUNCH-06 | Phase 4 | Pending |
| CROSS-04 | Phase 5 | Pending |

**Coverage:** 11 v1.1 requirements · 6 mapped complete · 5 pending

---
*Requirements defined: 2026-06-23 · GSD bootstrap from LAUNCH_PLAYBOOK + session PRs #297–#302*