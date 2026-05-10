# USDR full repository audit — May 2026

**Scope:** Repository inventory, governance alignment (see `docs/VISION_AND_SCOPE.md`, `docs/METHODOLOGY.md`, `docs/ETHICS_REPRODUCIBILITY_AND_DATA.md`), documentation drift, CI/tooling, contributor hub, security/reproducibility snapshot.  
**Method:** Static review of tracked paths, workflow descriptors, script surfaces, and spot-checks against live YAML/graph counts (no independent re-validation of scientific claims).  
**Counts verified locally (2026-05-10):** `cross-domain/**` bridge YAML **1,123**; `unknowns-catalog/**` **1,408**; `hypotheses/**` **1,274**; `phenomenology/**` **10**; `breakthrough-gaps/bg-*.yaml` **24**; `docs/knowledge_graph.json` meta **3,857** nodes / **4,517** edges.

---

## Executive summary

### Strengths

- **Strong structural discipline:** Schema-backed YAML for bridges, unknowns, hypotheses, pioneers, phenomena, breakthrough gaps; CI validates catalogs and dashboard count consistency (`validate-schemas.yml`, `verify_dashboard_consistency.py`).
- **Reproducible artifacts:** Knowledge graph and API generation wired into `build-graph.yml`; contributor playbook in `docs/DEV_DASHBOARD.md`; ethics/data boundaries documented in `docs/ETHICS_REPRODUCIBILITY_AND_DATA.md`.
- **Honest labeling posture:** Methodology and templates distinguish hypotheses vs findings; many bridge records carry explicit speculation/analogy caveats (pattern visible in catalog and STATE history).

### Risks

- **Planning-document drift:** Long-form `ROADMAP.md` milestone tables and `.planning/STATE.md` “Catalog state” froze at older counts (e.g. ~868–904 bridges, 12 breakthrough gaps) while README/graph reflect **1,123** / **24** — undermines maintainer and agent trust.
- **Automated vs narrative metrics:** Discovery engine cards embed **hand-maintained** “unknowns” counts in `dashboard/index.html` JS; easy to drift from the catalog.
- **Test coverage skew:** Automated tests concentrate on `packages/ingest/`; most `scripts/*.py` rely on CI scripts + manual runs — regressions are catchable but not unit-isolated.

### Top 10 actions (prioritized)

1. **Reconcile ROADMAP `Foundation achievement snapshot` and milestone bullets** with README + `docs/knowledge_graph.json` meta (or auto-link “see README for live counts”).
2. **Refresh `.planning/STATE.md` catalog table** after large waves (same numbers as README).
3. **Clarify hub “Discovery Engines”** as curated thematic shortcuts (not exhaustive coverage); link maintainer playbook (`docs/DEV_DASHBOARD.md`).
4. **Reduce breakthrough-gap friction to catalog search** (e.g. `data-search-query` + Alt-click affordance; steward note in `docs/BREAKTHROUGH_GAPS.md`).
5. **Resolve duplicate validation story:** `.github/workflows/validate.yml` (path-filtered on PR) vs `validate-schemas.yml` (broad) — document which gates merge / branch protection (`docs/OPERATING_RHYTHM.md` already notes ingest caveat; extend for validate split).
6. **README precision pass:** “Every entry … DOI-linked” is stronger than evidence guarantees across all record types — soften or qualify per schema requirements.
7. **Script test harness (incremental):** smoke tests for `validate_schemas.py`, `verify_dashboard_consistency.py`, `build_graph.py --report-orphans` on a tiny fixture subset.
8. **Graph reliability:** Continue tracking D3/load-path failures on GitHub Pages (listed in STATE “Current focus”) with reproduced console/network evidence per incident.
9. **Draft promotion hygiene:** Keep `drafts/` policy visible (`drafts/wave_factory/` gitignored — good); periodically audit remaining tracked drafts.
10. **MkDocs vs Pages:** Full repo deploy for Pages artifact (`pages.yml` uses `path: '.'`) — confirm newcomer expectations vs MkDocs site (`mkdocs-gh-pages.yml`) to avoid two “official” doc URLs without explanation.

---

## Inventory

| Area | Role | Primary paths / automation |
|------|------|----------------------------|
| **Catalog** | Bridges, unknowns, hypotheses, pioneers, phenomena | `cross-domain/`, `unknowns-catalog/`, `hypotheses/`, `pioneers/`, `phenomenology/` |
| **Breakthrough gaps** | High-impact problem stubs | `breakthrough-gaps/*.yaml`; `scripts/render_breakthrough_gaps_hub.py`; `api/v1/breakthrough_gaps.json` |
| **Graph / API** | Compiled graph + static JSON | `scripts/build_graph.py`, `scripts/generate_api.py` → `docs/knowledge_graph.json`, `api/v1/` |
| **CI** | Validation, graph build, Pages, MkDocs, link check, harvest | `.github/workflows/*.yml` (notably `validate-schemas.yml`, `validate.yml`, `build-graph.yml`, `pages.yml`, `mkdocs-build.yml`, `markdown-link-check.yml`, `harvest-openalex.yml`, `ingest-ci.yml`) |
| **Dashboard / hub** | Contributor-facing HTML | `dashboard/index.html`, `dashboard/domains/`, `scripts/update_dashboard_stats.py`, `verify_dashboard_consistency.py` |
| **MkDocs** | Policy/readthedocs-style site | `mkdocs.yml`, `docs/**/*.md` |
| **Ingest** | arXiv OAI envelope CLI + tests | `packages/ingest/`, `docs/DATA_PLAN.md`, `docs/UAT_INGEST.md` |
| **Scripts** | Harvesters, audits, generators | `scripts/`, `scripts/harvesters/` |
| **Governance docs** | Policy traceability | `AGENTS.md`, `docs/DOC_MAP.md`, `docs/REPOSITORY_MANIFEST.md`, core ethics/methodology set |
| **Phenomenology** | Pre-formal observations | `phenomenology/`, `schemas/phenomenon.yaml` |
| **Drafts** | Staging | `drafts/` (Wave Factory output gitignored per STATE) |
| **Domains** | Domain landing pages | `dashboard/domains/`, `scripts/generate_domain_pages.py`, `domain_matching.py` |
| **Tests** | Pytest | `packages/ingest/tests/` (4 modules); root `pyproject.toml` pytest entry |

