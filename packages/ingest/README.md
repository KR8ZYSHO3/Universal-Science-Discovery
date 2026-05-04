# `usdr-ingest`

**arXiv OAI-PMH → USDR envelope v1 JSONL** (metadata only; **no PDFs**). Policy and envelope spec: **[docs/DATA_PLAN.md](../../docs/DATA_PLAN.md)**, **[LEGAL.md](../../LEGAL.md)**.

## Install

From the repository root:

```bash
pip install -r requirements-ingest.txt
pip install -e "./packages/ingest[dev]"
```

## CLI

- `usdr-ingest --help` — subcommands: `harvest`, `version`
- `usdr-ingest harvest --help` — OAI window, `--dry-run`, `--max-records`, `-o` / `-m`

Example (see [docs/UAT_INGEST.md](../../docs/UAT_INGEST.md) for full manual QA):

```bash
usdr-ingest harvest --dry-run --max-records 1 --from 2024-01-01 --until 2024-01-02
```

## Tests

```bash
python -m pytest packages/ingest/tests -q
```

Envelope rows validate against [`schemas/ingestion-envelope-1.0.0.json`](../../schemas/ingestion-envelope-1.0.0.json) (see `tests/test_envelope_schema.py`).

## Layout

| Path | Role |
|------|------|
| `src/usdr_ingest/` | CLI, HTTP client, OAI XML parse, envelope build |
| `tests/` | CLI help, fixtures, schema validation |
