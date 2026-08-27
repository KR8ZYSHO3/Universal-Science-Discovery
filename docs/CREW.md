# Night crew — agents on a clock

A small set of jobs that run while you sleep. They **propose**, they **open a PR**, and they **ship that PR** when it is only the mailbox (harvest JSON + briefing). They do not promote science into the catalog.

This is not a chatbot left open. The clock is GitHub Actions (Monday + Thursday 06:00 UTC, or **Actions → Wave Factory Cadence → Run workflow**). Locally:

```bash
# Offline: audit catalog + Crosscheck contracts + write a briefing
python scripts/run_crew.py --skip-harvest --skip-scout

# After candidate JSON already exists (or after a harvest)
python scripts/run_crew.py --skip-harvest

# Full: harvest APIs + scout + audit + brief (needs network)
python scripts/run_crew.py
```

## Roles

| Role | What it does | What it never does |
|------|----------------|-------------------|
| **Harvester** | OpenAlex / PubMed / Semantic Scholar metadata | Store full papers; invent DOIs |
| **Scout** | Wave Factory ranks and stages triples in `drafts/wave_factory/` (gitignored) | Write into `cross-domain/` or mark a bridge confirmed |
| **Auditor** | `validate_schemas.py`, promote **dry-run**, `audit_quality.py` | `--apply` promotion |
| **Tester** | Checks Crosscheck *contracts* (habitat JS cannot emit CONFIRMED) | Run the habitat Monte Carlo; rewrite `RESULT:` |
| **Foreman** | Writes [`drafts/crew-reports/LATEST.md`](../drafts/crew-reports/LATEST.md) | Treat the briefing as evidence |
| **Shipper** | Opens the bot PR and squash-merges it **if and only if** files are harvest JSON + `drafts/crew-reports/` | Merge `cross-domain/`, unknowns, hypotheses, repro, or schemas |

## Mailbox

- Briefing file: `drafts/crew-reports/LATEST.md` (landed on `main` when the Shipper can merge).
- Staged YAML: regenerate locally from the candidate JSON; it is not in git. Artifact on the Actions run.
- Cadence workflow: [`.github/workflows/harvest-openalex.yml`](../.github/workflows/harvest-openalex.yml).
- Allowlist lives in [`scripts/crew_ship.py`](../scripts/crew_ship.py). If GitHub branch protection blocks the Actions token from merging, the PR stays open — that is still a shipped *request*. Enable “Allow GitHub Actions to create and approve pull requests” if you want the merge to complete unattended.

Catalog science still needs a human: `promote_wave_factory_batch.py --apply` after you edit the translation table.

## While you are at the keyboard

Grok **workflows** (`parallel` agents) are for one session: several reviewers at once. They stop when the session stops. The night crew is the part that keeps a clock.

## Why this stays small

Reuse of math only helps if identities are real. A larger unverified catalog is noise. The crew exists to surface candidates and catch honesty bugs (writeup vs runner), not to invent a golden age overnight.
