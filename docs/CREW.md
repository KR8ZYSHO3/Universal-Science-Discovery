# Night crew — agents on a clock

A small set of jobs that run while you sleep. They **propose**. They do not promote science.

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

## Mailbox

- Briefing file: `drafts/crew-reports/LATEST.md` (this *is* committed if the bot PR opens).
- Staged YAML: regenerate locally from the candidate JSON on that PR; it is not in git.
- Cadence workflow: [`.github/workflows/harvest-openalex.yml`](../.github/workflows/harvest-openalex.yml) — still **no push to `main`**.

## While you are at the keyboard

Grok **workflows** (`parallel` agents) are for one session: several reviewers at once. They stop when the session stops. The night crew is the part that keeps a clock.

## Why this stays small

Reuse of math only helps if identities are real. A larger unverified catalog is noise. The crew exists to surface candidates and catch honesty bugs (writeup vs runner), not to invent a golden age overnight.
