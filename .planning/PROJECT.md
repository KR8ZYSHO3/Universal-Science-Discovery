# Universal Science Discovery Repository (USDR)

## What This Is

USDR is open, git-native scientific infrastructure: a version-controlled catalog of unknowns, hypotheses, and cross-domain bridges, with a live knowledge graph, contributor hub, and **Crosscheck** — runnable repro protocols that falsify bridge claims. **Current focus: core development** — make Crosscheck and trust surfaces robust before any marketing push.

## Core Value

Researchers can discover what's *not yet known*, see credible cross-domain connections, and **run a falsifiable experiment in minutes** — not just read another database.

## Requirements

### Validated

- ✓ Schema-backed catalog at scale (1,100+ bridges, 1,400+ unknowns) — Phase 0
- ✓ Knowledge graph + dashboard + GitHub Pages — Phase 0
- ✓ Crosscheck hub with in-browser runners — PRs #291–#293
- ✓ 3 of 4 seed Crosscheck protocols **CONFIRMED** (FSS ν, Ising γ, cluster τ) — PRs #297–#302
- ✓ Core Crosscheck drift gate (`build_crosscheck.py --check`) — PRs #299–#301

### Active

- [ ] **CROSS-04**: Epidemic FSS protocol reaches CONFIRMED (4/4 seed protocols)
- [ ] **CROSS-06**: `generate_crosscheck.py` promotion path documented + second bridge protocols drafted
- [ ] **CROSS-07**: Browser demos parity-checked against Python canonical fits
- [ ] **TRUST-03**: Expanded `tests/repo_smoke` coverage for Crosscheck + critical scripts
- [ ] **HUB-01**: Dashboard Phase C smart-recommendations spec + thin JSON slice

### Out of Scope (this milestone)

- **Marketing / outreach** — Reddit, LinkedIn, DM waves, launch copy refresh — deferred to **v1.2 Launch** (owner decision 2026-06-23)
- **arXiv submit, usdr.science DNS** — deferred to v1.2 Launch
- New catalog waves without maintainer review — human gate sacred
- GSD artifacts as scientific evidence — process metadata only

## Context

- Crosscheck scorecard: habitat FSS ✓, cluster exponent ✓, Ising EWI ✓, **epidemic FSS ✗** (bond percolation on ER graphs, `networkx`, Colab path).
- Core pipeline robustness landed (#299–#301); next bottleneck is **4/4 CONFIRMED** and **scaling protocols beyond 4 seeds**.
- Repo tracks B–D (trust surfaces, breakthrough gaps, catalog depth) in root `ROADMAP.md` — GSD phases align with Track B + Crosscheck depth first.
- Launch prep artifacts exist (`LAUNCH_PLAYBOOK.md`, outreach copy) but **explicitly parked** until development milestone completes.

## Constraints

- **Governance**: METHODOLOGY.md, LEGAL.md, schema CI on every PR
- **Truth surfaces**: dashboard/hub must match git (`verify_dashboard_consistency.py`)
- **Python = canonical**; browser/Colab = demo tier with documented lighter budgets
- **No marketing work** in v1.1 GSD phases unless owner reopens v1.2

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| GSD planning activated 2026-06-23 | Ad-hoc session drift | ✓ Good |
| **Development before marketing** | Substantial engineering remains; outreach premature | — Pending (2026-06-23) |
| Pooled histogram + p≈p_c for cluster τ | Per-seed fits at p=0.55 biased low | ✓ Good |
| Python = canonical; browser = demo | CI locks Python fits | ✓ Good |
| Launch/outreach → v1.2 milestone | User directive: not interested in marketing now | — Pending |

---
*Last updated: 2026-06-23 after milestone reprioritization (v1.1 Core Development)*