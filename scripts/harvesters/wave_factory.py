#!/usr/bin/env python3
"""
Wave Factory orchestrator for high-throughput bridge draft generation.

This script reads harvested candidate JSON files, ranks candidates, deduplicates
against existing bridge IDs/titles, and stages schema-safe draft triples:
  - bridge stub
  - companion unknown
  - companion hypothesis
"""

from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT = ROOT / "drafts" / "wave_factory"
SOURCE_FILE_MAP = {
    "openalex": ROOT / "drafts" / "openalex_candidates.json",
    "pubmed": ROOT / "drafts" / "pubmed_candidates.json",
    "semantic_scholar": ROOT / "drafts" / "semantic_scholar_candidates.json",
}


@dataclass
class RankedCandidate:
    source_name: str
    raw: dict[str, Any]
    score: float
    citation_score: float
    recency_score: float
    novelty_score: float
    bridge_slug: str
    field_a: str
    field_b: str
    bridge_title_key: str


def slugify(text: str, max_len: int = 72) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-{2,}", "-", text)
    text = text.strip("-")
    return text[:max_len] if text else "unknown"


def parse_domains(bridge_hint: str) -> tuple[str, str]:
    hint = (bridge_hint or "").strip()
    if "↔" in hint:
        left, right = hint.split("↔", 1)
    elif "<->" in hint:
        left, right = hint.split("<->", 1)
    elif "-" in hint:
        parts = [p.strip() for p in hint.split("-") if p.strip()]
        if len(parts) >= 2:
            left, right = parts[0], parts[1]
        else:
            left, right = "cross-domain-a", "cross-domain-b"
    else:
        left, right = "cross-domain-a", "cross-domain-b"
    return slugify(left, max_len=32), slugify(right, max_len=32)


def parse_year(value: Any) -> int | None:
    if value is None:
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        m = re.search(r"\d{4}", value)
        if m:
            return int(m.group(0))
    return None


def citation_count(candidate: dict[str, Any]) -> int:
    for key in ("cited_by", "citations", "citationCount"):
        value = candidate.get(key)
        if isinstance(value, int):
            return max(0, value)
        if isinstance(value, str) and value.isdigit():
            return int(value)
    return 0


def load_candidates(source_names: list[str]) -> list[tuple[str, dict[str, Any]]]:
    loaded: list[tuple[str, dict[str, Any]]] = []
    for source_name in source_names:
        source_file = SOURCE_FILE_MAP[source_name]
        if not source_file.exists():
            print(f"[wave-factory] Skipping missing source file: {source_file.relative_to(ROOT)}")
            continue
        payload = json.loads(source_file.read_text(encoding="utf-8"))
        candidates = payload.get("candidates", [])
        for item in candidates:
            if isinstance(item, dict):
                loaded.append((source_name, item))
    return loaded


def bridge_hint(candidate: dict[str, Any]) -> str:
    return str(candidate.get("bridge_hint") or "cross-domain-a ↔ cross-domain-b")


def bridge_title_key(candidate: dict[str, Any]) -> str:
    hint = bridge_hint(candidate)
    title = str(candidate.get("title") or "").strip().lower()
    return f"{hint.lower()}::{title}"


def build_bridge_slug(source_name: str, candidate: dict[str, Any]) -> str:
    hint_slug = slugify(bridge_hint(candidate), max_len=48)
    title_slug = slugify(str(candidate.get("title") or "untitled"), max_len=28)
    return slugify(f"{source_name}-{hint_slug}-{title_slug}", max_len=70)


