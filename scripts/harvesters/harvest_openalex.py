#!/usr/bin/env python3
"""
Harvest cross-domain bridge candidates from OpenAlex.

Usage:
    python scripts/harvesters/harvest_openalex.py --concept-pair "Percolation theory" "Ecology" --top 20
    python scripts/harvesters/harvest_openalex.py --bridge-scan --output drafts/openalex_candidates.json
"""
import argparse
import json
import time
import urllib.request
import urllib.parse
from datetime import date
from pathlib import Path

BASE = "https://api.openalex.org"
HEADERS = {"User-Agent": "USDR/1.0 (https://github.com/KR8ZYSHO3/Universal-Science-Discovery; mailto:usdr@science.org)"}

# High-priority concept pairs for bridge discovery
BRIDGE_CANDIDATE_PAIRS = [
    ("Percolation theory", "Ecology"),
    ("Information theory", "Evolutionary biology"),
    ("Statistical mechanics", "Finance"),
    ("Network theory", "Epidemiology"),
    ("Topology", "Condensed matter physics"),
    ("Game theory", "Evolutionary biology"),
    ("Thermodynamics", "Information theory"),
    ("Statistical mechanics", "Neuroscience"),
    ("Optimal transport", "Biology"),
    ("Renormalization group", "Machine learning"),
    ("Dynamical systems", "Ecology"),
    ("Stochastic processes", "Cell biology"),
    ("Graph theory", "Immunology"),
    ("Information theory", "Neuroscience"),
    ("Statistical physics", "Social science"),
]

def search_concept(name):
    """Search OpenAlex for a concept by name, return first match ID."""
    url = f"{BASE}/concepts?search={urllib.parse.quote(name)}&per-page=1"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read())
            results = data.get("results", [])
            if results:
                return results[0]["id"], results[0].get("display_name", name)
    except Exception as e:
        print(f"  Warning: concept lookup failed for '{name}': {e}")
    return None, name

def fetch_crossdomain_papers(concept_id_a, concept_id_b, top=20):
    """Fetch papers citing both concept A and concept B."""
    filter_str = f"concepts.id:{concept_id_a}|{concept_id_b}"
    url = f"{BASE}/works?filter={urllib.parse.quote(filter_str)}&sort=cited_by_count:desc&per-page={top}&select=id,title,abstract_inverted_index,doi,publication_year,concepts,cited_by_count,authorships"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read())
            return data.get("results", [])
    except Exception as e:
        print(f"  Warning: paper fetch failed: {e}")
        return []

def reconstruct_abstract(inverted_index):
    """Reconstruct abstract from OpenAlex inverted index format."""
    if not inverted_index:
        return ""
    words = {}
    for word, positions in inverted_index.items():
        for pos in positions:
            words[pos] = word
    return " ".join(words[i] for i in sorted(words.keys()))

def paper_to_candidate(paper, concept_a_name, concept_b_name):
    """Convert OpenAlex paper to a bridge candidate dict."""
    abstract = reconstruct_abstract(paper.get("abstract_inverted_index"))
    doi = paper.get("doi", "")
    if doi:
        doi = doi.replace("https://doi.org/", "")

    concepts = [c.get("display_name", "") for c in paper.get("concepts", [])[:5]]

    return {
        "title": paper.get("title", ""),
        "doi": doi,
        "year": paper.get("publication_year"),
        "cited_by": paper.get("cited_by_count", 0),
        "concepts": concepts,
        "abstract_snippet": abstract[:400] + "..." if len(abstract) > 400 else abstract,
        "bridge_hint": f"{concept_a_name} \u2194 {concept_b_name}",
        "source": "openalex",
        "harvested": date.today().isoformat(),
    }

def main():
    parser = argparse.ArgumentParser(description="Harvest bridge candidates from OpenAlex")
    parser.add_argument("--concept-pair", nargs=2, metavar=("CONCEPT_A", "CONCEPT_B"),
                        help="Specific concept pair to query")
    parser.add_argument("--bridge-scan", action="store_true",
                        help="Scan all predefined bridge candidate pairs")
    parser.add_argument("--top", type=int, default=20, help="Papers per pair")
    parser.add_argument("--output", default="drafts/openalex_candidates.json",
                        help="Output JSON file")
    args = parser.parse_args()

    pairs = []
    if args.concept_pair:
        pairs = [tuple(args.concept_pair)]
    elif args.bridge_scan:
        pairs = BRIDGE_CANDIDATE_PAIRS
    else:
        parser.print_help()
        return

    all_candidates = []

    for concept_a_name, concept_b_name in pairs:
        print(f"\nSearching: {concept_a_name} <-> {concept_b_name}")

        id_a, name_a = search_concept(concept_a_name)
        time.sleep(0.3)
        id_b, name_b = search_concept(concept_b_name)
        time.sleep(0.3)

        if not id_a or not id_b:
            print(f"  Skipping — could not resolve concept IDs")
            continue

        print(f"  Concept A: {name_a} ({id_a})")
        print(f"  Concept B: {name_b} ({id_b})")

        papers = fetch_crossdomain_papers(id_a, id_b, top=args.top)
        time.sleep(0.5)

        candidates = [paper_to_candidate(p, name_a, name_b) for p in papers]
        print(f"  Found {len(candidates)} papers")
        all_candidates.extend(candidates)

    # Sort by citation count
    all_candidates.sort(key=lambda x: x["cited_by"], reverse=True)

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({
        "generated": date.today().isoformat(),
        "source": "OpenAlex",
        "total_candidates": len(all_candidates),
        "candidates": all_candidates
    }, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\nWrote {len(all_candidates)} bridge candidates to {out}")
    print("Next step: review drafts/openalex_candidates.json and promote to cross-domain/ YAMLs")

if __name__ == "__main__":
    main()
