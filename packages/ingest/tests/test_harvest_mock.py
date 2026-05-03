"""Integrated harvest tests with httpx.MockTransport (recorded fixtures)."""

from pathlib import Path
from urllib.parse import parse_qs, urlparse

import httpx

from usdr_ingest.client import fetch_oai_xml
from usdr_ingest.constants import USER_AGENT
from usdr_ingest.harvest import HarvestStats, harvest_envelope_rows

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def _transport() -> httpx.MockTransport:
    p1 = (FIXTURES / "listidentifiers_page1.xml").read_bytes()
    p2 = (FIXTURES / "listidentifiers_page2.xml").read_bytes()
    g1 = (FIXTURES / "getrecord_2401_00001.xml").read_bytes()
    g2 = (FIXTURES / "getrecord_2401_00002.xml").read_bytes()
    g3 = (FIXTURES / "getrecord_2401_00003.xml").read_bytes()

    def handler(request: httpx.Request) -> httpx.Response:
        qs = parse_qs(urlparse(str(request.url)).query)
        verb = (qs.get("verb") or [None])[0]
        if verb == "ListIdentifiers":
            rt = (qs.get("resumptionToken") or [None])[0]
            if rt is None:
                return httpx.Response(200, content=p1)
            if rt == "page-two-token":
                return httpx.Response(200, content=p2)
            return httpx.Response(500, content=b"unexpected resumption token")
        if verb == "GetRecord":
            ident = (qs.get("identifier") or [""])[0]
            if "2401.00001" in ident:
                return httpx.Response(200, content=g1)
            if "2401.00002" in ident:
                return httpx.Response(200, content=g2)
            if "2401.00003" in ident:
                return httpx.Response(200, content=g3)
        return httpx.Response(404, content=b"")

    return httpx.MockTransport(handler)


def test_harvest_streams_envelopes_fixture_chain() -> None:
    stats = HarvestStats()
    rows: list[dict] = []
    with httpx.Client(
        transport=_transport(),
        headers={"User-Agent": USER_AGENT},
    ) as client:
        for row in harvest_envelope_rows(
            "http://example.test/oai",
            http_client=client,
            stats=stats,
        ):
            rows.append(row)

    assert len(rows) == 2
    assert stats.list_requests == 2
    assert stats.get_requests == 3
    assert stats.records_emitted == 2
    assert stats.skipped_deleted == 1
    assert stats.stopped_reason == "complete"

    r0 = rows[0]
    assert r0["envelope_version"] == "1.0.0"
    assert r0["source_system"] == "arxiv_oai"
    assert r0["source_id"] == "2401.00001v1"
    assert r0["title"] == "Example paper one"
    assert r0["source_record_url"] == "https://arxiv.org/abs/2401.00001v1"
    assert r0["authors"] == [{"name": "Doe, Jane"}]
    assert "license_or_status" in r0


def test_user_agent_is_project_identifiable() -> None:
    seen: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request.headers.get("user-agent", ""))
        return httpx.Response(
            200,
            content=(FIXTURES / "listidentifiers_page2.xml").read_bytes(),
        )

    with httpx.Client(
        transport=httpx.MockTransport(handler),
        headers={"User-Agent": USER_AGENT},
    ) as c:
        fetch_oai_xml(
            "http://example.test/",
            {"verb": "ListIdentifiers"},
            client=c,
            max_retries=2,
        )

    assert any("Universal-Science-Discovery" in ua for ua in seen)


def test_max_records_stops_early() -> None:
    stats = HarvestStats()
    with httpx.Client(
        transport=_transport(),
        headers={"User-Agent": USER_AGENT},
    ) as client:
        rows = list(
            harvest_envelope_rows(
                "http://example.test/",
                http_client=client,
                stats=stats,
                max_records=1,
            )
        )
    assert len(rows) == 1
    assert stats.stopped_reason == "max_records"
    assert stats.records_emitted == 1


def test_manifest_fields_present_on_rows() -> None:
    stats = HarvestStats()
    with httpx.Client(
        transport=_transport(),
        headers={"User-Agent": USER_AGENT},
    ) as client:
        row = next(
            harvest_envelope_rows(
                "http://example/",
                http_client=client,
                stats=stats,
                max_records=1,
            )
        )
    assert "ingestion_cursor" in row
    assert "legal_note" in row
