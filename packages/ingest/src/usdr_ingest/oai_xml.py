"""Parse OAI-PMH XML (arXiv / oai_dc). Metadata only — no binaries."""

from __future__ import annotations

import xml.etree.ElementTree as ET
from dataclasses import dataclass
from typing import Optional

OAI_URI = "http://www.openarchives.org/OAI/2.0/"
DC_URI = "http://purl.org/dc/elements/1.1/"


class OAIProtocolError(ValueError):
    """Invalid or errored OAI-PMH response."""


def _oai(tag: str) -> str:
    return f"{{{OAI_URI}}}{tag}"


def _find(parent: ET.Element, tag_local: str) -> Optional[ET.Element]:
    return parent.find(_oai(tag_local))


def _findall(parent: ET.Element, tag_local: str) -> list[ET.Element]:
    return parent.findall(_oai(tag_local))


def _extract_text(elem: Optional[ET.Element]) -> Optional[str]:
    if elem is None or elem.text is None:
        return None
    t = elem.text.strip()
    return t or None


@dataclass(frozen=True)
class OAIHeader:
    identifier: str
    datestamp: str


@dataclass(frozen=True)
class ParsedRecord:
    header: OAIHeader
    title: Optional[str]
    abstract: Optional[str]
    creators: list[str]
    dates: list[str]
    subjects: list[str]


def _ensure_pmh(xml_bytes: bytes) -> ET.Element:
    root = ET.fromstring(xml_bytes)
    if root.tag != _oai("OAI-PMH"):
        raise OAIProtocolError("Expected OAI-PMH root element")
    return root


def _raise_if_error(root: ET.Element) -> None:
    err = _find(root, "error")
    if err is None:
        return
    code = err.attrib.get("code", "unknown")
    msg = (_extract_text(err) or "").strip()
    raise OAIProtocolError(f"OAI error {code}: {msg}")


def parse_resumption_token(list_element: ET.Element) -> Optional[str]:
    """Return resumption token string, or None if absent or empty (finished)."""
    el = _find(list_element, "resumptionToken")
    if el is None:
        return None
    if el.text is None:
        return None
    token = el.text.strip()
    return token or None


def parse_list_identifiers(xml_bytes: bytes) -> tuple[list[OAIHeader], Optional[str]]:
    root = _ensure_pmh(xml_bytes)
    _raise_if_error(root)
    li = _find(root, "ListIdentifiers")
    if li is None:
        raise OAIProtocolError("Missing ListIdentifiers")
    headers: list[OAIHeader] = []
    for h in _findall(li, "header"):
        if h.attrib.get("status") == "deleted":
            continue
        id_el = _find(h, "identifier")
        ds_el = _find(h, "datestamp")
        sid = _extract_text(id_el)
        ds = _extract_text(ds_el)
        if not sid or not ds:
            continue
        headers.append(OAIHeader(identifier=sid, datestamp=ds))
    token = parse_resumption_token(li)
    return headers, token


def _parse_dc_metadata(metadata_el: ET.Element) -> tuple[
    Optional[str],
    Optional[str],
    list[str],
    list[str],
    list[str],
]:
    titles: list[str] = []
    descriptions: list[str] = []
    creators: list[str] = []
    dates: list[str] = []
    subjects: list[str] = []

    for child in metadata_el.iter():
        if child.tag.startswith("{"):
            uri, local = child.tag[1:].split("}", 1)
        else:
            uri, local = "", child.tag
        if uri != DC_URI:
            continue
        txt = (child.text or "").strip()
        if not txt:
            continue
        if local == "title":
            titles.append(txt)
        elif local == "description":
            descriptions.append(txt)
        elif local == "creator":
            creators.append(txt)
        elif local == "date":
            dates.append(txt)
        elif local == "subject":
            subjects.append(txt)

    title = "; ".join(titles) if titles else None
    abstract = descriptions[0] if descriptions else None
    return title, abstract, creators, dates, subjects


def parse_get_record(xml_bytes: bytes) -> Optional[ParsedRecord]:
    root = _ensure_pmh(xml_bytes)
    _raise_if_error(root)
    gr = _find(root, "GetRecord")
    if gr is None:
        raise OAIProtocolError("Missing GetRecord")
    rec = _find(gr, "record")
    if rec is None:
        raise OAIProtocolError("Missing record")

    hdr = _find(rec, "header")
    if hdr is None:
        raise OAIProtocolError("Missing header")
    if hdr.attrib.get("status") == "deleted":
        return None

    id_el = _find(hdr, "identifier")
    ds_el = _find(hdr, "datestamp")
    sid = _extract_text(id_el)
    ds = _extract_text(ds_el)
    if not sid or not ds:
        raise OAIProtocolError("Incomplete header identifier/datestamp")

    meta = _find(rec, "metadata")
    if meta is None:
        raise OAIProtocolError("Missing metadata")

    title, abstract, creators, dates, subjects = _parse_dc_metadata(meta)
    return ParsedRecord(
        header=OAIHeader(identifier=sid, datestamp=ds),
        title=title,
        abstract=abstract,
        creators=creators,
        dates=dates,
        subjects=subjects,
    )
