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
- [x] **Phase 3: Crosscheck scale-up** — generate/promote protocols + browser parity
- [x] **Phase 4: CI & trust hardening** — smoke tests + CONFIRMED gates
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
**Plans**: 3/3 complete (2026-08-26)

Plans:
- **Wave 1**
- [x] 02-01: Parameter sweep + precision pass (SEEDS_PER_N, sizes, signed fit) — CONFIRMED 2026-08-26
- **Wave 2**
- [x] 02-02: Regression test + CI CONFIRMED gate — freeze pytest + CI grep 2026-08-26
- [x] 02-03: Colab/notebook path verified or documented — YAML status confirmed, nu_bar=3 2026-08-26

Cross-cutting constraints:
- Epidemic stdout must contain `RESULT: CONFIRMED` (CROSS-04)
- Fit target is volume FSS `NU_THEORY = 3.0`, never relabeled as 1 (D-03)
- Frozen `mean_pcs` from 02-01-SUMMARY is the only legal pytest pin (D-07)

### Phase 3: Crosscheck scale-up
**Goal**: Path from bridge YAML → promoted protocol → repro bundle is repeatable.
**Depends on**: Phase 2
**Requirements**: CROSS-06, CROSS-07
**Success Criteria**:
  1. `generate_crosscheck.py` run documented for ≥1 new bridge
  2. Parity doc: Python vs browser outcome tiers per protocol
**Plans**: 2/2 complete (2026-08-26)

Plans:
- **Wave 1**
- [x] 03-01: Generate + promote + stdlib repro for `b-percolation-oncology` (`p-b-percolation-oncology-gcc`) — INCONCLUSIVE 2026-08-26
- **Wave 2**
- [x] 03-02: Browser/Colab parity matrix in `docs/CROSSCHECK.md` + hub + `--apply` — 2026-08-26

Cross-cutting constraints:
- Python is canonical; browser/Colab are demo tier (CROSS-07)
- New oncology protocol prints `RESULT: INCONCLUSIVE` and is never `status: confirmed` (D-04/D-13/D-14)
- Epidemic freeze `NU_THEORY = 3.0` is untouched (D-07)

### Phase 4: CI & trust hardening
**Goal**: Regression coverage matches shipped Crosscheck surface area.
**Depends on**: Phase 2
**Requirements**: TRUST-02, TRUST-03
**Success Criteria**:
  1. All CONFIRMED protocols gated in crosscheck-repro workflow
  2. repo_smoke covers epidemic + any new script entry points
**Plans**: 2/2 complete (2026-08-26)

Plans:
- **Wave 1**
- [x] 04-01: Unified CONFIRMED gates in CI — text inventory pytest + CONFIRMED-only docs — 2026-08-26
- **Wave 2**
- [x] 04-02: repo_smoke expansion — generate `--dry-run` + GCC INCONCLUSIVE smoke — 2026-08-26

Cross-cutting constraints:
- Gate stdout `RESULT: CONFIRMED`, not YAML `status` (D-01)
- Keep the four live `crosscheck-repro.yml` greps; never grep GCC CONFIRMED (D-02/D-03)
- Epidemic freeze `NU_THEORY = 3.0` is untouched; no live NetworkX in pytest (D-05/D-06)
- No marketing, DNS, arXiv, or fabricated `RESULT: CONFIRMED` (D-12/D-13)

### Phase 5: Hub engineering
**Goal**: Phase C smart-recommendations has a spec and static prototype.
**Depends on**: Phase 4
**Requirements**: HUB-01
**Success Criteria**:
  1. Spec defines ranking signal (connectivity / harvest / curator score)
  2. `api/v1/` or hub section loads prototype JSON
**Plans**: 1/1 planned (2026-08-26)

Plans:
- **Wave 1**
- [ ] 05-01: Spec + thin JSON slice in hub — `docs/HUB_RECOMMENDATIONS.md` + `api/v1/recommendations.json` + `#recommendations`

Cross-cutting constraints:
- v1 ranks bridges by undirected degree; harvest/curator are spec-only (D-02)
- Contributor tooling, not a scientific ranking (D-06)
- Copy orphan/xref panel: Python exporter → committed JSON → hub `textContent` fetch (D-03/D-05)
- No marketing, epidemic retune, or fabricated `RESULT: CONFIRMED` (D-10)

## Deferred: v1.2 Launch (not scheduled)

Outreach copy, Reddit/LinkedIn, `usdr.science`, arXiv, personal DMs — see `LAUNCH_PLAYBOOK.md`. **Owner parked 2026-06-23.**

## Progress

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Crosscheck credibility | 3/3 | Complete | 2026-06-23 |
| 2. Epidemic FSS precision | 3/3 | Complete | 2026-08-26 |
| 3. Crosscheck scale-up | 2/2 | Complete | 2026-08-26 |
| 4. CI & trust hardening | 2/2 | Complete | 2026-08-26 |
| 5. Hub engineering | 0/1 | Ready to execute | — |

---
*Reprioritized 2026-06-23. Repo vision: `ROADMAP.md` (root).*