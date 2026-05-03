"""High-level OAI harvest: ListIdentifiers paging + GetRecord per header."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterator, Optional

import httpx

from usdr_ingest.client import DEFAULT_TIMEOUT_SEC, fetch_oai_xml
from usdr_ingest.envelope import build_envelope, utc_now_iso_z
from usdr_ingest.oai_xml import parse_get_record, parse_list_identifiers


@dataclass
class HarvestStats:
    list_requests: int = 0
    get_requests: int = 0
    records_emitted: int = 0
    skipped_deleted: int = 0
    last_resumption_token: Optional[str] = None
    stopped_reason: Optional[str] = None


def _listidentifiers_params(
    *,
    metadata_prefix: str,
    frm: Optional[str],
    until: Optional[str],
    set_spec: Optional[str],
    resumption_token: Optional[str],
) -> dict[str, str]:
    if resumption_token is not None:
        return {"verb": "ListIdentifiers", "resumptionToken": resumption_token}
    p: dict[str, str] = {
        "verb": "ListIdentifiers",
        "metadataPrefix": metadata_prefix,
    }
    if frm:
        p["from"] = frm
    if until:
        p["until"] = until
    if set_spec:
        p["set"] = set_spec
    return p


def harvest_envelope_rows(
    base_url: str,
    *,
    metadata_prefix: str = "oai_dc",
    frm: Optional[str] = None,
    until: Optional[str] = None,
    set_spec: Optional[str] = None,
    max_records: Optional[int] = None,
    timeout: float = DEFAULT_TIMEOUT_SEC,
    max_retries: int = 5,
    http_client: Optional[httpx.Client] = None,
    stats: Optional[HarvestStats] = None,
) -> Iterator[dict[str, Any]]:
    """
    ListIdentifiers over metadataPrefix (paged), then GetRecord each identifier.

    Yields envelope dicts aligned with docs/DATA_PLAN.md v1. Deleted records are skipped.
    """
    st = stats or HarvestStats()
    retrieval_time = utc_now_iso_z()

    token: Optional[str] = None
    while True:
        params = _listidentifiers_params(
            metadata_prefix=metadata_prefix,
            frm=frm,
            until=until,
            set_spec=set_spec,
            resumption_token=token,
        )
        st.list_requests += 1
        xml = fetch_oai_xml(
            base_url,
            params,
            timeout=timeout,
            max_retries=max_retries,
            client=http_client,
        )
        headers_page, next_token = parse_list_identifiers(xml)
        st.last_resumption_token = next_token

        for hdr in headers_page:
            if max_records is not None and st.records_emitted >= max_records:
                st.stopped_reason = "max_records"
                return

            gparams = {
                "verb": "GetRecord",
                "identifier": hdr.identifier,
                "metadataPrefix": metadata_prefix,
            }
            st.get_requests += 1
            gxml = fetch_oai_xml(
                base_url,
                gparams,
                timeout=timeout,
                max_retries=max_retries,
                client=http_client,
            )
            parsed = parse_get_record(gxml)
            if parsed is None:
                st.skipped_deleted += 1
                continue

            cursor = f"{parsed.header.identifier}|{parsed.header.datestamp}"
            row = build_envelope(
                parsed,
                retrieved_at=retrieval_time,
                ingestion_cursor=cursor,
            )
            st.records_emitted += 1
            yield row

            if max_records is not None and st.records_emitted >= max_records:
                st.stopped_reason = "max_records"
                return

        if next_token is None:
            st.stopped_reason = "complete"
            return
        token = next_token
