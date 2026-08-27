# Requirements: USDR v1.3 University-ready robustness

**Defined:** 2026-08-26
**Core Value:** Researchers can run falsifiable Crosscheck experiments in minutes.

v1.1 Core Development (11/11) → [milestones/v1.1-REQUIREMENTS.md](milestones/v1.1-REQUIREMENTS.md)

Product path (not this file): repo-root [ROADMAP.md](../ROADMAP.md). This file is the GSD requirement list for **v1.3 only**.

## v1.3 Requirements

### Closed loop

- [ ] **WORK-01**: After a documented Crosscheck run, catalog YAML and hub Crosscheck surfaces show the same RESULT token the protocol printed (or an explicit pending/apply state), without fabricating CONFIRMED

### Simple flow

- [ ] **FLOW-01**: A newcomer can pick Look, Add, or Run from [docs/USE.md](../docs/USE.md) and the hub `#start` section without reading a stack of strategy docs

### Hub first visit

- [ ] **UI-01**: A first visit to the hub shows git-consistent counts, working Crosscheck links, and no broken first-visit loads

### Maintainer ops

- [ ] **ROBUST-01**: A new maintainer can operate the repo from one ordered command list (clone → validate → graph/hub preview → Crosscheck)
- [ ] **WORK-02**: A catalog batch can be completed as one documented local run (validate → graph → consistency → PR-sized change)

## Future Requirements

Deferred; not in v1.3 phases.

### Launch (v1.2 — parked)

- **LAUNCH-01**: arXiv preprint submitted with a citable DOI
- **LAUNCH-02**: Coordinated public launch + researcher-facing outreach
- **LAUNCH-03**: Custom domain (`usdr.science` or equivalent)

### Hub ranking (after HUB-01 spec)

- **HUB-02**: Harvest-rank implementation (specified, not computed)
- **HUB-03**: Curator-score implementation (specified, not computed)

## Out of Scope

| Feature | Reason |
|---------|--------|
| Marketing posts (Reddit, LinkedIn, DMs) | v1.2 parked until the product impresses in the room |
| DNS / arXiv **upload** | v1.2 parked; DOI is for later, not a substitute for finishing the product |
| Catalog waves without review | Human gate sacred |
| GSD artifacts as science | Process metadata only |
| Fake `RESULT: CONFIRMED` | Honesty constraint |
| Epidemic FSS retune | Freeze `NU_THEORY=3.0`; R²=0.32 is not a defect to shop |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| WORK-01 | Phase 6 | Pending |
| FLOW-01 | Phase 7 | Pending |
| UI-01 | Phase 7 | Pending |
| ROBUST-01 | Phase 8 | Pending |
| WORK-02 | Phase 9 | Pending |

**Coverage:**
- v1.3 requirements: 5 total
- Mapped to phases: 5
- Unmapped: 0 ✓

---
*Requirements defined: 2026-08-26*
*Last updated: 2026-08-26 after opening v1.3*
