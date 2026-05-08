#!/usr/bin/env python3
"""
Harvest bridge candidates from PubMed/NCBI for biomedical cross-domain unknowns.

Usage:
    python scripts/harvesters/harvest_pubmed.py --query "Lyme disease neuroinflammation" --top 20
    python scripts/harvesters/harvest_pubmed.py --bridge-scan --output drafts/pubmed_candidates.json
"""
import argparse, json, time, urllib.request, urllib.parse
from datetime import date
from pathlib import Path

ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
EFETCH  = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
ESUM    = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

# Cross-domain queries mapped to USDR bridge areas
BRIDGE_QUERIES = [
    ("Lyme disease neuroinflammation mechanism", "neuroscience-immunology"),
    ("percolation threshold ecological connectivity", "physics-ecology"),
    ("gut microbiome brain axis neurotransmitter", "microbiology-neuroscience"),
    ("cancer immunotherapy checkpoint network", "immunology-oncology"),
    ("CRISPR gene editing therapeutic delivery", "genetics-medicine"),
    ("circadian rhythm metabolic syndrome", "chronobiology-metabolism"),
    ("antibiotic resistance evolution fitness landscape", "pharmacology-evolution"),
    ("neurodegeneration protein aggregation thermodynamics", "neuroscience-physics"),
    ("epigenetic aging clock biomarker", "epigenetics-geroscience"),
    ("psychedelic default mode network depression", "pharmacology-neuroscience"),
]

def esearch(query, db="pubmed", retmax=20):
    params = urllib.parse.urlencode({"db": db, "term": query, "retmax": retmax,
                                      "retmode": "json", "sort": "relevance"})
    req = urllib.request.Request(f"{ESEARCH}?{params}",
                                  headers={"User-Agent": "USDR/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read())
            return data.get("esearchresult", {}).get("idlist", [])
    except Exception as e:
        print(f"  esearch error: {e}")
        return []

def esummary(ids, db="pubmed"):
    if not ids:
        return []
    params = urllib.parse.urlencode({"db": db, "id": ",".join(ids),
                                      "retmode": "json"})
    req = urllib.request.Request(f"{ESUM}?{params}",
                                  headers={"User-Agent": "USDR/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read())
            result = data.get("result", {})
            uids = result.get("uids", [])
            return [result[uid] for uid in uids if uid in result]
    except Exception as e:
        print(f"  esummary error: {e}")
        return []

def paper_to_candidate(paper, bridge_area, query):
    return {
        "title": paper.get("title", ""),
        "pmid": paper.get("uid", ""),
        "doi": next((id_["value"] for id_ in paper.get("articleids", [])
                      if id_.get("idtype") == "doi"), ""),
        "year": paper.get("pubdate", "")[:4],
        "journal": paper.get("source", ""),
        "bridge_hint": bridge_area,
        "query": query,
        "source": "pubmed",
        "harvested": date.today().isoformat(),
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", help="Single PubMed query string")
    parser.add_argument("--bridge-scan", action="store_true")
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument("--output", default="drafts/pubmed_candidates.json")
    args = parser.parse_args()

    queries = []
    if args.query:
        queries = [(args.query, "custom")]
    elif args.bridge_scan:
        queries = BRIDGE_QUERIES
    else:
        parser.print_help(); return

    all_candidates = []
    for query, bridge_area in queries:
        print(f"\nQuerying PubMed: {query}")
        ids = esearch(query, retmax=args.top)
        time.sleep(0.4)
        papers = esummary(ids)
        time.sleep(0.4)
        candidates = [paper_to_candidate(p, bridge_area, query) for p in papers]
        print(f"  Found {len(candidates)} papers")
        all_candidates.extend(candidates)

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({
        "generated": date.today().isoformat(),
        "source": "PubMed/NCBI",
        "total_candidates": len(all_candidates),
        "candidates": all_candidates
    }, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nWrote {len(all_candidates)} candidates to {out}")

if __name__ == "__main__":
    main()
