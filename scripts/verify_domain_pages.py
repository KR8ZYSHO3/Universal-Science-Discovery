#!/usr/bin/env python3
"""
Sanity-check that domain landing page stats can see bridges (regression for wrong field keys).

Run from repo root:
  python scripts/verify_domain_pages.py
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))

import generate_domain_pages as gdp  # noqa: E402


def main() -> int:
    # Domains with large catalogs; must show non-zero bridges after fields[]-based matching
    for domain, minimum in (("biology", 50), ("physics", 50), ("mathematics", 40), ("computer-science", 25)):
        bridges = gdp.get_domain_bridges(domain)
        n = len(bridges)
        if n < minimum:
            print(f"FAIL: {domain} bridge count {n} < expected minimum {minimum}", file=sys.stderr)
            return 1
        print(f"OK {domain}: {n} bridges")

    print("verify_domain_pages: all checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
