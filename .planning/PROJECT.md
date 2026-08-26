# Universal Science Discovery Repository (USDR)

## What This Is

USDR is open, git-native scientific infrastructure: a version-controlled catalog of unknowns, hypotheses, and cross-domain bridges, with a live knowledge graph, contributor hub, and **Crosscheck** — runnable repro protocols that falsify bridge claims.

**v1.1 Core Development shipped 2026-08-26** (PR #308). Current GSD status: no active milestone. **v1.2 Launch is parked.**

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

### Next Milestone Goals

**Not opened.** Options when the owner is ready:

1. `/gsd-new-milestone` for remaining Ship Bar work (ROBUST-01, WORK-01, WORK-02, UI-01)
2. `/gsd-new-milestone` for **v1.2 Launch** only if marketing is un-parked
3. Keep parking and only open a PR at the next real milestone

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

None scheduled. Leftovers (not a milestone until `/gsd-new-milestone`):

- [ ] **ROBUST-01**: Maintainer playbook is one ordered command list
- [ ] **WORK-01**: Crosscheck outcome → catalog/hub status
- [ ] **WORK-02**: Catalog batch workflow verified in one local runbook
- [ ] **UI-01**: Hub first-visit audit

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
| **Ship Bar** | Quality bar beyond GSD IDs | — Still the bar; not fully claimed |

---
*Last updated: 2026-08-26 after v1.1 milestone*