def load_existing_bridge_identity() -> tuple[set[str], set[str], Counter[tuple[str, str]]]:
    bridge_ids: set[str] = set()
    bridge_titles: set[str] = set()
    pair_counts: Counter[tuple[str, str]] = Counter()

    for path in (ROOT / "cross-domain").rglob("b-*.yaml"):
        try:
            record = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except Exception:
            continue
        if not isinstance(record, dict):
            continue
        bridge_id = str(record.get("id") or "").strip()
        if bridge_id:
            bridge_ids.add(bridge_id)
        title = str(record.get("title") or "").strip().lower()
        if title:
            bridge_titles.add(title)
        fields = record.get("fields")
        if isinstance(fields, list) and len(fields) >= 2:
            a = slugify(str(fields[0]), max_len=32)
            b = slugify(str(fields[1]), max_len=32)
            pair_counts[tuple(sorted((a, b)))] += 1
    return bridge_ids, bridge_titles, pair_counts


def rank_candidates(
    loaded: list[tuple[str, dict[str, Any]]],
    min_citations: int,
    existing_bridge_ids: set[str],
    existing_bridge_titles: set[str],
    existing_pair_counts: Counter[tuple[str, str]],
) -> list[RankedCandidate]:
    today_year = date.today().year

    prepared: list[tuple[str, dict[str, Any], int, int | None, str, str, str, str]] = []
    for source_name, candidate in loaded:
        cites = citation_count(candidate)
        if cites < min_citations:
            continue
        year = parse_year(candidate.get("year"))
        field_a, field_b = parse_domains(bridge_hint(candidate))
        b_slug = build_bridge_slug(source_name, candidate)
        bridge_id = f"b-{b_slug}"
        title_key = bridge_title_key(candidate)
        raw_title = str(candidate.get("title") or "").strip().lower()
        if bridge_id in existing_bridge_ids or raw_title in existing_bridge_titles:
            continue
        prepared.append((source_name, candidate, cites, year, b_slug, field_a, field_b, title_key))

    if not prepared:
        return []

    max_cites = max(item[2] for item in prepared)
    source_pair_counts = Counter(tuple(sorted((item[5], item[6]))) for item in prepared)

    ranked: list[RankedCandidate] = []
    for source_name, candidate, cites, year, b_slug, field_a, field_b, title_key in prepared:
        c_score = math.log1p(cites) / math.log1p(max_cites) if max_cites > 0 else 0.0
        if year is None:
            r_score = 0.15
        else:
            age = max(0, today_year - year)
            r_score = max(0.0, 1.0 - (age / 25.0))
        pair_key = tuple(sorted((field_a, field_b)))
        historical = existing_pair_counts[pair_key]
        in_batch = max(0, source_pair_counts[pair_key] - 1)
        n_score = 1.0 / (1.0 + historical + (0.25 * in_batch))
        score = (0.55 * c_score) + (0.30 * r_score) + (0.15 * n_score)

        ranked.append(
            RankedCandidate(
                source_name=source_name,
                raw=candidate,
                score=score,
                citation_score=c_score,
                recency_score=r_score,
                novelty_score=n_score,
                bridge_slug=b_slug,
                field_a=field_a,
                field_b=field_b,
                bridge_title_key=title_key,
            )
        )

    ranked.sort(key=lambda x: x.score, reverse=True)
    return ranked


def primary_reference(candidate: dict[str, Any]) -> dict[str, str]:
    reference: dict[str, str] = {}
    doi = str(candidate.get("doi") or "").strip()
    arxiv = str(candidate.get("arxiv") or "").strip()
    if doi:
        reference["doi"] = doi
    elif arxiv:
        reference["arxiv"] = arxiv
    note_parts = []
    if candidate.get("source"):
        note_parts.append(f"source={candidate['source']}")
    if candidate.get("year"):
        note_parts.append(f"year={candidate['year']}")
    if citation_count(candidate):
        note_parts.append(f"citations={citation_count(candidate)}")
    if note_parts:
        reference["note"] = "Harvest metadata: " + ", ".join(note_parts)
    return reference


