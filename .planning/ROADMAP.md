# Roadmap: USDR — Milestone v1.1 Core Development

## Milestones

- ✅ **v1.0 Foundation** — repo `ROADMAP.md` Phase 0
- 🚧 **v1.1 Core Development** — Phases 1–5 (active)
- 📋 **v1.2 Launch** — outreach, DNS, arXiv, traction (**deferred** — not active)

## Overview

Harden Crosscheck to 4/4 CONFIRMED, scale the protocol pipeline, expand CI/trust surfaces, then spec hub recommendations. **No marketing work** in this milestone.

## Phases

- [x] **Phase 1: Crosscheck credibility** — 3 CONFIRMED + drift gate
- [ ] **Phase 2: Epidemic FSS precision** — 4th seed protocol CONFIRMED
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
**Plans**: TBD — run `/gsd-plan-phase 2`

Plans:
- [ ] 02-01: Parameter sweep + precision pass (SEEDS_PER_N, sizes, signed fit)
- [ ] 02-02: Regression test + CI CONFIRMED gate
- [ ] 02-03: Colab/notebook path verified or documented

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

### Phase 5: Hub engineering
**Goal**: Phase C smart-recommendations has a spec and static prototype.
**Depends on**: Phase 4
**Requirements**: HUB-01
**Success Criteria**:
  1. Spec defines ranking signal (connectivity / harvest / curator score)
  2. `api/v1/` or hub section loads prototype JSON
**Plans**: TBD

Plans:
- [ ] 05-01: Spec + thin JSON slice in hub

## Deferred: v1.2 Launch (not scheduled)

Outreach copy, Reddit/LinkedIn, `usdr.science`, arXiv, personal DMs — see `LAUNCH_PLAYBOOK.md`. **Owner parked 2026-06-23.**

## Progress

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Crosscheck credibility | 3/3 | Complete | 2026-06-23 |
| 2. Epidemic FSS precision | 0/3 | **Active** | — |
| 3. Crosscheck scale-up | 0/2 | Not started | — |
| 4. CI & trust hardening | 0/2 | Not started | — |
| 5. Hub engineering | 0/1 | Not started | — |

---
*Reprioritized 2026-06-23. Repo vision: `ROADMAP.md` (root).*