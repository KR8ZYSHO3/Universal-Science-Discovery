# Scripts

Place reproducible automation here (Python, R, Julia, shell, and so on).

- **Record validation:** `python scripts/validate_schemas.py` (see [requirements-validate.txt](requirements-validate.txt); also runs in GitHub Actions).
- Add dependency notes (`requirements.txt`, `environment.yml`, or equivalent) alongside nontrivial scripts.
- Prefer idempotent scripts with clear CLI or top-level configuration.
- When pipelines grow, add a `RUNBOOK.md` in this folder.
