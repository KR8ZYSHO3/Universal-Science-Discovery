#!/usr/bin/env python3
"""Ship a night-crew mailbox PR — harvest JSON + briefing only.

The video-style loop *opens and merges* PRs. In this repo that is allowed only
for operations files. Catalog science (bridges, unknowns, hypotheses, repro
RESULT gates) is never auto-merged.

Usage:
  python scripts/crew_ship.py --pr 314
  python scripts/crew_ship.py --paths-from-stdin   # one path per line (tests)
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from typing import Iterable, List, Sequence, Tuple

ALLOW_EXACT = frozenset(
    {
        "drafts/openalex_candidates.json",
        "drafts/pubmed_candidates.json",
        "drafts/semantic_scholar_candidates.json",
        "drafts/crew-reports/LATEST.md",
        "drafts/crew-reports/README.md",
    }
)
ALLOW_PREFIXES = ("drafts/crew-reports/",)
FORBIDDEN_PREFIXES = (
    "cross-domain/",
    "unknowns-catalog/",
    "hypotheses/",
    "protocols-catalog/",
    "repro/",
    "schemas/",
    "phenomenology/",
    "breakthrough-gaps/",
    "pioneers/",
)


def shippable(paths: Iterable[str]) -> Tuple[bool, str]:
    cleaned = [p.replace("\\", "/").lstrip("/") for p in paths if p.strip()]
    if not cleaned:
        return False, "no files on the PR"
    for p in cleaned:
        if any(p == f or p.startswith(f) for f in FORBIDDEN_PREFIXES):
            return False, f"refusing science path: {p}"
        allowed = p in ALLOW_EXACT or any(p.startswith(pref) for pref in ALLOW_PREFIXES)
        if not allowed:
            return False, f"not on ship allowlist: {p}"
    return True, "allowlist only (mailbox)"


def gh_pr_files(pr: int) -> List[str]:
    proc = subprocess.run(
        ["gh", "pr", "view", str(pr), "--json", "files,url,title"],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        raise SystemExit(f"gh pr view failed: {proc.stderr or proc.stdout}")
    data = json.loads(proc.stdout or "{}")
    files = data.get("files") or []
    return [str(f.get("path") or "") for f in files]


def merge_pr(pr: int) -> int:
    # --auto: merge when required checks pass. Mailbox commits should not skip CI
    # if main requires status checks, or the PR will sit forever.
    proc = subprocess.run(
        [
            "gh",
            "pr",
            "merge",
            str(pr),
            "--squash",
            "--auto",
            "--subject",
            "bot: night crew mailbox (harvest JSON + briefing)",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    sys.stdout.write(proc.stdout or "")
    sys.stderr.write(proc.stderr or "")
    if proc.returncode != 0:
        print(
            "[crew-ship] merge not completed (branch protection or token). "
            "PR stays open — that is still a shipped *request*."
        )
        return 0
    print(f"[crew-ship] auto-merge enabled or completed for PR #{pr}")
    return 0


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Ship allowlisted night-crew PRs only")
    p.add_argument("--pr", type=int, default=0)
    p.add_argument("--paths-from-stdin", action="store_true")
    p.add_argument("--dry-run", action="store_true")
    return p.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    if args.paths_from_stdin:
        paths = [ln.strip() for ln in sys.stdin if ln.strip()]
    elif args.pr:
        paths = gh_pr_files(args.pr)
    else:
        print("pass --pr N or --paths-from-stdin", file=sys.stderr)
        return 2
    ok, reason = shippable(paths)
    print(f"[crew-ship] files={paths}")
    print(f"[crew-ship] shippable={ok} ({reason})")
    if not ok:
        print("[crew-ship] refusing to merge — not a mailbox PR")
        return 1
    if args.dry_run or args.paths_from_stdin:
        return 0
    return merge_pr(args.pr)


if __name__ == "__main__":
    raise SystemExit(main())
