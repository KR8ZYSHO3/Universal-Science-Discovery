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
