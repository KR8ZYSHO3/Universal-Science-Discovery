# Universal Science Discovery Repository (USDR)

## What This Is

USDR is open, git-native scientific infrastructure: a version-controlled catalog of unknowns, hypotheses, and cross-domain bridges, with a live knowledge graph, contributor hub, and **Crosscheck** — runnable repro protocols that falsify bridge claims. **Current focus: core development** — make Crosscheck and trust surfaces robust before any marketing push.

## Core Value

Researchers can discover what's *not yet known*, see credible cross-domain connections, and **run a falsifiable Crosscheck experiment in minutes** — with outcomes reflected in the catalog, hub, and knowledge graph — not just read another database.

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
| **Pathfinder** | Two domains → shortest graph path → highlight + evidence tier per hop |
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
- ✓ 4 of 4 seed Crosscheck protocols **CONFIRMED** (habitat FSS ν, cluster τ, Ising γ, epidemic FSS ν) — Phase 2
- ✓ Core Crosscheck drift gate (`build_crosscheck.py --check`) — PRs #299–#301
- ✓ **WORK-01**: Crosscheck outcome loop closed (`crosscheck_outcome` in protocol YAML → hub badges → `evidence_tier` on bridge nodes)

### Active (must advance a pillar — see Ship Bar)

- [ ] **ROBUST-01**: Maintainer playbook is one ordered command list; smoke tests cover all critical scripts
- [ ] **WORK-02**: Catalog batch workflow documented + verified in one local runbook
- ✓ **UI-01**: Hub passes "first visit" audit (consistency, Crosscheck UX, no broken loads)
- ✓ **DISC-01**: Graph pathfinder — CLI + hub domain path UI (spec: `.planning/specs/PATHFINDER.md`)
- ✓ **DISC-02**: Impact router — `propose_bridges.py` + hub `#impact-router` (filter, graph/gap/pathfinder actions)
- ✓ **DISC-03**: Priority unknowns panel — `export_orphan_unknowns_panel.py` + hub `#orphan-unknowns-panel`

### Out of Scope (this milestone)

- **Marketing / outreach** — Reddit, LinkedIn, DM waves, launch copy refresh — deferred to **v1.2 Launch** (owner decision 2026-06-23)
- **arXiv submit, usdr.science DNS** — deferred to v1.2 Launch
- New catalog waves without maintainer review — human gate sacred
- GSD artifacts as scientific evidence — process metadata only

## Context

- Crosscheck scorecard: habitat FSS ✓, cluster exponent ✓, Ising EWI ✓, epidemic FSS ✓ — **4/4 CONFIRMED**.
- Outcome loop: protocol `status` + `crosscheck_outcome` → hub cards → bridge `evidence_tier` in knowledge graph.
- Next bottleneck: scaling protocols beyond 4 seeds (Phase 3), smart recommendations (HUB-01 / 05-03).
- Repo tracks A–E in root `ROADMAP.md` — GSD Phase 5 instruments (pathfinder, impact router, priority unknowns) shipped; UI-01 polish complete.
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
| **Pathfinder spec** (DISC-01) | Pull INTERFACE P2.3 into v1.1 instruments | ✓ Good (2026-06-23) |

---
*Last updated: 2026-06-24 — DISC-03 priority unknowns panel shipped*