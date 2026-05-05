#!/usr/bin/env python3
"""
USDR Hypothesis Generator — pattern-based bridge drafting tool.

Analyzes existing bridges to extract mathematical patterns, then applies
those patterns to proposed domain pairs to generate draft bridge YAMLs.

Usage:
    python scripts/generate_hypothesis.py --domain1 neuroscience --domain2 medicine --output drafts/bridges/
    python scripts/generate_hypothesis.py --from-proposals --top 5 --output drafts/bridges/
"""
import yaml
import json
import argparse
from pathlib import Path
from collections import defaultdict, Counter
import re

ROOT = Path(__file__).parent.parent

MATH_PATTERNS = {
    "phase_transition": {
        "keywords": [
            "phase transition", "critical point", "order parameter", "universality",
            "bifurcation", "tipping", "threshold", "percolation", "abrupt", "collapse",
            "attractor", "bifurcation", "critical slowing",
        ],
        "template_bridge_claim": (
            "Both systems exhibit a phase transition at a critical parameter value, "
            "with the same universality class governing the order parameter exponents."
        ),
        "template_translation": [
            {
                "source_concept": "control parameter",
                "target_concept": "analogous control variable",
                "mathematical_object": "bifurcation parameter λ",
            },
            {
                "source_concept": "order parameter",
                "target_concept": "observable quantity",
                "mathematical_object": "P(λ) ~ |λ - λ_c|^β",
            },
            {
                "source_concept": "critical exponents β, ν, γ",
                "target_concept": "scaling laws in target system",
                "mathematical_object": "finite-size scaling F(L^{1/ν}(λ-λ_c))",
            },
        ],
    },
    "information_theory": {
        "keywords": [
            "entropy", "information", "channel capacity", "mutual information",
            "coding", "compression", "uncertainty", "biomarker", "signal", "noise",
            "language", "communication", "encoding", "decoding",
        ],
        "template_bridge_claim": (
            "The target system can be analyzed as an information-processing channel, "
            "with Shannon's capacity theorem setting fundamental limits on the "
            "achievable performance."
        ),
        "template_translation": [
            {
                "source_concept": "channel capacity C",
                "target_concept": "system throughput/accuracy limit",
                "mathematical_object": "C = max_{p(x)} I(X;Y)",
            },
            {
                "source_concept": "entropy H(X)",
                "target_concept": "system uncertainty/diversity",
                "mathematical_object": "H = -Σ p_i log p_i",
            },
            {
                "source_concept": "Landauer erasure cost",
                "target_concept": "irreversible computation cost",
                "mathematical_object": "ΔF ≥ k_B T ln 2 per bit erased",
            },
        ],
    },
    "network_graph": {
        "keywords": [
            "network", "graph", "topology", "connectivity", "hub", "centrality",
            "clustering", "path length", "percolation", "connectome", "folding",
            "microbiome", "axis", "axis-mechanism",
        ],
        "template_bridge_claim": (
            "The structural topology of both systems can be described by the same "
            "graph-theoretic measures, with network properties predicting emergent "
            "system behavior."
        ),
        "template_translation": [
            {
                "source_concept": "degree distribution P(k)",
                "target_concept": "connectivity distribution",
                "mathematical_object": "P(k) ~ k^{-γ} (scale-free) or Poisson (random)",
            },
            {
                "source_concept": "clustering coefficient C",
                "target_concept": "local cohesion measure",
                "mathematical_object": "C = (triangles)/(connected triples)",
            },
            {
                "source_concept": "characteristic path length L",
                "target_concept": "functional distance",
                "mathematical_object": "L = mean shortest path",
            },
        ],
    },
    "scaling_law": {
        "keywords": [
            "scaling", "power law", "allometric", "fractal", "self-similar",
            "Zipf", "Pareto", "log-normal", "gradient", "inequality",
            "baryon", "asymmetry",
        ],
        "template_bridge_claim": (
            "Both systems exhibit power-law scaling with the same exponent, "
            "suggesting a common underlying optimization principle or "
            "renormalization group fixed point."
        ),
        "template_translation": [
            {
                "source_concept": "scaling exponent α",
                "target_concept": "analogous exponent",
                "mathematical_object": "Y ~ X^α",
            },
            {
                "source_concept": "fractal dimension D",
                "target_concept": "space-filling efficiency",
                "mathematical_object": "N(r) ~ r^{-D}",
            },
            {
                "source_concept": "RG fixed point",
                "target_concept": "universal behavior class",
                "mathematical_object": "β(g*) = 0",
            },
        ],
    },
    "optimization": {
        "keywords": [
            "optimal", "minimum", "maximum", "variational", "Lagrangian",
            "Hamiltonian", "cost function", "efficiency", "policy", "equilibrium",
            "prediction", "employment", "behavioral", "cognitive",
        ],
        "template_bridge_claim": (
            "Both systems implement the same optimization principle — minimizing a "
            "common cost functional — producing structurally identical solutions "
            "despite arising in different physical contexts."
        ),
        "template_translation": [
            {
                "source_concept": "cost functional F[φ]",
                "target_concept": "system cost/objective",
                "mathematical_object": "δF/δφ = 0 (variational equation)",
            },
            {
                "source_concept": "Euler-Lagrange equation",
                "target_concept": "governing dynamics",
                "mathematical_object": "d/dt(∂L/∂φ̇) - ∂L/∂φ = 0",
            },
            {
                "source_concept": "global minimum",
                "target_concept": "equilibrium/steady state",
                "mathematical_object": "Nash equilibrium / ESS / metabolic optimum",
            },
        ],
    },
}