def build_records(item: RankedCandidate) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    candidate = item.raw
    today = date.today().isoformat()
    bridge_id = f"b-{item.bridge_slug}"
    unknown_id = f"u-{item.bridge_slug}"
    hypothesis_id = f"h-{item.bridge_slug}"
    hint = bridge_hint(candidate)
    paper_title = str(candidate.get("title") or "Untitled candidate")
    speculative = item.score < 0.50
    confidence_tag = "SPECULATIVE" if speculative else "PROVISIONAL"

    bridge = {
        "id": bridge_id,
        "title": f"{hint}: candidate bridge from '{paper_title}' ({confidence_tag})",
        "status": "proposed",
        "fields": [item.field_a, item.field_b],
        "bridge_claim": (
            f"{confidence_tag}: Harvested candidate suggests a cross-domain mapping between "
            f"{item.field_a} and {item.field_b}. Human review is required before treating this as a finding."
        ),
        "translation_table": [
            {
                "field_a_term": f"{item.field_a} core construct",
                "field_b_term": f"{item.field_b} analog construct",
                "note": "Auto-generated placeholder mapping for reviewer completion.",
            }
        ],
        "related_unknowns": [unknown_id],
        "related_hypotheses": [hypothesis_id],
        "cross_pollination_opportunities": [
            "Curate 2-3 direct papers with explicit mathematical mapping statements.",
            "Design a falsification-oriented benchmark shared by both domains.",
        ],
        "communication_gap": (
            "Generated by Wave Factory ranking pipeline; requires domain expert vetting, "
            "citation checks, and translation-table refinement before promotion."
        ),
        "last_reviewed": today,
        "references": [primary_reference(candidate)] if primary_reference(candidate) else [],
    }

    unknown = {
        "id": unknown_id,
        "title": f"Does {hint} hold under reproducible cross-domain tests? ({confidence_tag})",
        "status": "open",
        "priority": "medium" if speculative else "high",
        "disciplines": [item.field_a, item.field_b],
        "summary": (
            f"{confidence_tag}: Candidate derived from harvested literature ('{paper_title}'). "
            "The unknown is whether the proposed bridge survives rigorous comparison and falsification."
        ),
        "systematic_gaps": [
            "No reviewer-verified translation table yet.",
            "No explicit boundary conditions for when the mapping fails.",
            "Independent replication set not curated.",
        ],
        "suggested_hypotheses": [
            (
                f"Under matched modeling assumptions, one quantitative descriptor from {item.field_a} "
                f"improves predictive performance on a benchmark from {item.field_b}."
            )
        ],
        "related_bridges": [bridge_id],
        "references": [primary_reference(candidate)] if primary_reference(candidate) else [],
        "last_reviewed": today,
    }

    hypothesis = {
        "id": hypothesis_id,
        "title": (
            f"{confidence_tag}: A model feature transfer from {item.field_a} to {item.field_b} "
            "outperforms baseline domain-native methods on held-out data."
        ),
        "status": "active",
        "priority": "medium" if speculative else "high",
        "impact_score": round(max(0.2, min(0.95, item.score)), 2),
        "created": today,
        "last_updated": today,
        "author": "USDR Wave Factory",
        "evidence_links": [
            {
                **primary_reference(candidate),
                "type": "related",
                "confidence": round(max(0.05, min(0.95, item.score)), 2),
                "note": (
                    f"{confidence_tag}: Auto-generated from harvested candidate; "
                    "requires source verification and experiment design."
                ),
            }
        ],
        "unknowns_addressed": [unknown_id],
        "proposed_tests": [
            {
                "description": "Assemble benchmark datasets from both disciplines and evaluate transfer mapping.",
                "method": "Compare against domain baselines with preregistered metrics.",
                "prediction": "Mapped model improves benchmark performance by >=5% over baseline.",
            }
        ],
        "related_disciplines": [item.field_a, item.field_b],
    }

    return bridge, unknown, hypothesis


