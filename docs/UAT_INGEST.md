# User acceptance — `usdr-ingest` (pilot)

Manual checks for the [`packages/ingest`](../packages/ingest) CLI. **Automated contract** is `pytest packages/ingest/tests` (fixtures + envelope schema). Policy: [DATA_PLAN.md](DATA_PLAN.md), [LEGAL.md](../LEGAL.md) — **metadata only**, no PDFs or full text.

## Preconditions

From the repository root:

```bash
pip install -r requirements-ingest.txt
pip install -e "./packages/ingest[dev]"
```

## Automated (run before merge or release)

```bash
python -m pytest packages/ingest/tests -q
```

## CLI smoke (no network)

- `usdr-ingest --help` — Typer help; `harvest` and `version` subcommands listed.
- `usdr-ingest harvest --help` — OAI options, `--dry-run`, `--max-records`, `--output`, `--manifest`.
- `usdr-ingest version` — prints installed package version.

## Optional live OAI check (network)

Use only if you accept **minimal traffic** to arXiv’s OAI endpoint and comply with current [arXiv OAI / terms](https://arxiv.org/help/oa). Prefer **`--dry-run`** and **`--max-records 1`** (or similarly small).

Example:

```bash
usdr-ingest harvest --dry-run --max-records 1 --from 2024-01-01 --until 2024-01-02
```

Expect **stderr** JSON with `dry_run`, `base_url`, and counters (`list_requests`, `get_requests`, etc.). To emit one JSONL envelope line to a **local** file, omit `--dry-run`, add e.g. `-o sample.jsonl`, inspect the line, then delete — **do not commit** ad hoc harvest output without maintainer review ([ETHICS_REPRODUCIBILITY_AND_DATA.md](ETHICS_REPRODUCIBILITY_AND_DATA.md)).

Default OAI base is HTTPS `export.arxiv.org/oai` (see `packages/ingest`); override only when testing against a documented endpoint.

## Envelope validation

Each output line MUST validate against [`schemas/ingestion-envelope-1.0.0.json`](../schemas/ingestion-envelope-1.0.0.json). Tests cover this; for ad hoc lines use your JSON Schema tool of choice or extend pytest locally.
