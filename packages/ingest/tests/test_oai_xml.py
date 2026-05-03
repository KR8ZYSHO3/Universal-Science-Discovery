"""Unit tests for OAI XML parsers (fixture files; no HTTP)."""

from pathlib import Path

import pytest

from usdr_ingest.oai_xml import (
    OAIProtocolError,
    parse_get_record,
    parse_list_identifiers,
)

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def test_parse_listidentifiers_page_one() -> None:
    xml = (FIXTURES / "listidentifiers_page1.xml").read_bytes()
    headers, token = parse_list_identifiers(xml)
    assert token == "page-two-token"
    ids = [h.identifier for h in headers]
    assert ids == ["oai:arXiv.org:2401.00001v1", "oai:arXiv.org:2401.00002v1"]
    assert headers[0].datestamp == "2024-01-10"


def test_parse_listidentifiers_page_two() -> None:
    xml = (FIXTURES / "listidentifiers_page2.xml").read_bytes()
    headers, token = parse_list_identifiers(xml)
    assert token is None
    assert len(headers) == 1


def test_parse_getrecord_roundtrip_metadata() -> None:
    xml = (FIXTURES / "getrecord_2401_00001.xml").read_bytes()
    rec = parse_get_record(xml)
    assert rec is not None
    assert rec.header.identifier == "oai:arXiv.org:2401.00001v1"
    assert rec.title == "Example paper one"
    assert rec.abstract == "Abstract for paper one."
    assert rec.creators == ["Doe, Jane"]
    assert rec.dates == ["2024-01-09"]
    assert rec.subjects == ["cs.AI"]


def test_deleted_get_record_returns_none() -> None:
    xml = (FIXTURES / "getrecord_2401_00003.xml").read_bytes()
    assert parse_get_record(xml) is None


def test_oai_error_response() -> None:
    xml = b"""<?xml version="1.0" encoding="UTF-8"?>
<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/">
  <responseDate>2024-01-15T12:00:00Z</responseDate>
  <request verb="ListIdentifiers"/>
  <error code="badArgument">Malformed request</error>
</OAI-PMH>
"""
    with pytest.raises(OAIProtocolError):
        parse_list_identifiers(xml)
