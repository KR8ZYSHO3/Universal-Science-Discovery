"""Typer CLI — arXiv OAI-PMH metadata only (ListIdentifiers + GetRecord)."""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import httpx
import typer

from usdr_ingest.constants import (
    DEFAULT_ARXIV_OAI_BASE,
    USER_AGENT,
)
from usdr_ingest.constants import ENVELOPE_VERSION as DOC_ENVELOPE_VER
from usdr_ingest.constants import SOURCE_SYSTEM as DOC_SOURCE
from usdr_ingest import __version__ as PKG_VERSION
from usdr_ingest.harvest import HarvestStats, harvest_envelope_rows


app = typer.Typer(
    help="USDR arXiv OAI-PMH metadata ingest (metadata only; see docs/DATA_PLAN.md).",
    invoke_without_command=False,
    no_args_is_help=True,
    add_completion=False,
)


@app.command("version")
def version_cmd() -> None:
    """Print installed usdr-ingest version."""
    typer.echo(PKG_VERSION)


@app.command("harvest")
def harvest_cmd(
    output: Optional[Path] = typer.Option(
        None,
        "--output",
        "-o",
        help="JSONL output file; default: stdout",
    ),
    manifest: Optional[Path] = typer.Option(
        None,
        "--manifest",
        "-m",
        help="Optional manifest sidecar (JSON summary).",
    ),
    base_url: str = typer.Option(
        DEFAULT_ARXIV_OAI_BASE,
        "--base-url",
        help="OAI-PMH base URL (arXiv HTTPS recommended).",
    ),
    frm: Optional[str] = typer.Option(
        None,
        "--from",
        help="ListIdentifiers from (OAI date/datetime; YYYY-MM-DD or UTC).",
    ),
    until: Optional[str] = typer.Option(
        None,
        "--until",
        help="ListIdentifiers until (OAI date/datetime).",
    ),
    set_spec: Optional[str] = typer.Option(
        None,
        "--set",
        help="Optional OAI SetSpec slice.",
    ),
    max_records: Optional[int] = typer.Option(
        None,
        "--max-records",
        help="Stop after this many emitted records (each GetRecord).",
    ),
    metadata_prefix: str = typer.Option(
        "oai_dc",
        "--metadata-prefix",
        help="OAI metadataPrefix (arXiv pilot: oai_dc).",
    ),
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        help="Do not write JSONL/manifest; print summary to stderr.",
    ),
) -> None:
    """Harvest arXiv OAI metadata into DATA_PLAN envelope v1 JSONL (no PDFs)."""
    stats = HarvestStats()
    started = datetime.now(timezone.utc)

    out_f = sys.stdout
    owns_out = False
    if output is not None and not dry_run:
        out_f = open(output, "w", encoding="utf-8")
        owns_out = True

    try:
        with httpx.Client(
            headers={"User-Agent": USER_AGENT},
            timeout=60.0,
            follow_redirects=True,
        ) as http_client:
            for row in harvest_envelope_rows(
                base_url,
                metadata_prefix=metadata_prefix,
                frm=frm,
                until=until,
                set_spec=set_spec,
                max_records=max_records,
                http_client=http_client,
                stats=stats,
            ):
                if dry_run:
                    continue
                out_f.write(json.dumps(row, ensure_ascii=False) + "\n")
                out_f.flush()

            if dry_run:
                typer.echo(
                    json.dumps(
                        {
                            "dry_run": True,
                            "base_url": base_url,
                            **stats.__dict__,
                        },
                        indent=2,
                        default=str,
                    ),
                    err=True,
                )
                return

            if manifest:
                man = {
                    "generated_at": started.strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "finished_at": datetime.now(timezone.utc).strftime(
                        "%Y-%m-%dT%H:%M:%SZ"
                    ),
                    "envelope_version": DOC_ENVELOPE_VER,
                    "source_system": DOC_SOURCE,
                    "base_url": base_url.rstrip("/"),
                    "metadata_prefix": metadata_prefix,
                    "from": frm,
                    "until": until,
                    "set": set_spec,
                    "max_records": max_records,
                    "record_count": stats.records_emitted,
                    "list_requests": stats.list_requests,
                    "get_requests": stats.get_requests,
                    "skipped_deleted": stats.skipped_deleted,
                    "last_resumption_token": stats.last_resumption_token,
                    "stopped_reason": stats.stopped_reason,
                }
                manifest.write_text(
                    json.dumps(man, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8",
                )
    finally:
        if owns_out and out_f is not sys.stdout:
            out_f.close()


def main() -> None:
    app()


if __name__ == "__main__":
    main()
