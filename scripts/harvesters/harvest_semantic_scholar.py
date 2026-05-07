#!/usr/bin/env python3
"""
Harvest bridge candidates from Semantic Scholar for cross-domain bridge discovery.

Usage:
    python scripts/harvesters/harvest_semantic_scholar.py --query "information theory neuroscience" --top 20
    python scripts/harvesters/harvest_semantic_scholar.py --bridge-scan --output drafts/semantic_scholar_candidates.json
"""
import argparse, json, time, urllib.request, urllib.parse
from datetime import date
from pathlib import Path

BASE = "https://api.semanticscholar.org/graph/v1"
FIELDS = "title,abstract,year,citationCount,externalIds,fieldsOfStudy,s2FieldsOfStudy"

BRIDGE_QUERIES = [
    ("renormalization group machine learning", "physics-ML"),
    ("optimal transport cell differentiation", "mathematics-biology"),
    ("statistical mechanics social networks", "physics-social"),
    ("information geometry evolution", "mathematics-biology"),
    ("topological data analysis neuroscience", "mathematics-neuroscience"),
    ("game theory microbiome ecology", "mathematics-ecology"),
    ("quantum field theory condensed matter topology", "physics-mathematics"),
    ("network percolation epidemics SIR threshold", "physics-epidemiology"),
    ("fractal dimension urban scaling cities", "mathematics-urban"),
    ("stochastic thermodynamics biological motors", "physics-biology"),
]

def search_papers(query, top=20):
    params = urllib.parse.urlencode({
        "query": query, "limit": top, "fields": FIELDS
    })
    url = f"{BASE}/paper/search?{params}"
    req = urllib.request.Request(url, headers={
        "User-Agent": "USDR/1.0 (https://github.com/KR8ZYSHO3/Universal-Science-Discovery)"
    })
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read())
            return data.get("data", [])
    except Exception as e:
        print(f"  S2 search error: {e}")
        return []

def paper_to_candidate(paper, bridge_hint):
    ext_ids = paper.get("externalIds", {})
    return {
        "title": paper.get("title", ""),
        "doi": ext_ids.get("DOI", ""),
        "arxiv": ext_ids.get("ArXiv", ""),
        "year": paper.get("year"),
        "citations": paper.get("citationCount", 0),
        "fields": paper.get("fieldsOfStudy", []),
        "abstract_snippet": (paper.get("abstract") or "")[:400],
        "bridge_hint": bridge_hint,
        "source": "semantic_scholar",
        "harvested": date.today().isoformat(),
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", help="Single query")
    parser.add_argument("--bridge-scan", action="store_true")
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument("--output", default="drafts/semantic_scholar_candidates.json")
    args = parser.parse_args()

    queries = [(args.query, "custom")] if args.query else (BRIDGE_QUERIES if args.bridge_scan else [])
    if not queries:
        parser.print_help(); return

    all_candidates = []
    for query, bridge_hint in queries:
        print(f"\nQuerying Semantic Scholar: {query}")
        papers = search_papers(query, top=args.top)
        time.sleep(1.0)  # S2 rate limit: 1 req/sec unauthenticated
        candidates = [paper_to_candidate(p, bridge_hint) for p in papers]
        print(f"  Found {len(candidates)} papers")
        all_candidates.extend(candidates)

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({
        "generated": date.today().isoformat(),
        "source": "Semantic Scholar",
        "total_candidates": len(all_candidates),
        "candidates": all_candidates
    }, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nWrote {len(all_candidates)} candidates to {out}")

if __name__ == "__main__":
    main()
