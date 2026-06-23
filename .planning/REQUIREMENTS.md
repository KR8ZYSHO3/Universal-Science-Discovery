# Requirements: USDR Core Development (v1.1)

**Defined:** 2026-06-23
**Core Value:** Researchers can run falsifiable Crosscheck experiments in minutes.
**Reprioritized:** 2026-06-23 — marketing deferred to v1.2 Launch.

## v1.1 Requirements (Core Development)

### Crosscheck credibility

- [x] **CROSS-01**: Habitat percolation FSS CONFIRMED — Phase 1 (#298)
- [x] **CROSS-02**: Ising EWI CONFIRMED — Phase 1 (#297)
- [x] **CROSS-03**: Cluster exponent CONFIRMED — Phase 1 (#302)
- [ ] **CROSS-04**: Epidemic FSS CONFIRMED — Phase 2
- [x] **CROSS-05**: `build_crosscheck.py --check` in CI — Phase 1 (#299–#301)

### Crosscheck scale-up

- [ ] **CROSS-06**: Second-bridge protocol drafts promoted or generated via `generate_crosscheck.py` — Phase 3
- [ ] **CROSS-07**: Browser runner outputs documented vs Python canonical (parity matrix) — Phase 3

### Trust surfaces & CI

- [x] **TRUST-01**: Stale dashboard graph removed — Phase 1 (#300)
- [ ] **TRUST-02**: All CONFIRMED protocols gated in `crosscheck-repro.yml` — Phase 4
- [ ] **TRUST-03**: Additional repo_smoke tests for epidemic + script entry points — Phase 4

### Hub engineering

- [ ] **HUB-01**: Smart-recommendations spec + static JSON prototype — Phase 5

## v1.2 Requirements (Launch — deferred)

- **LAUNCH-01** through **LAUNCH-06**: outreach, DNS, arXiv, DMs — see `LAUNCH_PLAYBOOK.md`
- Parked until v1.1 Core Development milestone completes

## Out of Scope

| Feature | Reason |
|---------|--------|
| Marketing posts | Owner: development first (2026-06-23) |
| Catalog waves | After Crosscheck + trust surfaces |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| CROSS-01–03, CROSS-05, TRUST-01 | Phase 1 | Complete |
| CROSS-04 | Phase 2 | Pending |
| CROSS-06, CROSS-07 | Phase 3 | Pending |
| TRUST-02, TRUST-03 | Phase 4 | Pending |
| HUB-01 | Phase 5 | Pending |

**Coverage:** 10 v1.1 dev requirements · 5 complete · 5 pending

---
*Last updated: 2026-06-23 — marketing requirements moved to v1.2*