def _text_from_unknowns(unknowns: list[str]) -> str:
    return " ".join(u.replace("-", " ") for u in unknowns[:5])


def detect_pattern(domain1: str, domain2: str, unknowns_d1: list, unknowns_d2: list) -> tuple[str, dict]:
    """Detect which mathematical pattern best fits a domain pair."""
    all_text = " ".join([
        domain1.replace("-", " "),
        domain2.replace("-", " "),
        _text_from_unknowns(unknowns_d1),
        _text_from_unknowns(unknowns_d2),
    ]).lower()

    scores: dict[str, int] = {}
    for pattern_name, pattern in MATH_PATTERNS.items():
        scores[pattern_name] = sum(1 for kw in pattern["keywords"] if kw in all_text)

    best = max(scores, key=scores.get)
    return best, MATH_PATTERNS[best]


def generate_bridge_yaml(
    domain1: str,
    domain2: str,
    pattern_name: str,
    pattern: dict,
    unknowns_d1: list,
    unknowns_d2: list,
) -> dict:
    """Generate a draft bridge YAML from a domain pair and detected pattern."""
    slug = f"{domain1}-{domain2}".replace("_", "-").replace(" ", "-").lower()
    bid = f"b-{slug}"

    d1_title = domain1.replace("-", " ").title()
    d2_title = domain2.replace("-", " ").title()
    pattern_title = pattern_name.replace("_", " ").title()

    bridge = {
        "id": bid,
        "title": (
            f"{d1_title} ↔ {d2_title}: {pattern_title} Connection "
            f"[AI DRAFT — REQUIRES EXPERT REVIEW]"
        ),
        "source_domain": domain1,
        "target_domain": domain2,
        "bridge_claim": (
            f"[AI-GENERATED DRAFT] {pattern['template_bridge_claim']} "
            f"Applied to {d1_title} and {d2_title}: the mathematical structure of "
            f"{pattern_name.replace('_', ' ')} appears in both domains, suggesting "
            f"a deep structural correspondence that could enable cross-pollination "
            f"of methods and predictions."
        ),
        "translation_table": [
            {
                "source_concept": f"[{d1_title}] {t['source_concept']}",
                "target_concept": f"[{d2_title}] {t['target_concept']}",
                "mathematical_object": t["mathematical_object"],
            }
            for t in pattern["template_translation"]
        ],
        "evidence": [
            (
                f"[TO VERIFY] Literature search needed for {d1_title} instances "
                f"of {pattern_name.replace('_', ' ')}"
            ),
            (
                f"[TO VERIFY] Literature search needed for {d2_title} instances "
                f"of {pattern_name.replace('_', ' ')}"
            ),
            "[TO ADD] Key papers connecting these domains",
        ],
        "open_unknowns": (unknowns_d1[:2] + unknowns_d2[:2]),
        "related_hypotheses": [],
        "communication_gap": (
            f"Researchers in {d1_title} and {d2_title} rarely collaborate. "
            f"The {pattern_name.replace('_', ' ')} framework is well-developed in "
            f"{d1_title} but largely unknown to {d2_title} practitioners."
        ),
        "cross_pollination_opportunities": [
            f"Apply {d1_title} {pattern_name.replace('_', ' ')} methods to {d2_title} datasets",
            f"Test whether {d2_title} exhibits the same critical exponents as {d1_title}",
            (
                f"Use {d2_title} experimental systems to validate theoretical "
                f"predictions from {d1_title}"
            ),
        ],
        "references": [
            {
                "title": "[TO ADD] Foundational paper in source domain",
                "doi_or_url": "TODO",
            },
            {
                "title": "[TO ADD] Foundational paper in target domain",
                "doi_or_url": "TODO",
            },
        ],
        "last_reviewed": "2026-05-05",
        "_ai_generated": True,
        "_pattern_detected": pattern_name,
        "_novelty_score": len(unknowns_d1) + len(unknowns_d2),
    }
    return bridge


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Pattern-based bridge hypothesis generator for USDR."
    )
    parser.add_argument("--domain1", type=str, default=None, help="First domain slug")
    parser.add_argument("--domain2", type=str, default=None, help="Second domain slug")
    parser.add_argument(
        "--from-proposals",
        action="store_true",
        help="Generate from top entries in docs/bridge_proposals.json",
    )
    parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="Number of top proposals to generate (default: 5)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="drafts/bridges/",
        help="Output directory for generated YAML files",
    )
    args = parser.parse_args()

    proposals_path = ROOT / "docs" / "bridge_proposals.json"
    if not proposals_path.exists():
        raise FileNotFoundError(f"bridge_proposals.json not found at {proposals_path}")

    proposals = json.loads(proposals_path.read_text(encoding="utf-8"))
    candidates = proposals.get("candidates", [])

    if args.from_proposals:
        pairs = [
            (
                c["domain_1"],
                c["domain_2"],
                c.get("sample_unknowns_d1", []),
                c.get("sample_unknowns_d2", []),
            )
            for c in candidates[: args.top]
        ]
    elif args.domain1 and args.domain2:
        pairs = [(args.domain1, args.domain2, [], [])]
    else:
        parser.error("Specify --domain1 and --domain2, or use --from-proposals")
        return

    out_dir = ROOT / args.output
    out_dir.mkdir(parents=True, exist_ok=True)

    generated = []
    for domain1, domain2, unknowns_d1, unknowns_d2 in pairs:
        pattern_name, pattern = detect_pattern(domain1, domain2, unknowns_d1, unknowns_d2)
        bridge = generate_bridge_yaml(
            domain1, domain2, pattern_name, pattern, unknowns_d1, unknowns_d2
        )

        slug = f"{domain1}-{domain2}".replace("_", "-").replace(" ", "-").lower()
        out_path = out_dir / f"b-{slug}.yaml"

        # Strip internal metadata keys before writing
        bridge_clean = {k: v for k, v in bridge.items() if not k.startswith("_")}
        out_path.write_text(
            yaml.dump(bridge_clean, allow_unicode=True, sort_keys=False),
            encoding="utf-8",
        )

        score = bridge["_novelty_score"]
        claim_preview = bridge["bridge_claim"][:100]
        print(f"Generated: {out_path.name}")
        print(f"  Pattern : {pattern_name}  (novelty_score={score})")
        print(f"  Claim   : {claim_preview}...")
        print()
        generated.append((out_path.name, pattern_name, score))

    print(f"\n{len(pairs)} draft bridge(s) written to {out_dir}/")
    print("IMPORTANT: All AI-generated drafts require domain expert review before submission.")

    return generated


if __name__ == "__main__":
    main()
