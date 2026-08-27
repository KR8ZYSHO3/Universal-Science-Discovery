# Roadmap: USDR — Milestone v1.1 Core Development

## Milestones

- ✅ **v1.0 Foundation** — repo `ROADMAP.md` Phase 0
- 🚧 **v1.1 Core Development** — Phases 1–5 (active)
- 📋 **v1.2 Launch** — outreach, DNS, arXiv, traction (**deferred** — not active)

## Overview

Harden Crosscheck to 4/4 CONFIRMED, scale the protocol pipeline, expand CI/trust surfaces, then spec hub recommendations. **No marketing work** in this milestone.

## Phases

- [x] **Phase 1: Crosscheck credibility** — 3 CONFIRMED + drift gate
- [x] **Phase 2: Epidemic FSS precision** — 4th seed protocol CONFIRMED
- [ ] **Phase 3: Crosscheck scale-up** — generate/promote protocols + browser parity
- [ ] **Phase 4: CI & trust hardening** — smoke tests + CONFIRMED gates
- [ ] **Phase 5: Hub engineering** — smart recommendations spec + prototype

## Phase Details

### Phase 1: Crosscheck credibility
**Goal**: Crosscheck reproducible; CI prevents artifact drift.
**Depends on**: Nothing
**Requirements**: CROSS-01, CROSS-02, CROSS-03, CROSS-05, TRUST-01
**Plans**: 3/3 complete (#297–#302)

### Phase 2: Epidemic FSS precision
**Goal**: All 4 seed protocols CONFIRMED in CI.
**Depends on**: Phase 1
**Requirements**: CROSS-04
**Success Criteria**:
  1. `epidemic_percolation_fss.py` prints `RESULT: CONFIRMED`
  2. Fixed-input regression test for epidemic ν fit
  3. `crosscheck-repro.yml` greps CONFIRMED for epidemic
**Plans**: 3 plans in 2 waves (planned 2026-06-23)

Plans:
- [ ] 02-01: Parameter sweep + precision pass (averaged bisection, signed fit, PC_INF=1/k) — **Wave 1**
- [ ] 02-02: Regression test + CI CONFIRMED gate — **Wave 2** *(blocked on 02-01)*
- [ ] 02-03: Colab/notebook path verified or documented — **Wave 2** *(blocked on 02-01)*

**Cross-cutting constraints:**
- `epidemic_percolation_fss.py` prints `RESULT: CONFIRMED` at locked defaults
- CI `crosscheck-repro.yml` greps CONFIRMED for epidemic (all 3 plans)

### Phase 3: Crosscheck scale-up
**Goal**: Path from bridge YAML → promoted protocol → repro bundle is repeatable.
**Depends on**: Phase 2
**Requirements**: CROSS-06, CROSS-07
**Success Criteria**:
  1. `generate_crosscheck.py` run documented for ≥1 new bridge
  2. Parity doc: Python vs browser outcome tiers per protocol
**Plans**: TBD

Plans:
- [ ] 03-01: Generate + promote protocols for a second bridge
- [ ] 03-02: Browser/Colab parity matrix + hub updates

### Phase 4: CI & trust hardening
**Goal**: Regression coverage matches shipped Crosscheck surface area.
**Depends on**: Phase 2
**Requirements**: TRUST-02, TRUST-03
**Success Criteria**:
  1. All CONFIRMED protocols gated in crosscheck-repro workflow
  2. repo_smoke covers epidemic + any new script entry points
**Plans**: TBD

Plans:
- [ ] 04-01: Unified CONFIRMED gates in CI
- [ ] 04-02: repo_smoke expansion

### Phase 5: Hub engineering + discovery instruments
**Goal**: Hub delivers goal-directed discovery (pathfinder) and recommendation prototype.
**Depends on**: Phase 4 (soft — pathfinder can start after Phase 2)
**Requirements**: HUB-01, DISC-01
**Success Criteria**:
  1. `graph_pathfinder.py` + smoke test for known domain pair
  2. Hub knowledge-graph section: domain pickers → path → graph highlight
  3. (Optional) Spec defines ranking signal for smart recommendations JSON slice
**Plans**: TBD

Plans:
- [x] 05-01: Pathfinder CLI + smoke test (`.planning/specs/PATHFINDER.md`)
- [x] 05-02: Hub pathfinder UI wired to graph panel
- [ ] 05-03: Smart-recommendations spec + thin JSON slice (HUB-01)

## Deferred: v1.2 Launch (not scheduled)

Outreach copy, Reddit/LinkedIn, `usdr.science`, arXiv, personal DMs — see `LAUNCH_PLAYBOOK.md`. **Owner parked 2026-06-23.**

## Progress

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Crosscheck credibility | 3/3 | Complete | 2026-06-23 |
| 2. Epidemic FSS precision | 3/3 | Complete | 2026-06-23 |
| 3. Crosscheck scale-up | 0/2 | Not started | — |
| 4. CI & trust hardening | 0/2 | Not started | — |
| 5. Hub engineering | 2/3 | In progress | 2026-06-23 (pathfinder) |

---
*Reprioritized 2026-06-23. Repo vision: `ROADMAP.md` (root).*