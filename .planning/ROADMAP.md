# Roadmap: USDR — Milestone v1.1 Launch Execution

## Milestones

- ✅ **v1.0 Foundation** — Phases 0 (repo ROADMAP.md Phase 0 complete)
- 🚧 **v1.1 Launch Execution** — Phases 1–5 (June 2026)

## Overview

Ship credible Crosscheck demos, then execute the human-calendar launch sequence (outreach → domain → arXiv → first externals). Engineering debt (epidemic FSS) runs last so outreach isn't blocked.

## Phases

- [x] **Phase 1: Crosscheck credibility** — 3 CONFIRMED protocols + CI drift gate
- [ ] **Phase 2: Launch outreach wave** — Updated copy + Reddit + social follow-ups
- [ ] **Phase 3: Credibility infrastructure** — `usdr.science` DNS + arXiv submit
- [ ] **Phase 4: First external traction** — DMs + steward activation + spotlight
- [ ] **Phase 5: Crosscheck completion** — Epidemic FSS precision pass (4/4 CONFIRMED)

## Phase Details

### Phase 1: Crosscheck credibility
**Goal**: Crosscheck is demonstrably reproducible; CI prevents artifact drift.
**Depends on**: Nothing
**Requirements**: CROSS-01, CROSS-02, CROSS-03, CROSS-05, TRUST-01
**Success Criteria**:
  1. Three seed protocols print `RESULT: CONFIRMED` in CI
  2. `pytest tests/repo_smoke` includes fixed-input regression for each CONFIRMED fit
  3. `build_crosscheck.py --check` runs in validate-schemas workflow
**Plans**: 3 plans (retroactive)

Plans:
- [x] 01-01: FSS + Ising precision passes (#297–#298)
- [x] 01-02: Core pipeline robustness (#299–#301)
- [x] 01-03: Cluster exponent precision (#302)

### Phase 2: Launch outreach wave
**Goal**: Public narrative matches shipped reality (3 CONFIRMED Crosschecks).
**Depends on**: Phase 1
**Requirements**: LAUNCH-01, LAUNCH-02, TRUST-02
**Success Criteria**:
  1. `READY_TO_POST.md` and `CROSSCHECK_LAUNCH_STORY.md` cite 3 CONFIRMED protocols
  2. Reddit r/OpenScience post published (link captured in STATE.md)
  3. At least one additional social post (LinkedIn §1b or 3-CONFIRMED update) published
**Plans**: TBD (run `/gsd-plan-phase 2`)

Plans:
- [ ] 02-01: Refresh outreach copy for 3 CONFIRMED demos
- [ ] 02-02: Execute Reddit post (E6)
- [ ] 02-03: LinkedIn / X follow-up posts

### Phase 3: Credibility infrastructure
**Goal**: Stable public URL + citable preprint.
**Depends on**: Phase 2 (can overlap after 02-01 ships)
**Requirements**: LAUNCH-03, LAUNCH-04
**Success Criteria**:
  1. `https://usdr.science/dashboard/` resolves with HTTPS
  2. arXiv submission confirmation ID recorded in LAUNCH_MILESTONES.md
**Plans**: TBD

Plans:
- [ ] 03-01: Register DNS + GitHub Pages custom domain (E3)
- [ ] 03-02: Submit arXiv preprint v1.2 (E5)

### Phase 4: First external traction
**Goal**: Evidence of ownership distribution beyond founder.
**Depends on**: Phase 3
**Requirements**: LAUNCH-05, LAUNCH-06
**Success Criteria**:
  1. 5 personal DMs sent (logged in LAUNCH_MILESTONES E7)
  2. At least one external engagement (issue comment, PR, or reply)
**Plans**: TBD

Plans:
- [ ] 04-01: Personal DM wave (E7)
- [ ] 04-02: Steward activation + first external spotlight

### Phase 5: Crosscheck completion
**Goal**: All 4 seed protocols CONFIRMED.
**Depends on**: Phase 2 (copy can reference 3/4 until done)
**Requirements**: CROSS-04
**Success Criteria**:
  1. Epidemic FSS repro prints `RESULT: CONFIRMED` in CI
  2. Regression test added for epidemic fit
**Plans**: TBD

Plans:
- [ ] 05-01: Epidemic FSS precision pass

## Progress

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Crosscheck credibility | 3/3 | Complete | 2026-06-23 |
| 2. Launch outreach wave | 0/3 | **Active** | — |
| 3. Credibility infrastructure | 0/2 | Not started | — |
| 4. First external traction | 0/2 | Not started | — |
| 5. Crosscheck completion | 0/1 | Not started | — |

---
*GSD roadmap created 2026-06-23. Repo vision roadmap remains at `ROADMAP.md` (project root).*