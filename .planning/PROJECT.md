# Universal Science Discovery Repository (USDR)

## What This Is

USDR is open, git-native scientific infrastructure: a version-controlled catalog of unknowns, hypotheses, and cross-domain bridges, with a live knowledge graph, contributor hub, and **Crosscheck** — runnable repro protocols that falsify bridge claims. **Current focus: core development** — make Crosscheck and trust surfaces robust before any marketing push.

## Core Value

Researchers can discover what's *not yet known*, see credible cross-domain connections, and **run a falsifiable experiment in minutes** — not just read another database.

## Ship Bar (owner constraint — gates all plans)

> **No more engineering for its own sake, and no marketing, until USDR is very robust for a single developer, every maintainer workflow runs excellently end-to-end, and the project interface is refined and truly awesome.**

This is the bar for v1.1 completion — not "one more CONFIRMED protocol" or "green CI" in isolation. Pushing further is intentional; "good enough" is when the three pillars below are honestly met.

### Pillar 1 — Single-developer robustness

One person (Brandon) can operate the full repo without tribal knowledge or fragile manual steps.

- Catalog change → validate → graph → dashboard/API → Pages deploy: documented, scripted, CI-backed
- Crosscheck change → repro → hub/explainers → drift check: one command path (`build_crosscheck.py`)
- Bot PRs (graph, waves) predictable — no 400-merge-conflict surprises
- `pytest tests/repo_smoke` + schema validation = confidence before merge

### Pillar 2 — Workflows work excellently

Each loop completes reliably, with clear failure modes and recovery — not "works on my machine."

| Workflow | Done when |
|----------|-----------|
| **Crosscheck** | Bridge → protocol → repro → outcome → reflected in catalog/hub |
| **Catalog batch** | YAML → graph → stats → domain pages → hub consistent |
| **Contributor** | Happy path documented; first PR path tested |
| **Maintainer** | STATE, CHANGELOG, dashboard sync cadence is routine |

### Pillar 3 — Interface truly awesome

The contributor hub (`dashboard/`) is the product face — fast, coherent, trustworthy, impressive to a serious researcher (and eventually an institution) on first visit.

- Numbers and links match git; no stale subgraphs or console errors on load
- Crosscheck runnable in-browser without friction
- Navigation, search → graph → GitHub flow feels intentional, not assembled
- Phase C+ (recommendations, polish) judged against *awesome*, not "shipped a panel"

## Requirements

### Validated

- ✓ Schema-backed catalog at scale (1,100+ bridges, 1,400+ unknowns) — Phase 0
- ✓ Knowledge graph + dashboard + GitHub Pages — Phase 0
- ✓ Crosscheck hub with in-browser runners — PRs #291–#293
- ✓ 3 of 4 seed Crosscheck protocols **CONFIRMED** (FSS ν, Ising γ, cluster τ) — PRs #297–#302
- ✓ Core Crosscheck drift gate (`build_crosscheck.py --check`) — PRs #299–#301

### Active (must advance a pillar — see Ship Bar)

- [ ] **ROBUST-01**: Maintainer playbook is one ordered command list; smoke tests cover all critical scripts
- [ ] **WORK-01**: Crosscheck full loop closed (outcome → catalog/hub status, not just stdout)
- [ ] **WORK-02**: Catalog batch workflow documented + verified in one local runbook
- [ ] **UI-01**: Hub passes "first visit" audit (consistency, Crosscheck UX, no broken loads)
- [ ] **CROSS-04**: Epidemic FSS CONFIRMED — only if it unblocks WORK-01, not as a standalone trophy

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
| **Ship Bar** (3 pillars) | Single-dev robust + excellent workflows + awesome UI before ship/market | — Pending (2026-06-23) |

---
*Last updated: 2026-06-23 — Ship Bar locked as plan gate for all GSD phases*