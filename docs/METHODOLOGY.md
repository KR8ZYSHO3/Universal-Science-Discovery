# Methodology

## Evidence bar

Before labeling work as a **finding**:

1. State the hypothesis and the falsification criteria (what would convince you the hypothesis is wrong).
2. List data sources and versions; link protocols in [methods/](../methods/) or equivalent.
3. Describe analysis steps enough that another researcher could critique or reproduce the logic (code or pseudocode as appropriate).
4. List limitations, confounders, and alternative explanations.

## Claims discipline

- Separate **results** (what was observed or computed) from **interpretation**.
- Mark confidence: exploratory, provisional, supported (with caveats), or established (only when externally validated or exceptionally well evidenced).
- When using generative or automated assistants, note where summaries were AI-assisted and verify citations against primary sources.

## Branch and naming conventions (suggested)

- `main` stays integration-ready; use short-lived branches: `topic/<slug>`, `fix/<slug>`, `docs/<slug>`.
- Prefix issue titles for triage: `[Hypothesis]`, `[Methods]`, `[Finding]`, `[Docs]`, `[Tooling]`.

## Outputs

- Place generated tables, figures, and exports that belong in version control under [artifacts/](../artifacts/) with a short README note on how they were produced.
- Prefer deterministic scripts in [scripts/](../scripts/) over one-off undocumented steps.

---

## Data Harvesting

The harvest-to-unknown pipeline integrates external scientific databases to surface bridge candidates and open questions.

### Pipeline stages

1. **API query** — A harvester script in `scripts/harvesters/` queries an external source (e.g., OpenAlex, PubMed) for papers matching a cross-domain concept pair (e.g., "Percolation theory" + "Ecology"). Only metadata and abstracts are retrieved; full paper text is never ingested.

2. **Abstract analysis** — The harvester reconstructs the abstract, extracts concept tags, and computes citation counts. It records a `bridge_hint` field encoding the two-field span.

3. **Candidate YAML stub** — Promising papers are serialized to a JSON staging file under `drafts/` (e.g., `drafts/openalex_candidates.json`). Each entry carries source attribution (DOI, API source, harvest date) to satisfy `docs/ETHICS_REPRODUCIBILITY_AND_DATA.md`.

4. **Human expert review** — A domain expert reads the stub, evaluates scientific plausibility, updates confidence levels, and converts the entry to a structured YAML record.

5. **Merge to main** — Reviewed records are promoted to `cross-domain/` (bridges) or `unknowns-catalog/` (open questions) via a normal PR. CI validates schema before merge. No harvested stub reaches `main` without human sign-off.

### Traceability

- Every merged record retains `source:` and `doi:` fields linking back to the originating paper.
- Harvest scripts are deterministic: re-running with the same concept pair and `--top` value reproduces the same candidate list (modulo upstream API updates).
- See `docs/DATA_SOURCES.md` for the full catalog of integrated and planned sources.

