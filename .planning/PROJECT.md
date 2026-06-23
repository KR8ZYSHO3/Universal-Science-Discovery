# Universal Science Discovery Repository (USDR)

## What This Is

USDR is open, git-native scientific infrastructure: a version-controlled catalog of unknowns, hypotheses, and cross-domain bridges, with a live knowledge graph, contributor hub, and **Crosscheck** — runnable repro protocols that falsify bridge claims. June 2026 focus: **public launch** and first external contributors while preserving schema/CI rigor.

## Core Value

Researchers can discover what's *not yet known*, see credible cross-domain connections, and **run a falsifiable experiment in minutes** — not just read another database.

## Requirements

### Validated

- ✓ Schema-backed catalog at scale (1,100+ bridges, 1,400+ unknowns) — Phase 0
- ✓ Knowledge graph + dashboard + GitHub Pages — Phase 0
- ✓ Crosscheck hub with in-browser runners — PRs #291–#293
- ✓ 3 of 4 seed Crosscheck protocols **CONFIRMED** (FSS ν, Ising γ, cluster τ) — PRs #297–#302
- ✓ Core Crosscheck drift gate (`build_crosscheck.py --check`) — PRs #299–#301
- ✓ Early Stewards call posted — Discussion #286

### Active

- [ ] **LAUNCH-01**: Coordinated outreach wave live (Reddit + updated Crosscheck copy)
- [ ] **LAUNCH-02**: Custom domain `usdr.science` resolves with HTTPS
- [ ] **LAUNCH-03**: arXiv preprint v1.2 submitted with citable DOI
- [ ] **LAUNCH-04**: 5+ external engagements (DMs, issues claimed, or PRs)
- [ ] **CROSS-01**: Epidemic FSS protocol reaches CONFIRMED (4/4 seed protocols)

### Out of Scope

- New catalog waves during launch sprint — deferred until E7 traction signal
- Wave Factory bot PR merges without maintainer review — human gate sacred
- GSD artifacts as scientific evidence — process metadata only per `docs/GSD_INTEGRATION.md`

## Context

- **Preparation complete** (LAUNCH_MILESTONES.md): stats refresh, outreach copy, preprint package, stewards call, contributor guide.
- **Execution gap**: engineering shipped fast (#297–#302) but human launch items (Reddit, DNS, arXiv, DMs) deferred.
- **Crosscheck scorecard**: habitat FSS ✓, cluster exponent ✓, Ising EWI ✓, epidemic FSS ✗.
- **Canonical human calendar**: `LAUNCH_PLAYBOOK.md`, `LAUNCH_MILESTONES.md` (E1–E7).
- **Repo-level long roadmap**: `ROADMAP.md` (Phase 0–4 vision) — distinct from `.planning/ROADMAP.md` (GSD execution phases).

## Constraints

- **Governance**: METHODOLOGY.md, LEGAL.md, schema CI on every PR
- **Truth surfaces**: dashboard/hub must match git (`verify_dashboard_consistency.py`)
- **Human gates**: arXiv submit, DNS register, personal DMs — Brandon-owned
- **Agent scope**: agents draft/copy/script; humans post/submit/register

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| GSD planning activated 2026-06-23 | Ad-hoc session drift; need discuss→plan→execute | — Pending |
| Crosscheck before outreach depth | 3 CONFIRMED demos stronger than INCONCLUSIVE story | ✓ Good |
| Pooled histogram + p≈p_c for cluster τ | Per-seed fits at p=0.55 biased low (~25% error) | ✓ Good |
| Python = canonical; browser = demo | CI and regression tests lock Python fits | ✓ Good |
| Outreach copy must reflect 3 CONFIRMED | READY_TO_POST still says INCONCLUSIVE at quick-trial | ⚠️ Revisit in Phase 2 |

---
*Last updated: 2026-06-23 after GSD bootstrap (milestone v1.1 Launch Execution)*