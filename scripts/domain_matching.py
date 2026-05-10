#!/usr/bin/env python3
"""
Shared logic: map bridge/hypothesis discipline tags (schema `fields`, `related_disciplines`)
to `unknowns-catalog/<domain>/` folder names for dashboard domain pages.

Bridges use `fields` (see schemas/bridge.yaml). Older generator code incorrectly looked for
`source_domain` / `target_domain`, which are not required fields — so counts showed 0.

Matching strategy:
  1. Normalize tags (lowercase, underscores → hyphens).
  2. Exact match to catalog domain slug.
  3. Prefix / suffix hyphen boundaries (`evolutionary-biology` → biology; `biology-chemistry` → biology).
  4. Small curated map for tags that do not share a token with the folder name (e.g. biophysics ↔ biology).
"""

from __future__ import annotations

# Field tags that should also count toward given catalog domains (beyond prefix/suffix/exact rules).
# Values are unknowns-catalog folder slugs.
TAG_EXTRA_CATALOG_DOMAINS: dict[str, frozenset[str]] = {
    "biophysics": frozenset({"biology", "physics", "neuroscience", "biophysics"}),
    "machine-learning": frozenset({"computer-science", "mathematics", "statistics", "machine-learning"}),
    "computational-neuroscience": frozenset({"neuroscience", "computer-science"}),
    "computer_science": frozenset({"computer-science", "computing"}),
    "information-theory": frozenset({"computer-science", "mathematics", "information-theory"}),
    "signal-processing": frozenset({"computer-science", "engineering", "signal-processing"}),
    "quantum-computing": frozenset({"computer-science", "quantum-physics", "physics", "quantum-computing"}),
    "statistical-physics": frozenset({"physics", "mathematics", "statistics"}),
    "mathematical-biology": frozenset({"biology", "mathematics"}),
    "systems-biology": frozenset({"biology", "systems-biology"}),
    "fluid-mechanics": frozenset({"physics", "engineering", "fluid-mechanics"}),
    "fluid-dynamics": frozenset({"physics", "engineering", "oceanography"}),
}


def normalize_slug(s: str) -> str:
    return (s or "").strip().lower().replace("_", "-")


def catalog_domain_matches_field_tag(catalog_domain: str, field_tag: str) -> bool:
    """Return True if a bridge/hypothesis discipline tag should count toward this catalog domain page."""
    d = normalize_slug(catalog_domain)
    f = normalize_slug(field_tag)
    if not d or not f:
        return False
    if f == d:
        return True
    if f.startswith(d + "-"):
        return True
    if f.endswith("-" + d):
        return True
    extras = TAG_EXTRA_CATALOG_DOMAINS.get(f)
    if extras and d in extras:
        return True
    return False


def summarize_fields_line(fields: list[str], max_terms: int = 8) -> str:
    """Pretty comma line of bridge `fields` for display on domain pages."""
    parts = []
    for raw in fields or []:
        parts.append(str(raw).replace("-", " ").strip().title())
    if len(parts) > max_terms:
        return ", ".join(parts[:max_terms]) + f" (+{len(parts) - max_terms})"
    return ", ".join(parts) if parts else ""
