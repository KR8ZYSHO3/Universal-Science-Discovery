# Roadmap: USDR

**This is the GSD execution list**, not the product strategy. Canonical product path: [../ROADMAP.md](../ROADMAP.md).

## Milestones

- ✅ **v1.0 Foundation** — repo Phase 0
- ✅ **v1.1 Core Development** — GSD Phases 1–5 (shipped 2026-08-26, PR #308)
- 🔒 **v1.2 Launch** — outreach, DNS, arXiv, traction (**parked**)
- 🚧 **v1.3 University-ready robustness** — GSD Phases 6–9 (**active**)

## Phases

<details>
<summary>✅ v1.1 Core Development (Phases 1–5) — SHIPPED 2026-08-26</summary>

- [x] Phase 1: Crosscheck credibility (3/3 plans) — 2026-06-23
- [x] Phase 2: Epidemic FSS precision (3/3 plans) — 2026-08-26
- [x] Phase 3: Crosscheck scale-up (2/2 plans) — 2026-08-26
- [x] Phase 4: CI & trust hardening (2/2 plans) — 2026-08-26
- [x] Phase 5: Hub engineering (1/1 plan) — 2026-08-26

Full archive: [milestones/v1.1-ROADMAP.md](milestones/v1.1-ROADMAP.md)

</details>

### 🚧 v1.3 University-ready robustness (active)

- [ ] **Phase 6: Crosscheck closed loop** — RESULT writes through to catalog/hub
- [ ] **Phase 7: Hub first-visit + simple flow** — three doors on the hub; counts, links, Crosscheck, no broken loads
- [ ] **Phase 8: Maintainer command list** — one ordered playbook
- [ ] **Phase 9: Catalog batch runbook** — one documented local run

### 🔒 v1.2 Launch (parked)

Outreach copy, Reddit/LinkedIn, `usdr.science`, arXiv submit, personal DMs — see `LAUNCH_PLAYBOOK.md`. **Owner parked 2026-06-23; reaffirmed 2026-08-26.** Do not schedule GSD phases until the owner reopens this milestone.

## Phase Details

### Phase 6: Crosscheck closed loop

**Goal**: A researcher who runs a protocol sees the same RESULT on catalog/hub surfaces, without fabricating CONFIRMED.
**Depends on**: v1.1 (shipped)
**Requirements**: WORK-01
**Success Criteria** (what must be TRUE):
  1. A documented command (or short sequence) applies a protocol's stdout RESULT token to catalog YAML and hub Crosscheck cards
  2. Honest INCONCLUSIVE / pending states remain visible; no path invents CONFIRMED
  3. Existing CI CONFIRMED-gate inventory still fail-closes on the four seeds
**Plans**: TBD (plan-phase)

Plans:
- [ ] 06-01: RESULT write-through path (catalog + hub) with honesty tests

### Phase 7: Hub first-visit + simple flow

**Goal**: A first visit to the hub holds up, and the only choice is Look / Add / Run.
**Depends on**: Phase 6 (closed loop should be visible on the hub)
**Requirements**: FLOW-01, UI-01
**Success Criteria** (what must be TRUE):
  1. Hub `#start` and [docs/USE.md](../docs/USE.md) show the same three doors
  2. Hero/snapshot counts match git (`verify_dashboard_consistency.py`)
  3. Crosscheck entry points from the hub reach documented runners without 404s
  4. First-visit paths (start, search, graph, Crosscheck, recommendations) load without broken JS/CSS
  5. Recommendations remain labeled contributor tooling, not science
**Plans**: TBD (plan-phase)

Plans:
- [ ] 07-01: Three-door `#start` + first-visit audit against Pages hub and local server

### Phase 8: Maintainer command list

**Goal**: A student can operate the repo without tribal knowledge.
**Depends on**: Phase 7
**Requirements**: ROBUST-01
**Success Criteria** (what must be TRUE):
  1. One document lists clone → validate → graph/hub preview → Crosscheck in order (Door 3 of [docs/USE.md](../docs/USE.md))
  2. Each command has a skip condition or succeeds on a clean clone
  3. The list does not require marketing, DNS, or arXiv steps
**Plans**: TBD (plan-phase)

Plans:
- [ ] 08-01: Ordered maintainer playbook (single list, verified)

### Phase 9: Catalog batch runbook

**Goal**: A catalog batch is one documented local run, not a scavenger hunt.
**Depends on**: Phase 8
**Requirements**: WORK-02
**Success Criteria** (what must be TRUE):
  1. One runbook covers YAML add → validate → graph → dashboard consistency → PR-sized change
  2. Wave Factory / bot PR steps stay in the ops checklist (`docs/PATH_TO_SUCCESS.md`) without becoming a second strategy
  3. Human review gate remains required; no silent bulk commits
**Plans**: TBD (plan-phase)

Plans:
- [ ] 09-01: Catalog-batch local runbook verified end-to-end

## Progress

| Phase | Milestone | Plans Complete | Status | Completed |
|-------|-----------|----------------|--------|-----------|
| 1. Crosscheck credibility | v1.1 | 3/3 | Complete | 2026-06-23 |
| 2. Epidemic FSS precision | v1.1 | 3/3 | Complete | 2026-08-26 |
| 3. Crosscheck scale-up | v1.1 | 3/3 | Complete | 2026-08-26 |
| 4. CI & trust hardening | v1.1 | 2/2 | Complete | 2026-08-26 |
| 5. Hub engineering | v1.1 | 1/1 | Complete | 2026-08-26 |
| 6. Crosscheck closed loop | v1.3 | 0/1 | Not started | — |
| 7. Hub first-visit + simple flow | v1.3 | 0/1 | Not started | — |
| 8. Maintainer command list | v1.3 | 0/1 | Not started | — |
| 9. Catalog batch runbook | v1.3 | 0/1 | Not started | — |

---
*v1.3 opened 2026-08-26. Phase numbering continues from v1.1 (last phase 5 → start at 6). Product path: `ROADMAP.md` (root).*
