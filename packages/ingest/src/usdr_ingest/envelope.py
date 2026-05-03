"""Build ingestion envelope dicts compatible with docs/DATA_PLAN.md v1.0.0."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional
from urllib.parse import quote

from usdr_ingest.constants import (
    ENVELOPE_VERSION,
    LEGAL_NOTE_DEFAULT,
    LICENSE_OR_STATUS,
    SOURCE_SYSTEM,
)
from usdr_ingest.oai_xml import ParsedRecord


def utc_now_iso_z() -> str:
    """RFC 3339 UTC with trailing Z."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def abs_url_from_oai_identifier(oai_identifier: str) -> str:
    """Best-effort arXiv abs URL from OAI identifier (e.g. oai:arXiv.org:2401.00001v1)."""
    tail = oai_identifier.split(":")[-1].strip()
    return "https://arxiv.org/abs/" + quote(tail, safe="./-_")


def build_envelope(
    parsed: ParsedRecord,
    *,
    retrieved_at: Optional[str] = None,
    ingestion_cursor: Optional[str] = None,
) -> dict:
    """Produce one JSON-object row for JSONL export."""
    retrieved = retrieved_at or utc_now_iso_z()
    local_id = parsed.header.identifier.split(":")[-1].strip()

    authors = [{"name": n} for n in parsed.creators]
    published_at = parsed.dates[0] if parsed.dates else None

    row = {
        "envelope_version": ENVELOPE_VERSION,
        "source_system": SOURCE_SYSTEM,
        "source_id": local_id or parsed.header.identifier,
        "source_record_url": abs_url_from_oai_identifier(parsed.header.identifier),
        "retrieved_at": retrieved,
        "license_or_status": LICENSE_OR_STATUS,
        "legal_note": LEGAL_NOTE_DEFAULT,
        "ingestion_cursor": ingestion_cursor,
    }
    if parsed.title:
        row["title"] = parsed.title
    if parsed.abstract:
        row["abstract"] = parsed.abstract
    if authors:
        row["authors"] = authors
    if published_at:
        row["published_at"] = published_at
    if parsed.subjects:
        row["subjects"] = parsed.subjects
    # Drop None-valued optional canonical keys for cleaner JSONL (envelope allows extra props)
    return {k: v for k, v in row.items() if v is not None}
