#!/usr/bin/env python3
"""Emit docs/examples/arxiv-oai-metadata-sample.v1.jsonl from OAI XML fixtures (offline)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import httpx
from urllib.parse import parse_qs, urlparse

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / "packages" / "ingest" / "src"))

from usdr_ingest.constants import USER_AGENT  # noqa: E402
from usdr_ingest.harvest import harvest_envelope_rows  # noqa: E402

FIXTURES = REPO_ROOT / "packages" / "ingest" / "tests" / "fixtures"
OUT = REPO_ROOT / "docs" / "examples" / "arxiv-oai-metadata-sample.v1.jsonl"


def transport() -> httpx.MockTransport:
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


def main() -> None:
    rows: list[dict] = []
    with httpx.Client(
        transport=transport(),
        headers={"User-Agent": USER_AGENT},
    ) as client:
        for row in harvest_envelope_rows("http://example.test/oai", http_client=client):
            rows.append(row)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        "\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {OUT} ({len(rows)} rows); set stable retrieved_at in the file before committing.")


if __name__ == "__main__":
    main()
