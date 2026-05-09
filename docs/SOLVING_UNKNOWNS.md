# Solving an unknown in USDR

This project catalogs **open questions** (`unknowns-catalog/u-*.yaml`), **testable claims** (`hypotheses/active/h-*.yaml`), and **cross-domain bridges** (`cross-domain/b-*.yaml`). “Solving” an unknown means moving from speculation to **documented, reviewable evidence**—not declaring victory without it.

## Resolution ladder

1. **Open** — no decisive evidence yet.
2. **Partial** — credible evidence exists but gaps, conflicts, or replication limits remain.
3. **Resolved** — the question is answered *for a stated scope* with references and (where applicable) reproducible methods.

Hypotheses follow their own enum (`draft` → `active` → `validated` / `refuted` / `archived`). Prefer updating hypothesis status **before** marking an unknown `resolved`.

## Minimum bar to mark an unknown `resolved`

- At least one linked hypothesis has been **`validated`** *or* the unknown’s summary explicitly states the answer with **primary references** (DOI / arXiv / stable URL).
- **Falsification paths** from active hypotheses have been addressed (not ignored).
- If the claim is quantitative or model-based, another contributor could **re-run** the stated method or find the same sources.

Do **not** mark `resolved` based only on intuition, uncited LLM output, or a single weak secondary source.

## Practical workflow

1. Pick `u-*` and read `related_bridges` / `suggested_hypotheses`.
2. Ensure there is an **`active`** hypothesis with clear `proposed_tests` and `falsification_criteria`.
3. Run literature checks, simulations, or experiments **outside** or alongside git; capture DOIs and notes in `evidence_links` on the hypothesis (each link needs `type`: `supporting`, `related`, or `contradicting`).
4. Update hypothesis `status` and unknown `status`; add `references` on the unknown if appropriate.
5. Refresh derived artifacts if you changed catalog links: `python scripts/validate_schemas.py`, `python -X utf8 scripts/build_graph.py`.
6. Note the resolution in `CHANGELOG.md` (Unreleased) if it is a notable closure.

## Graph hygiene

Stale cross-references (`related_unknowns` pointing at deleted IDs) produce **orphan edges** filtered at graph build time. To list missing IDs:

```bash
python scripts/build_graph.py --report-orphans
```

Fix YAML IDs or restore missing records so the graph matches the catalog.
