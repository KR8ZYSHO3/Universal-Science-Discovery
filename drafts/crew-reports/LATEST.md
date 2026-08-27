# USDR crew briefing

Generated **2026-08-27 17:36 UTC**. Foreman only; not a scientific result.

**Do not promote this run to `cross-domain/`, `unknowns-catalog/`, or `hypotheses/` without a human.**
Wave Factory output stays in gitignored `drafts/wave_factory/`.

Flags: skip_harvest=True, skip_scout=True

## Harvester

- skipped (`--skip-harvest`)

## Scout (Wave Factory)

- skipped (`--skip-scout`)

## Auditor

- `validate_schemas.py` exit **0**
  `OK: all hypothesis, unknown-catalog, cross-domain bridge, crosscheck protocol, phenomenology, pioneer, and breakthrough-gap YAML files validate. (5 crosscheck protocols, 11 phenomenology entries, 18 pioneer entries, 24 breakthrough-gap entr`
- `promote_wave_factory_batch.py` dry-run exit **0** (never `--apply`)
  `[promote-wave-factory] Validation OK. Planned promotions: bridges=4, unknowns=4, hypotheses=4`
  `[promote-wave-factory] Dry-run only. Use --apply to move files.`
- `audit_quality.py` exit **0**
  `Quality Audit Results:`
  `  ERRORS:   0`
  `  WARNINGS: 0`
  `  INFO:     42`
  `Report written to C:\Projects\Universal-Science-Discovery-git\drafts\crew-reports\quality.md`

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
