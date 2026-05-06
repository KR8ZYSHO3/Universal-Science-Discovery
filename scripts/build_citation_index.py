#!/usr/bin/env python3
"""
USDR Citation Index — extracts DOIs and references from all catalog entries.
Identifies which papers are cited across multiple bridges (most influential cross-domain works).

Output:
  docs/citation_index.json  — all citations with bridge/entry cross-references
  docs/citation_index.md    — human-readable citation report
"""
import yaml, json, re
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).parent.parent

def load_yaml(p):
    try:
        return yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    except Exception as exc:
        import sys
        print(f"  WARNING: could not parse {p}: {exc}", file=sys.stderr)
        return {}

def extract_citations(entry_id, entry_type, data):
    """Extract all references from a catalog entry."""
    citations = []
    refs = data.get("references", [])
    if isinstance(refs, list):
        for ref in refs:
            if isinstance(ref, dict):
                doi = ref.get("doi_or_url", "") or ref.get("doi", "") or ""
                title = ref.get("title", "")
                citations.append({
                    "entry_id": entry_id,
                    "entry_type": entry_type,
                    "title": title.strip(),
                    "doi": doi.strip() if doi else "",
                    "raw": str(ref)
                })
            elif isinstance(ref, str):
                citations.append({
                    "entry_id": entry_id,
                    "entry_type": entry_type,
                    "title": ref.strip(),
                    "doi": "",
                    "raw": ref
                })

    # Also check evidence_links in hypotheses
    for link in data.get("evidence_links", []):
        if isinstance(link, dict):
            doi = link.get("doi", "") or link.get("url", "") or ""
            citations.append({
                "entry_id": entry_id,
                "entry_type": entry_type,
                "title": link.get("note", link.get("title", "")),
                "doi": doi.strip() if doi else "",
                "raw": str(link)
            })

    return citations

def normalize_doi(doi_str):
    """Normalize DOI for deduplication."""
    doi = doi_str.strip().lower()
    doi = re.sub(r'^https?://(dx\.)?doi\.org/', '', doi)
    doi = re.sub(r'^doi:', '', doi)
    return doi.strip()

def main():
    all_citations = []

    # Collect from bridges
    for p in sorted((ROOT / "cross-domain").rglob("b-*.yaml")):
        d = load_yaml(p)
        if d:
            cites = extract_citations(d.get("id", p.stem), "bridge", d)
            all_citations.extend(cites)

    # Collect from hypotheses
    for p in sorted((ROOT / "hypotheses").rglob("h-*.yaml")):
        d = load_yaml(p)
        if d:
            cites = extract_citations(d.get("id", p.stem), "hypothesis", d)
            all_citations.extend(cites)

    # Build citation frequency map (by normalized title or DOI)
    citation_map = defaultdict(lambda: {"title": "", "doi": "", "entries": [], "count": 0})

    for cite in all_citations:
        # Use DOI as key if available, else normalize title
        key = normalize_doi(cite["doi"]) if cite["doi"] and len(cite["doi"]) > 5 else ""
        if not key:
            # Use first 50 chars of title as key
            key = re.sub(r'\W+', ' ', cite["title"].lower()).strip()[:50]
        if not key:
            continue

        citation_map[key]["title"] = citation_map[key]["title"] or cite["title"]
        citation_map[key]["doi"] = citation_map[key]["doi"] or cite["doi"]
        if cite["entry_id"] not in citation_map[key]["entries"]:
            citation_map[key]["entries"].append(cite["entry_id"])
        citation_map[key]["count"] = len(citation_map[key]["entries"])

    # Sort by citation count (most cross-referenced first)
    ranked = sorted(citation_map.values(), key=lambda x: -x["count"])

    # Generate JSON output
    from datetime import date
    output = {
        "generated": date.today().isoformat(),
        "total_citations": len(all_citations),
        "unique_references": len(citation_map),
        "cross_domain_papers": [r for r in ranked if r["count"] >= 2],
        "all_references": ranked
    }

    out_json = ROOT / "docs" / "citation_index.json"
    out_json.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Citation index: {len(all_citations)} total citations, {len(citation_map)} unique references")

    # Generate Markdown report
    cross_domain = [r for r in ranked if r["count"] >= 2]

    report = [
        "# USDR Citation Index\n\n",
        f"**{len(all_citations)} total citations · {len(citation_map)} unique references · {len(cross_domain)} cited in 2+ bridges**\n\n",
        "## Most Cross-Domain Papers\n\n",
        "Papers cited across the highest number of different bridges — the most influential cross-domain works in the catalog.\n\n",
        "| Bridges | Title | DOI |\n|---|---|---|\n"
    ]

    for ref in cross_domain[:50]:
        doi_link = f"[DOI]({ref['doi']})" if ref.get("doi") and not ref["doi"].startswith("TODO") else ""
        title = ref["title"][:80] + "..." if len(ref["title"]) > 80 else ref["title"]
        bridges = ", ".join(f"`{e}`" for e in ref["entries"][:5])
        report.append(f"| {ref['count']} | {title} | {doi_link} |\n")

    report.extend([
        "\n## Citation Network\n\n",
        "Papers that appear in multiple bridges act as conceptual hubs — they're the works that *most enable cross-domain thinking*.\n\n",
        "The full citation data is available at [`docs/citation_index.json`](citation_index.json).\n\n",
        "## All Unique References\n\n",
        f"The catalog currently references **{len(citation_map)} unique papers/books**.\n"
    ])

    out_md = ROOT / "docs" / "citation_index.md"
    out_md.write_text("".join(report), encoding="utf-8")

    # Print top 10
    print("\nTop 10 most cross-referenced papers:")
    for r in ranked[:10]:
        title_safe = r['title'][:70].encode('ascii', 'replace').decode('ascii')
        print(f"  [{r['count']}x] {title_safe} — bridges: {', '.join(r['entries'])}")

if __name__ == "__main__":
    main()