def write_yaml(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump(payload, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )


def resolve_sources(raw_sources: str | None) -> list[str]:
    if not raw_sources:
        return list(SOURCE_FILE_MAP.keys())
    requested = [slugify(token, max_len=64) for token in raw_sources.split(",") if token.strip()]
    valid = [name for name in requested if name in SOURCE_FILE_MAP]
    if not valid:
        raise ValueError(
            "No valid --sources provided. Allowed values: "
            + ", ".join(sorted(SOURCE_FILE_MAP.keys()))
        )
    return valid


def main() -> int:
    parser = argparse.ArgumentParser(description="Wave Factory candidate orchestrator")
    parser.add_argument("--top", type=int, default=12, help="Maximum staged bridge triples")
    parser.add_argument(
        "--min-citations", type=int, default=0, help="Minimum citation threshold for candidates"
    )
    parser.add_argument(
        "--sources",
        default=None,
        help="Comma-separated source list: openalex,pubmed,semantic_scholar",
    )
    parser.add_argument(
        "--output",
        default=str(DEFAULT_OUTPUT.relative_to(ROOT)),
        help="Output staging directory relative to repo root",
    )
    parser.add_argument("--dry-run", action="store_true", help="Compute and print plan only")
    args = parser.parse_args()

    sources = resolve_sources(args.sources)
    output_dir = (ROOT / args.output).resolve()
    loaded = load_candidates(sources)
    if not loaded:
        print("[wave-factory] No candidates loaded from selected sources.")
        return 0

    existing_ids, existing_titles, pair_counts = load_existing_bridge_identity()
    ranked = rank_candidates(
        loaded=loaded,
        min_citations=args.min_citations,
        existing_bridge_ids=existing_ids,
        existing_bridge_titles=existing_titles,
        existing_pair_counts=pair_counts,
    )
    if not ranked:
        print("[wave-factory] No candidates survived filtering and dedupe.")
        return 0

    selected: list[RankedCandidate] = []
    staged_title_keys: set[str] = set()
    staged_ids: set[str] = set()
    for item in ranked:
        bridge_id = f"b-{item.bridge_slug}"
        if item.bridge_title_key in staged_title_keys or bridge_id in staged_ids:
            continue
        selected.append(item)
        staged_title_keys.add(item.bridge_title_key)
        staged_ids.add(bridge_id)
        if len(selected) >= args.top:
            break

    if not selected:
        print("[wave-factory] No unique candidates available after in-batch dedupe.")
        return 0

    print(
        f"[wave-factory] Selected {len(selected)} candidates "
        f"(from {len(loaded)} loaded, {len(ranked)} ranked)."
    )

    writes = 0
    per_source = Counter()
    for idx, item in enumerate(selected, start=1):
        bridge, unknown, hypothesis = build_records(item)
        bridge_path = output_dir / "cross-domain" / f"{item.field_a}-{item.field_b}" / f"{bridge['id']}.yaml"
        unknown_path = output_dir / "unknowns-catalog" / item.field_a / f"{unknown['id']}.yaml"
        hypothesis_path = output_dir / "hypotheses" / "active" / f"{hypothesis['id']}.yaml"
        per_source[item.source_name] += 1

        print(
            f"  [{idx:02d}] {bridge['id']} score={item.score:.3f} "
            f"(c={item.citation_score:.2f}, r={item.recency_score:.2f}, n={item.novelty_score:.2f})"
        )

        if args.dry_run:
            continue

        write_yaml(bridge_path, bridge)
        write_yaml(unknown_path, unknown)
        write_yaml(hypothesis_path, hypothesis)
        writes += 3

    summary = ", ".join(f"{k}={v}" for k, v in sorted(per_source.items()))
    if args.dry_run:
        print(f"[wave-factory] Dry run complete. Source mix: {summary}")
    else:
        print(f"[wave-factory] Wrote {writes} YAML files under {output_dir.relative_to(ROOT)}")
        print(f"[wave-factory] Source mix: {summary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
