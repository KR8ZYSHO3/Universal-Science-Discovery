# Scripts

Place reproducible automation here (Python, R, Julia, shell, and so on).

- **Record validation:** `python scripts/validate_schemas.py` (see [requirements-validate.txt](requirements-validate.txt); also runs in GitHub Actions).
- **Contributor hub stats:** `python scripts/update_dashboard_stats.py --apply` — patches `dashboard/index.html` catalog counters, hero **live snapshot** row (`snap-bridges`, `snap-unknowns`, etc.), social meta, and (when `docs/knowledge_graph.json` exists) graph node/edge placeholders and API blurbs. Typical order: `validate_schemas` → `build_graph.py` → `update_dashboard_stats.py --apply`.
- **Hub drift guard:** `python scripts/verify_dashboard_consistency.py` — asserts YAML + graph JSON match dashboard `snap-*` / `stat-*` / hero pill (runs in **`validate-schemas.yml`**). Full maintainer checklist: **[docs/DEV_DASHBOARD.md](../docs/DEV_DASHBOARD.md)**.
- **Domain browse pages:** `python scripts/generate_domain_pages.py` — rebuilds `dashboard/domains/*.html` + index from `unknowns-catalog/` + bridge `fields` (see `scripts/domain_matching.py`). Regression check: `python scripts/verify_domain_pages.py`. Also invoked from **`build-graph.yml`** after catalog edits.
- **Preprint HTML:** `python scripts/render_preprint_html.py --apply` — rebuilds `docs/preprint/usdr_preprint.html` from `usdr_preprint.md` (needs **`markdown`** from `requirements-docs.txt`).
- **Breakthrough gaps hub grid:** `python scripts/render_breakthrough_gaps_hub.py --apply` — injects cards into `dashboard/index.html` from `breakthrough-gaps/bg-*.yaml`. See **`docs/BREAKTHROUGH_GAPS.md`**.
- **Ingest exemplar JSONL:** `python scripts/generate-ingest-example-jsonl.py` — refreshes [docs/examples/arxiv-oai-metadata-sample.v1.jsonl](../docs/examples/arxiv-oai-metadata-sample.v1.jsonl) from offline OAI fixtures; set stable `retrieved_at` before committing (see [docs/examples/README.md](../docs/examples/README.md)).
- Add dependency notes (`requirements.txt`, `environment.yml`, or equivalent) alongside nontrivial scripts.
- Prefer idempotent scripts with clear CLI or top-level configuration.
- When pipelines grow, add a `RUNBOOK.md` in this folder.
