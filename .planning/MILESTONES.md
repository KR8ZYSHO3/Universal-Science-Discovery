# Project Milestones: USDR

## v1.1 Core Development (Shipped: 2026-08-26)

**Delivered:** Four seed Crosscheck protocols CONFIRMED in CI, a repeatable generate/promote path, fail-closed CONFIRMED gates plus entry-point smokes, and a hub recommendations spec with a static JSON prototype.

**Phases completed:** 1–5 (11 plans total)

**Key accomplishments:**
- Habitat FSS, Ising EWI, cluster τ, and epidemic volume FSS (ν̄=3) all CI-gated `RESULT: CONFIRMED`
- Repeatable `generate_crosscheck.py --write` → human-promoted oncology GCC repro (`INCONCLUSIVE`, exit 0)
- Python-vs-browser/Colab run-mode parity documented; Python remains canonical
- CONFIRMED-gate inventory pytest + generate dry-run / GCC smokes in `tests/repo_smoke`
- Hub `#recommendations` loads `api/v1/recommendations.json` (undirected degree; not a scientific ranking)

**Stats:**
- PR #308 squash: 79 files, +11435 / −162
- 5 phases, 11 plans, 11/11 v1.1 requirements
- Timeline: GSD v1.1 locked 2026-06-23 → ship 2026-08-26
- Git: `#305` / `#304` planning lock → `#308` (`cda2526`)

**What's next:** v1.2 Launch (outreach, DNS, arXiv) remains **parked**. Ship Bar items ROBUST-01 / WORK-01 / WORK-02 / UI-01 are not a scheduled GSD milestone until the owner opens one. Progress continues via GSD in this repo (`.planning/`).

**Known deferred items at close:** 0 open GSD todos. Parked launch + Ship Bar leftovers (see STATE.md Deferred Items). No `v1.1-MILESTONE-AUDIT.md`.

---

## v1.0 Foundation (Shipped: prior to GSD v1.1)

**Delivered:** Schema-backed catalog at scale, knowledge graph, dashboard/GitHub Pages, Crosscheck hub runners, 3/4 seed CONFIRMED, core drift gate.

**Phases completed:** repo Phase 0 (not GSD-numbered)

See root `ROADMAP.md`.
