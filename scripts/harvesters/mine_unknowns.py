#!/usr/bin/env python3
"""Mine *stated* research gaps from harvest JSON. Stage unknowns only.

This is how unsolvables grow. Bridges stay in Wave Factory and still need a human.

A hit is a paper whose title/abstract uses ignorance language
(remains unknown, open problem, poorly understood, …), not “any highly cited paper.”

Usage:
  python scripts/harvesters/mine_unknowns.py
  python scripts/harvesters/mine_unknowns.py --top 15 --output drafts/unknowns_harvest
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import date, datetime
from pathlib import Path
from typing import Any, Iterable

import yaml

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SOURCES = (
    "drafts/openalex_candidates.json",
    "drafts/pubmed_candidates.json",
    "drafts/semantic_scholar_candidates.json",
)
GAP_RE = re.compile(
    r"("
    r"remains? unknown|still unknown|poorly understood|not well understood|"
    r"little is known|open problem|open question|unsolved|"
    r"unresolved (question|problem)|mechanism is unclear|remains unclear|"
    r"not known whether|gap in (our )?knowledge|outstanding problem|"
    r"major challenge remains|elusive"
    r")",
    re.IGNORECASE,
)


def slugify(text: str, max_len: int = 48) -> str:
    text = (text or "").lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-{2,}", "-", text).strip("-")
    return (text[:max_len] if text else "gap").strip("-")


def load_candidates(paths: Iterable[str]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for rel in paths:
        path = ROOT / rel
        if not path.is_file():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        rows = data.get("candidates") if isinstance(data, dict) else data
        if isinstance(rows, list):
            out.extend(r for r in rows if isinstance(r, dict))
    return out


def blob(c: dict[str, Any]) -> str:
    parts = [
        str(c.get("title") or ""),
        str(c.get("abstract_snippet") or c.get("abstract") or ""),
    ]
    return " ".join(parts)


def existing_index() -> tuple[set[str], set[str]]:
    titles: set[str] = set()
    dois: set[str] = set()
    for path in (ROOT / "unknowns-catalog").rglob("u-*.yaml"):
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        t = re.sub(r"\s+", " ", str(data.get("title") or "").lower()).strip()
        if t:
            titles.add(t)
        for ref in data.get("references") or []:
            if isinstance(ref, dict) and ref.get("doi"):
                dois.add(str(ref["doi"]).lower().strip())
    return titles, dois


def unknown_id(title: str, doi: str) -> str:
    key = (doi or title).encode("utf-8")
    tail = hashlib.sha256(key).hexdigest()[:8]
    return f"u-gap-{slugify(title, 40)}-{tail}"


def build_unknown(c: dict[str, Any], match: str) -> dict[str, Any]:
    title = str(c.get("title") or "Untitled gap").strip()
    doi = str(c.get("doi") or "").strip()
    concepts = c.get("concepts") or []
    disc = [str(x) for x in concepts[:3] if x]
    if not disc:
        hint = str(c.get("bridge_hint") or "")
        disc = [p.strip() for p in hint.replace("↔", ",").split(",") if p.strip()][:2]
    if not disc:
        disc = ["unspecified"]
    folder = slugify(disc[0], 32)
    snippet = str(c.get("abstract_snippet") or c.get("abstract") or "")[:400]
    rec: dict[str, Any] = {
        "id": unknown_id(title, doi),
        "title": title if len(title) >= 8 else f"Open gap: {title}",
        "status": "open",
        "priority": "medium",
        "disciplines": disc,
        "summary": (
            f"HARVESTED gap language ({match!r}) in '{title}'. "
            "Treat as a stated unsolvable until a human confirms it is still open. "
            f"Snippet: {snippet}"
        ),
        "systematic_gaps": [
            "Harvested from title/abstract phrasing; not yet expert-curated.",
            "Confirm the gap is still open and not already solved under another name.",
        ],
        "related_bridges": [],
        "last_reviewed": date.today().isoformat(),
        "_folder": folder,
    }
    if doi:
        rec["references"] = [
            {
                "doi": doi,
                "note": f"Harvested {c.get('source') or 'literature'}; year={c.get('year')}",
            }
        ]
    return rec


def mine(candidates: list[dict[str, Any]], top: int) -> list[dict[str, Any]]:
    titles, dois = existing_index()
    seen_doi: set[str] = set()
    seen_title: set[str] = set()
    hits: list[dict[str, Any]] = []
    for c in candidates:
        text = blob(c)
        m = GAP_RE.search(text)
        if not m:
            continue
        doi = str(c.get("doi") or "").lower().strip()
        tnorm = re.sub(r"\s+", " ", str(c.get("title") or "").lower()).strip()
        if doi and (doi in dois or doi in seen_doi):
            continue
        if tnorm and (tnorm in titles or tnorm in seen_title):
            continue
        rec = build_unknown(c, m.group(1))
        if rec["id"] in {h["id"] for h in hits}:
            continue
        hits.append(rec)
        if doi:
            seen_doi.add(doi)
        if tnorm:
            seen_title.add(tnorm)
        if len(hits) >= top:
            break
    return hits


def write_yaml(path: Path, data: dict[str, Any]) -> None:
    payload = {k: v for k, v in data.items() if not k.startswith("_")}
    path.parent.mkdir(parents=True, exist_ok=True)
    dumped = yaml.safe_dump(payload, sort_keys=False, allow_unicode=True)
    dumped = re.sub(
        r"(?m)^last_reviewed: (\d{4}-\d{2}-\d{2})\s*$",
        r'last_reviewed: "\1"',
        dumped,
    )
    path.write_text(dumped, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--top", type=int, default=15)
    p.add_argument("--output", default="drafts/unknowns_harvest")
    p.add_argument("--dry-run", action="store_true")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    candidates = load_candidates(DEFAULT_SOURCES)
    hits = mine(candidates, args.top)
    print(f"[mine-unknowns] scanned={len(candidates)} gap-hits={len(hits)} (deduped)")
    out = ROOT / args.output
    for rec in hits:
        folder = rec.get("_folder") or "harvested"
        dest = out / folder / f"{rec['id']}.yaml"
        print(f"  {rec['id']}  {rec['title'][:70]}")
        if not args.dry_run:
            write_yaml(dest, rec)
    if not args.dry_run:
        print(f"[mine-unknowns] staged under {out.relative_to(ROOT)}")
        print("Promote unknowns only: python scripts/harvesters/promote_unknowns.py --apply")
        print("Do not promote bridges from this path.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
