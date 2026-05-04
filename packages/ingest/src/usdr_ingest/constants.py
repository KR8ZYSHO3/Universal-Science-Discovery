"""Shared constants (User-Agent, defaults) — polite, project-identified requests."""

DEFAULT_ARXIV_OAI_BASE = "https://export.arxiv.org/oai"

# Identify the project; metadata-only harvest per LEGAL.md / docs/DATA_PLAN.md
USER_AGENT = (
    "Universal-Science-Discovery-ingest/0.1 "
    "(+https://github.com/KR8ZYSHO3/Universal-Science-Discovery; "
    "OAI-PMH metadata only; no PDFs)"
)

ENVELOPE_VERSION = "1.0.0"
SOURCE_SYSTEM = "arxiv_oai"

# DATA_PLAN + LEGAL traceability
LICENSE_OR_STATUS = "arXiv terms of use — metadata via OAI-PMH (see LEGAL.md)"
LEGAL_NOTE_DEFAULT = "metadata only; no full text or PDFs stored"
