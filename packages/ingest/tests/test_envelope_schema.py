"""Harvest output rows must satisfy schemas/ingestion-envelope-1.0.0.json."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas" / "ingestion-envelope-1.0.0.json"
EXAMPLE_JSONL = REPO_ROOT / "docs" / "examples" / "arxiv-oai-metadata-sample.v1.jsonl"


@pytest.fixture(scope="module")
def envelope_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def test_envelope_schema_file_exists() -> None:
    assert SCHEMA_PATH.is_file(), f"missing {SCHEMA_PATH}"


def test_harvest_rows_validate_against_envelope_schema(
    envelope_validator: Draft202012Validator,
) -> None:
    import httpx

    from usdr_ingest.constants import USER_AGENT
    from usdr_ingest.harvest import HarvestStats, harvest_envelope_rows

    from test_harvest_mock import _transport

    rows: list[dict] = []
    with httpx.Client(
        transport=_transport(),
        headers={"User-Agent": USER_AGENT},
    ) as client:
        for row in harvest_envelope_rows(
            "http://example.test/oai",
            http_client=client,
            stats=HarvestStats(),
        ):
            rows.append(row)

    assert rows, "expected at least one harvested row"
    for row in rows:
        envelope_validator.validate(row)


def test_docs_example_jsonl_validates_against_envelope_schema(
    envelope_validator: Draft202012Validator,
) -> None:
    assert EXAMPLE_JSONL.is_file(), f"missing checked-in exemplar {EXAMPLE_JSONL}"
    lines = [
        ln
        for ln in EXAMPLE_JSONL.read_text(encoding="utf-8").splitlines()
        if ln.strip()
    ]
    assert lines, "expected at least one JSONL row in docs example"
    for line in lines:
        envelope_validator.validate(json.loads(line))