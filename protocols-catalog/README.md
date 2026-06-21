# Crosscheck Protocol Catalog

Schema-validated, reproducible experiment protocols derived from USDR cross-domain bridges.

Each file is a `p-*.yaml` record validated against [`schemas/protocol.yaml`](../schemas/protocol.yaml).

| Status | Meaning |
|--------|---------|
| `draft` | Auto-generated or incomplete — not yet promoted |
| `ready` | Human-reviewed, runnable |
| `executed` | Repro bundle has been run |
| `confirmed` | Results support the falsifiable prediction |
| `falsified` | Results refute the falsifiable prediction |

**Generate drafts:** `python scripts/generate_crosscheck.py --bridge b-{id} --write`

**Manifesto:** [docs/CROSSCHECK.md](../docs/CROSSCHECK.md)