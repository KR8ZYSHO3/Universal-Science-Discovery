# Universal Science Discovery Repository (USDR)

## What This Is

USDR is open, git-native scientific infrastructure: a version-controlled catalog of unknowns, hypotheses, and cross-domain bridges, with a live knowledge graph, contributor hub, and **Crosscheck** — runnable repro protocols that falsify bridge claims.

**v1.1 Core Development shipped 2026-08-26** (PR #308). **Current milestone: v1.3 University-ready robustness.** **v1.2 Launch is parked.** Product path: repo-root `ROADMAP.md`.

## Core Value

Researchers can discover what's *not yet known*, see credible cross-domain connections, and **run a falsifiable experiment in minutes** — not just read another database.

## Current State (after v1.1)

- 4/4 seed Crosscheck protocols print `RESULT: CONFIRMED` in CI (habitat FSS, cluster τ, Ising EWI, epidemic volume FSS ν̄=3)
- Generate → human-promote → repro path proven (`p-b-percolation-oncology-gcc`, always INCONCLUSIVE)
- `tests/repo_smoke` covers CONFIRMED-gate inventory, generate `--dry-run`, GCC, epidemic freeze
- Hub `#recommendations` fetches `api/v1/recommendations.json` (undirected degree; contributor tooling, not science)
- GitHub `main` is PR-protected; batch a PR at milestones

## Ship Bar (still the quality bar — not a GSD phase list)

> **No more engineering for its own sake, and no marketing, until USDR is very robust for a single developer, every maintainer workflow runs excellently end-to-end, and the project interface is refined and truly awesome.**

v1.1 closed the GSD requirement IDs. The three pillars are **not** fully claimed as met:

| Pillar | Honest status after v1.1 |
|--------|--------------------------|
| Single-dev robustness | Stronger (smoke + generate path + CONFIRMED inventory). ROBUST-01 playbook still a leftover |
| Workflows excellent | Crosscheck loop still does not feed stdout RESULT back into catalog YAML (WORK-01) |
| Interface awesome | Recommendations panel shipped as a thin slice; UI-01 first-visit audit not run |

## Current Milestone: v1.3 University-ready robustness

**Goal:** One person can run the repo honestly; a first visit to the hub holds up; Crosscheck is a closed loop; the flow is three doors (Look / Add / Run).

**Target features:**
- Three-door utilization ([docs/USE.md](../docs/USE.md)) on the hub (FLOW-01)
- Crosscheck `RESULT:` writes through to catalog/hub status (WORK-01)
- Hub first-visit audit: counts, links, Crosscheck, no broken loads (UI-01)
- One ordered maintainer command list (ROBUST-01)
- Catalog batch = one documented local run (WORK-02)

**Not in v1.3:** Reddit, LinkedIn, DMs, hackathon, custom domain, arXiv **upload**.

## Requirements

### Validated

- ✓ Schema-backed catalog at scale — v1.0
- ✓ Knowledge graph + dashboard + GitHub Pages — v1.0
- ✓ Crosscheck hub with in-browser runners — v1.0 (#291–#293)
- ✓ Habitat FSS, Ising EWI, cluster τ CONFIRMED — v1.1 Phase 1
- ✓ Epidemic FSS CONFIRMED (volume ν̄=3) — v1.1 Phase 2
- ✓ Crosscheck drift gate (`build_crosscheck.py --check`) — v1.0 / v1.1 TRUST-01
- ✓ Generate/promote second-bridge path — v1.1 CROSS-06
- ✓ Python vs browser/Colab parity documented — v1.1 CROSS-07
- ✓ CONFIRMED protocols gated in CI inventory — v1.1 TRUST-02
- ✓ repo_smoke for epidemic + generate + GCC — v1.1 TRUST-03
- ✓ Hub recommendations spec + static JSON — v1.1 HUB-01

### Active

- [ ] **FLOW-01**: A newcomer can pick Look, Add, or Run from docs/USE.md and hub `#start` without a stack of strategy docs
- [ ] **WORK-01**: After a documented Crosscheck run, catalog YAML and hub Crosscheck surfaces show the same RESULT token the protocol printed (or an explicit pending/apply state), without fabricating CONFIRMED
- [ ] **UI-01**: A first visit to the hub shows git-consistent counts, working Crosscheck links, and no broken first-visit loads
- [ ] **ROBUST-01**: A new maintainer can operate the repo from one ordered command list
- [ ] **WORK-02**: A catalog batch can be completed as one documented local run

### Out of Scope (until owner reopens)

- **Marketing / outreach** — v1.2 Launch parked (2026-06-23)
- **arXiv, usdr.science DNS** — v1.2 Launch parked
- New catalog waves without maintainer review
- GSD artifacts as scientific evidence

## Context

- Crosscheck scorecard: habitat FSS ✓, cluster exponent ✓, Ising EWI ✓, epidemic FSS ✓ (volume ν̄=3; freeze R²=0.32 — do not retune)
- Hub recommendations: connectivity only; harvest/curator specified, not computed
- GSD lives **in this repository** (`.planning/`). There is no separate GSD progress repo.

## Constraints

- **Governance**: METHODOLOGY.md, LEGAL.md, schema CI on every PR
- **Truth surfaces**: dashboard/hub must match git (`verify_dashboard_consistency.py`)
- **Python = canonical**; browser/Colab = demo tier
- **No marketing** unless owner reopens v1.2
- **`main` is PR-only** — push feature branches; squash at milestones

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| GSD planning in this repo | Ad-hoc session drift | ✓ Good — `.planning/` is the progress system |
| Development before marketing | Outreach premature | ✓ v1.1 shipped without marketing |
| Epidemic volume ν̄=3 not ν=1 | Honest FSS | ✓ CONFIRMED; freeze pinned |
| Python canonical; browser demo | CI locks Python | ✓ Good |
| CONFIRMED gates = stdout | YAML `status` is not the token | ✓ TRUST-02 |
| Recommendations ≠ science | Degree is contributor leverage | ✓ HUB-01 |
| PR at milestones | `main` protected | ✓ #308 |
| **Ship Bar** | Quality bar beyond GSD IDs | — Still the bar; v1.3 is the remaining work |
| **Root ROADMAP.md is the only product path** | PATH_TO_SUCCESS / launch docs were a second strategy | ✓ 2026-08-26 |
| **v1.3 before v1.2 Launch** | Product must impress in the room before outreach | — Pending |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `/gsd-transition`):
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

**After each milestone** (via `/gsd-complete-milestone`):
1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-08-26 after opening v1.3*
