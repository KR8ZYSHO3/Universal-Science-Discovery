"""HTTP client for OAI-PMH with retries and polite headers."""

from __future__ import annotations

import logging
import time
from typing import Any, Mapping, Optional

import httpx

from usdr_ingest.constants import USER_AGENT


log = logging.getLogger(__name__)


class OAIHTTPError(RuntimeError):
    """HTTP/network failure after retries."""


DEFAULT_TIMEOUT_SEC = 60.0


def fetch_oai_xml(
    base_url: str,
    params: Mapping[str, Any],
    *,
    timeout: float = DEFAULT_TIMEOUT_SEC,
    max_retries: int = 5,
    client: Optional[httpx.Client] = None,
) -> bytes:
    """
    GET OAI-PMH with retries (exponential backoff, capped).

    Sends a descriptive User-Agent. Metadata-only callers must not alter this to hide identity.
    """
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/xml,text/xml;q=0.9,*/*;q=0.1",
    }
    owns_client = client is None
    c = client or httpx.Client(
        headers=headers,
        timeout=timeout,
        follow_redirects=True,
    )
    try:
        last_err: Optional[BaseException] = None
        for attempt in range(max_retries):
            try:
                r = c.get(base_url.rstrip("/"), params=dict(params))
                r.raise_for_status()
                return r.content
            except (httpx.HTTPError, httpx.TransportError, OSError) as e:
                last_err = e
                sleep = min(30.0, 0.5 * (2**attempt))
                log.warning(
                    "OAI request failed (attempt %s/%s); sleeping %.1fs: %s",
                    attempt + 1,
                    max_retries,
                    sleep,
                    e,
                )
                if attempt < max_retries - 1:
                    time.sleep(sleep)
        raise OAIHTTPError(f"OAI HTTP failed after {max_retries} attempts") from last_err
    finally:
        if owns_client:
            c.close()
