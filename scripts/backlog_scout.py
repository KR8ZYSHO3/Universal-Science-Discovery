#!/usr/bin/env python3
"""Backlog scout — idle job. Find work, open issues, never promote science.

When the queue is empty, this is how agents "search for things to complete."
Findings become GitHub issues (todo list). Cap per run. Dedup by fingerprint.

Never: --apply promote, catalog YAML edits, RESULT: CONFIRMED invention.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, List, Optional, Sequence

import yaml

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "drafts" / "crew-reports" / "SCOUT.md"
CATALOG = ROOT / "protocols-catalog"
ROADMAP = ROOT / "ROADMAP.md"
MAX_OPEN = 5
MARKER = "usdr-scout:fingerprint="

V13 = (
    ("FLOW-01", "Hub and docs present the three doors", "docs/USE.md"),
    ("WORK-01", "Crosscheck RESULT writes through", "scripts/apply_crosscheck_result.py"),
    ("UI-01", "Hub first-visit audit (counts, links, no broken loads)", None),
    ("ROBUST-01", "One ordered maintainer command list", None),
    ("WORK-02", "Catalog batch = one documented local run", "docs/DEV_DASHBOARD.md"),
)


@dataclass
class Finding:
    kind: str
    title: str
    body: str
    severity: str = "normal"
    fingerprint: str = field(init=False)

    def __post_init__(self) -> None:
        raw = f"{self.kind}|{self.title}".encode("utf-8")
        self.fingerprint = hashlib.sha256(raw).hexdigest()[:12]


def load_yaml(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return data if isinstance(data, dict) else {}


def scan_v13_gaps() -> List[Finding]:
    out: List[Finding] = []
    text = ROADMAP.read_text(encoding="utf-8") if ROADMAP.is_file() else ""
    for rid, blurb, hint in V13:
        if rid not in text:
            continue
        if hint and (ROOT / hint).is_file():
            continue
        out.append(
            Finding(
                kind="roadmap",
                title=f"{rid} still open — {blurb}",
                body=(
                    f"v1.3 item **{rid}** is on ROADMAP.md and has no shipped hint file "
                    f"(`{hint or 'none'}`).\n\n"
                    f"{blurb}\n\n"
                    "Open a PR that satisfies the success criteria in `.planning/ROADMAP.md`. "
                    "Do not market. Do not auto-confirm science."
                ),
            )
        )
    return out


def scan_protocol_contracts() -> List[Finding]:
    out: List[Finding] = []
    missing_run: List[str] = []
    missing_bundle: List[str] = []
    for path in sorted(CATALOG.rglob("p-b-*.yaml")):
        proto = load_yaml(path)
        pid = str(proto.get("id") or path.stem)
        status = str(proto.get("status") or "")
        bundle = str(proto.get("repro_bundle") or "").strip().rstrip("/")
        if bundle and not (ROOT / bundle).is_dir():
            missing_bundle.append(f"{pid} → `{bundle}`")
        if status in {"executed", "confirmed", "ready"} and not proto.get("last_run_result"):
            missing_run.append(f"{pid} (status={status})")
    if missing_bundle:
        out.append(
            Finding(
                kind="repro-missing",
                title="Protocols point at missing repro bundles",
                body="These `repro_bundle` paths are not directories:\n\n"
                + "\n".join(f"- {m}" for m in missing_bundle[:20]),
                severity="high",
            )
        )
    if missing_run:
        out.append(
            Finding(
                kind="last-run",
                title="Protocols have no last_run_result (hub will not show last run)",
                body=(
                    "WORK-01 write-through is missing on:\n\n"
                    + "\n".join(f"- `{m}`" for m in missing_run)
                    + "\n\nRun the canonical Python, then:\n"
                    "`python scripts/apply_crosscheck_result.py --protocol ID "
                    "--from-stdout run.txt --apply --refresh-hub`\n"
                    "Do not set `status: confirmed` from this bot."
                ),
            )
        )
    js = ROOT / "repro/p-b-habitat-percolation-ecology-fss/simulate_percolation_fss.js"
    if js.is_file():
        txt = js.read_text(encoding="utf-8")
        if 'result: "CONFIRMED"' in txt:
            out.append(
                Finding(
                    kind="honesty",
                    title="Habitat browser demo can emit CONFIRMED (must not)",
                    body=(
                        "`simulate_percolation_fss.js` contains `result: \"CONFIRMED\"`. "
                        "Smoke test must print INCONCLUSIVE only."
                    ),
                    severity="high",
                )
            )
    return out


def scan_orphans() -> List[Finding]:
    graph = ROOT / "docs" / "knowledge_graph.json"
    if not graph.is_file():
        return []
    sys.path.insert(0, str(ROOT / "scripts"))
    from find_orphan_unknowns import analyze_orphan_unknowns  # type: ignore

    data = analyze_orphan_unknowns(graph)
    orphans = data.get("orphans") if isinstance(data.get("orphans"), list) else []
    n = int(data.get("orphan_count") or len(orphans))
    if n <= 0:
        return []
    sample = orphans[:8] if isinstance(orphans, list) else []
    lines = []
    for row in sample:
        if isinstance(row, dict):
            lines.append(f"- `{row.get('id')}`")
    return [
        Finding(
            kind="orphans",
            title=f"{n} orphan unknowns in the knowledge graph",
            body=(
                "Unknowns with no bridge/hypothesis edge. Prime contribution targets, "
                "not auto-generated bridges.\n\n"
                + "\n".join(lines)
                + "\n\n`python scripts/find_orphan_unknowns.py`"
            ),
        )
    ]


def scan_hub_local_targets() -> List[Finding]:
    html = (ROOT / "dashboard" / "index.html").read_text(encoding="utf-8")
    missing: List[str] = []
    for m in re.finditer(
        r"https://kr8zysho3\.github\.io/Universal-Science-Discovery/(repro/[^\"'#\s]+|dashboard/explainers/[^\"'#\s]+)",
        html,
    ):
        rel = m.group(1).rstrip("/")
        local = ROOT / rel
        if rel.endswith(".html") and not local.is_file():
            missing.append(rel)
        elif not rel.endswith(".html") and not local.exists() and not (ROOT / rel / "index.html").is_file():
            missing.append(rel)
    if not missing:
        return []
    uniq = sorted(set(missing))[:15]
    return [
        Finding(
            kind="hub-404",
            title="Hub links to missing local files (will 404 on Pages)",
            body="\n".join(f"- `{u}`" for u in uniq),
            severity="high",
        )
    ]


def collect() -> List[Finding]:
    findings: List[Finding] = []
    findings.extend(scan_v13_gaps())
    findings.extend(scan_protocol_contracts())
    try:
        findings.extend(scan_orphans())
    except Exception as exc:
        findings.append(
            Finding(
                kind="orphans-error",
                title="Orphan scan failed",
                body=str(exc)[:500],
                severity="low",
            )
        )
    findings.extend(scan_hub_local_targets())
    return findings


def render_report(findings: List[Finding], opened: Sequence[str]) -> str:
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Backlog scout",
        "",
        f"Generated **{now}**. Operations only — not a scientific result.",
        "",
        f"Findings: **{len(findings)}**. New issues this run (cap {MAX_OPEN}): {len(opened)}.",
        "",
        "Agents: pick `status:needs-owner` issues first, then this list, then ROADMAP.md.",
        "Do not promote Wave Factory. Do not invent CONFIRMED.",
        "",
    ]
    if not findings:
        lines.append("_Queue empty of scout checks. Still do not invent catalog rows._")
        return "\n".join(lines) + "\n"
    for f in findings:
        lines.append(f"## {f.title}")
        lines.append("")
        lines.append(f"`{MARKER}{f.fingerprint}` · {f.kind} · {f.severity}")
        lines.append("")
        lines.append(f.body)
        lines.append("")
    if opened:
        lines.append("## Opened this run")
        lines.append("")
        for u in opened:
            lines.append(f"- {u}")
        lines.append("")
    return "\n".join(lines)


def existing_fingerprints() -> set[str]:
    proc = subprocess.run(
        [
            "gh",
            "issue",
            "list",
            "--state",
            "open",
            "--limit",
            "100",
            "--json",
            "number,title,body",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        print(f"[scout] gh issue list failed: {proc.stderr[-300:]}", file=sys.stderr)
        return set()
    found: set[str] = set()
    try:
        rows = json.loads(proc.stdout or "[]")
    except json.JSONDecodeError:
        return set()
    for row in rows:
        body = str(row.get("body") or "")
        for m in re.finditer(re.escape(MARKER) + r"([0-9a-f]{12})", body):
            found.add(m.group(1))
    return found


def open_issue(finding: Finding) -> Optional[str]:
    body = (
        f"<!-- {MARKER}{finding.fingerprint} -->\n\n"
        f"{finding.body}\n\n"
        "_Opened by `scripts/backlog_scout.py`. Not a finding. Do not auto-merge catalog YAML._\n"
    )
    proc = subprocess.run(
        [
            "gh",
            "issue",
            "create",
            "--title",
            f"[scout] {finding.title[:80]}",
            "--body",
            body,
            "--label",
            "scout",
            "--label",
            "crew",
            "--label",
            "status:needs-owner",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        print(f"[scout] issue create failed: {proc.stderr[-400:]}", file=sys.stderr)
        return None
    url = (proc.stdout or "").strip()
    print(f"[scout] opened {url}")
    return url or "opened"


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--write", type=Path, default=REPORT)
    p.add_argument("--open-issues", action="store_true")
    p.add_argument("--max-open", type=int, default=MAX_OPEN)
    return p.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    findings = collect()
    opened: List[str] = []
    if args.open_issues:
        known = existing_fingerprints()
        for f in findings:
            if f.fingerprint in known:
                continue
            if len(opened) >= args.max_open:
                break
            url = open_issue(f)
            if url:
                opened.append(url)
    report = render_report(findings, opened)
    path: Path = args.write if args.write.is_absolute() else ROOT / args.write
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(report, encoding="utf-8")
    print(report)
    print(f"[scout] wrote {path.relative_to(ROOT)} findings={len(findings)} opened={len(opened)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
