#!/usr/bin/env python3
"""
Generate bridge YAML stubs from harvested candidates (OpenAlex, PubMed, etc.).

Reads a candidates JSON file, filters by citation count, and writes
partially-filled bridge YAML stubs to drafts/bridges/ for human expert review.

Usage:
    python scripts/harvesters/generate_bridge_stubs.py \
        --input drafts/openalex_candidates.json \
        --output drafts/bridges/ \
        --top 10 \
        --min-citations 500
"""
import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent


def slugify(text):
    """Convert text to a valid YAML slug."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    text = re.sub(r'^-+|-+$', '', text)
    return text[:60]


def parse_domains_from_hint(bridge_hint):
    """Extract domain pair from bridge_hint like 'Information Theory ↔ Neuroscience'."""
    if '↔' in bridge_hint:
        parts = bridge_hint.split('↔')
        return [slugify(p.strip()).replace('-', '_') for p in parts[:2]]
    return ['domain-a', 'domain-b']


def candidate_to_stub(candidate, rank):
    """Generate a bridge YAML stub from a candidate."""
    hint = candidate.get('bridge_hint', 'Unknown ↔ Unknown')
    domains = parse_domains_from_hint(hint)
    title = candidate.get('title', '')
    doi = candidate.get('doi', '') or candidate.get('arxiv', '')
    year = candidate.get('year', '')
    citations = candidate.get('cited_by', candidate.get('citations', 0))
    abstract = candidate.get('abstract_snippet', '')

    # Generate slug from hint
    slug_parts = hint.replace('↔', 'x').replace('/', '-')
    slug = 'openalex-' + slugify(slug_parts)

    domain_a = domains[0] if len(domains) > 0 else 'domain-a'
    domain_b = domains[1] if len(domains) > 1 else 'domain-b'

    stub = f"""# DRAFT BRIDGE STUB — generated from {candidate.get('source', 'harvest')}
# Source paper: {title[:100]}
# Citations: {citations} | Year: {year} | DOI: {doi}
# REVIEW REQUIRED: fill in all FILL_IN fields before promoting to cross-domain/
id: b-{slug}
title: "{hint} — [FILL_IN: specific mechanism]"
domains: [{domain_a}, {domain_b}]
bridge_claim: "FILL_IN: one sentence stating the mathematical correspondence between {hint.split('↔')[0].strip()} and {hint.split('↔')[-1].strip()}"
translation_table:
  - source: "FILL_IN: key concept in {hint.split('↔')[0].strip()}"
    target: "FILL_IN: corresponding concept in {hint.split('↔')[-1].strip()}"
    notes: "FILL_IN: why these are mathematically the same"
  - source: "FILL_IN: second concept"
    target: "FILL_IN: second corresponding concept"
    notes: "FILL_IN: mathematical correspondence"
status: proposed
confidence: 0.6
communication_gap: "FILL_IN: why have these fields not already converged?"
cross_pollination_opportunities:
  - "FILL_IN: specific research opportunity enabled by this bridge"
  - "FILL_IN: second opportunity"
references:
  - doi: "{doi}"
    note: "Source paper ({citations} citations, {year}) — {title[:80]}"
  - doi: "FILL_IN: second reference DOI"
    note: "FILL_IN: what this second paper shows"
related_unknowns:
  - u-FILL_IN
last_reviewed: "{date.today().isoformat()}"
# Abstract snippet: {abstract[:200]}
"""
    return slug, stub


def main():
    parser = argparse.ArgumentParser(description='Generate bridge stubs from harvest candidates')
    parser.add_argument('--input', required=True, help='Input candidates JSON file')
    parser.add_argument('--output', default='drafts/bridges/', help='Output directory for stubs')
    parser.add_argument('--top', type=int, default=10, help='Max stubs to generate')
    parser.add_argument('--min-citations', type=int, default=0, help='Minimum citation count')
    parser.add_argument('--source', default=None, help='Filter by source (openalex, pubmed, etc.)')
    args = parser.parse_args()

    input_file = ROOT / args.input
    if not input_file.exists():
        print(f"Error: {input_file} not found", file=sys.stderr)
        sys.exit(1)

    data = json.loads(input_file.read_text(encoding='utf-8'))
    candidates = data.get('candidates', [])

    # Filter
    if args.source:
        candidates = [c for c in candidates if c.get('source') == args.source]
    if args.min_citations > 0:
        candidates = [c for c in candidates
                      if (c.get('cited_by', 0) or c.get('citations', 0)) >= args.min_citations]

    # Sort by citations descending
    candidates.sort(key=lambda c: c.get('cited_by', c.get('citations', 0)), reverse=True)
    candidates = candidates[:args.top]

    out_dir = ROOT / args.output
    out_dir.mkdir(parents=True, exist_ok=True)

    # Check existing bridges to avoid duplicate slugs
    existing_bridges = set()
    bridge_dir = ROOT / 'cross-domain'
    if bridge_dir.exists():
        existing_bridges = {f.stem for f in bridge_dir.rglob('b-*.yaml')}

    generated = 0
    for i, candidate in enumerate(candidates):
        slug, stub = candidate_to_stub(candidate, i + 1)
        if f'b-{slug}' in existing_bridges:
            print(f"  Skipping b-{slug} — already in cross-domain/")
            continue

        out_file = out_dir / f'b-{slug}.yaml'
        if out_file.exists():
            print(f"  Skipping {out_file.name} — already exists in drafts/")
            continue

        out_file.write_text(stub, encoding='utf-8')
        citations = candidate.get('cited_by', candidate.get('citations', 0))
        print(f"  Generated: {out_file.name} ({citations} citations)")
        generated += 1

    print(f"\nGenerated {generated} bridge stubs in {out_dir}")
    print("Next: review and fill in FILL_IN fields, then move to cross-domain/<dir>/")


if __name__ == '__main__':
    main()