---

## Underdeveloped areas (with evidence)

| Area | Evidence |
|------|----------|
| **Unit tests for catalog tooling** | Tests under `packages/ingest/tests/` only; no parallel suite for `scripts/build_graph.py`, `validate_schemas.py`, `generate_domain_pages.py`, harvesters. |
| **ROADMAP / STATE numeric freshness** | `ROADMAP.md` “Foundation achievement snapshot (as of 2026-05-07)” still lists **868** bridges and aligned milestones; `.planning/STATE.md` catalog table lists **904** bridges and **12** breakthrough gaps — contradicts README **1,123** / **24** (verified 2026-05-10). |
| **Discovery engine metrics** | `dashboard/index.html` `discoveryEngines` array includes static `unknowns: N` per theme — no CI check against catalog. |
| **Workflow discoverability** | Two PR validation paths (`validate.yml` path-limited vs `validate-schemas.yml` full); contributors may not know which runs on their PR without reading YAML. |
| **Breakthrough → catalog UX** | Prior to this audit’s hub tweak proposal, cards linked only to GitHub YAML — no structured bridge to Lunr catalog search. |
| **`.planning/` breadth** | Aside from `STATE.md`, limited archived planning artifacts in-repo (may be intentional — note for maintainers). |

---

## Issues found

| Severity | Category | Evidence | Suggested fix |
|----------|----------|----------|----------------|
| HIGH | Documentation drift | `ROADMAP.md` ~L95–125 “Current counts” / milestones: **868** bridges vs actual **1,123** | Refresh table or replace static counts with pointer to README + graph meta |
| HIGH | Maintainer state drift | `.planning/STATE.md` “Catalog state” ~L160–174: **904** bridges, **12** breakthrough gaps | Update table after each wave batch; or generate from script |
| MED | UX honesty | `dashboard/index.html` Discovery Engines copy presents “six thematic lenses” without stating curation limits | Clarify scope + link `docs/DEV_DASHBOARD.md` |
| MED | README absolutism | `README.md` ~L54 “Every entry … DOI-linked” | Qualify per record type / schema minimums |
| MED | CI clarity | `.github/workflows/validate.yml` vs `validate-schemas.yml` overlap | Document merge gates in `docs/DOC_MAP.md` or `OPERATING_RHYTHM.md` |
| LOW | Manual metrics | `discoveryEngines[].unknowns` static | Derive from API or drop counts |
| LOW | Test gap | No pytest for `scripts/*.py` beyond ingest | Add smoke tests incrementally |
| LOW | Dual doc sites | MkDocs deploy workflow + raw `docs/` on Pages root | Short pointer in README or INTERFACE |

---

## Documentation drift

| Pair | Observation |
|------|-------------|
| **README vs ROADMAP snapshot** | README reflects **1,123** bridges; ROADMAP foundation snapshot still **868** until refreshed. |
| **README vs STATE catalog table** | README **24** breakthrough gaps; STATE table **12**. |
| **Preprint vs README** | `docs/preprint/usdr_preprint.md` abstract aligns with README-scale metrics (spot-check 2026-05-10) — **no drift flagged** for headline counts. |
| **DOC_MAP** | Workflow table lists `validate.yml` behavior; does not spell out dual-validator strategy — minor gap addressed via backlog + optional doc row. |

---

## Security / reproducibility (quick pass)

- **Secrets:** No secrets committed in this audit’s sampled paths; `dashboard/deploy-info.json` gitignored for Pages metadata (good). Harvest workflows should continue using GitHub Actions secrets only where needed — not expanded here.
- **Raw / restricted data:** `docs/ETHICS_REPRODUCIBILITY_AND_DATA.md` + `data/README.md` pattern upheld; `data/raw/.gitkeep` placeholder; ingest docs emphasize metadata envelopes — consistent with scope.
- **Reproducibility:** Graph/API regeneration paths documented; Wave Factory staging gitignored — reduces accidental bulk promotion.

---

## Speculation / limits

- **DOI ubiquity:** Whether *every* hypothesis/unknown satisfies “DOI-linked” in practice was **not** exhaustively verified; treating README wording as potentially overstated is a documentation judgment, not a statistical audit.
- **Scientific accuracy of catalog entries:** Out of scope for this engineering audit; methodology expects labeled speculation and review via contribution workflow.

---

## Related changes shipped with this report

- `ROADMAP.md` — **Audit backlog (2026-05)** subsection.
- `.planning/STATE.md` — audit completion bullet + refreshed catalog figures (target).
- Hub/tooling tweaks as merged on the same branch (breakthrough `data-search-query`, Discovery Engines copy, optional Alt-click catalog jump).
