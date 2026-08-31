# USDR crew briefing

Generated **2026-08-31 12:19 UTC**. Foreman only; not a scientific result.

**Do not promote this run to `cross-domain/`, `unknowns-catalog/`, or `hypotheses/` without a human.**
Wave Factory output stays in gitignored `drafts/wave_factory/`.

Flags: skip_harvest=True, skip_scout=False

## Harvester

- skipped (`--skip-harvest`)

## Scout (Wave Factory)

- wave_factory exit **0**
- staged (gitignored): bridges=30, unknowns=30, hypotheses=30
- these are **candidates**, not findings. Human review before promote.
  `  [25] b-openalex-information-theory-evolutionary-biology-mega7-molecular-evolu score=0.685 (c=0.87, r=0.60, n=0.17)`
  `  [26] b-openalex-outcome-game-theory-evolutionary-biology-mega7-molecular-evol score=0.685 (c=0.87, r=0.60, n=0.17)`
  `  [27] b-openalex-renormalization-group-machine-learning-very-deep-convolutiona score=0.683 (c=0.91, r=0.52, n=0.17)`
  `  [28] b-openalex-statistical-mechanics-finance-reflecting-on-reflexive-them score=0.681 (c=0.80, r=0.72, n=0.17)`
  `  [29] b-openalex-renormalization-group-machine-learning-untitled score=0.677 (c=0.88, r=0.56, n=0.17)`
  `  [30] b-openalex-renormalization-group-machine-learning-going-deeper-with-conv score=0.674 (c=0.87, r=0.56, n=0.17)`
  `[wave-factory] Wrote 90 YAML files under drafts/wave_factory`
  `[wave-factory] Source mix: openalex=30`

## Auditor

- `validate_schemas.py` exit **0**
  `OK: all hypothesis, unknown-catalog, cross-domain bridge, crosscheck protocol, phenomenology, pioneer, and breakthrough-gap YAML files validate. (5 crosscheck protocols, 11 phenomenology entries, 18 pioneer entries, 24 breakthrough-gap entr`
- `promote_wave_factory_batch.py` dry-run exit **0** (never `--apply`)
  `[promote-wave-factory] Validation OK. Planned promotions: bridges=30, unknowns=30, hypotheses=30`
  `[promote-wave-factory] Dry-run only. Use --apply to move files.`
- `audit_quality.py` exit **0**
  `Quality Audit Results:`
  `  ERRORS:   0`
  `  WARNINGS: 0`
  `  INFO:     42`
  `Report written to /home/runner/work/Universal-Science-Discovery/Universal-Science-Discovery/drafts/crew-reports/quality.md`

## Tester (contracts only — no live exponent run)

- habitat JS cannot emit CONFIRMED: **yes**
- habitat Python either-wrap estimator present: **yes**
- Crosscheck CI workflow present: **yes**
- live Crosscheck Monte Carlo is **not** this crew's job (too long; human/CI).

## What you do next

1. Read this briefing (and the bot PR if one opened).
2. Open interesting staged YAML under `drafts/wave_factory/` locally.
3. If a triple is real math, promote with `python scripts/harvesters/promote_wave_factory_batch.py --stage drafts/wave_factory --apply` **after** you edited the translation table — never blindly.
4. Do not loosen Crosscheck gates so the night job looks greener.
