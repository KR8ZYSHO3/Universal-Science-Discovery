#!/usr/bin/env python3
"""
Auto-update dashboard/index.html stat counts from actual catalog file counts.

Targets:
  - id="stat-hyp"   — hypotheses count
  - id="stat-unk"   — unknowns count
  - id="stat-bridges" — cross-domain bridges count
  - id="stat-phenom"  — phenomenology entries count
  - pill text "N cross-domain bridges"
  - pill text "N unknowns · N hypotheses · N pre-formal observation"

Run by GitHub Actions after every merge to main.
Usage:
  python scripts/update_dashboard_stats.py           # dry-run (print counts only)
  python scripts/update_dashboard_stats.py --apply   # write changes to dashboard/index.html
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent


def count_files(pattern: str) -> int:
    return len(list(ROOT.glob(pattern)))


def replace_stat_id(html: str, stat_id: str, new_value: int) -> str:
    """Replace the number inside <div ... id="stat-id">NUMBER</div>."""
    pattern = rf'(<div[^>]*\bid="{re.escape(stat_id)}"[^>]*>)\d+(</div>)'
    replacement = rf'\g<1>{new_value}\2'
    result, n = re.subn(pattern, replacement, html)
    if n == 0:
        print(f"  WARNING: stat id '{stat_id}' not found in HTML", file=sys.stderr)
    return result


def replace_pill_bridges(html: str, new_value: int) -> str:
    """Replace 'N cross-domain bridges' in pill text."""
    pattern = r'(\d+) cross-domain bridges'
    result, n = re.subn(pattern, rf'{new_value} cross-domain bridges', html)
    if n == 0:
        print("  WARNING: pill 'cross-domain bridges' not found in HTML", file=sys.stderr)
    return result


def replace_pill_summary(html: str, unknowns: int, hypotheses: int, phenomena: int) -> str:
    """Replace 'N unknowns · N hypotheses · N pre-formal observation' in pill text."""
    # Match the pattern with any Unicode separator between numbers
    pattern = r'\d+ unknowns[^<]*\d+ hypotheses[^<]*\d+ pre-formal observation'
    new_text = f'{unknowns} unknowns \u00b7 {hypotheses} hypotheses \u00b7 {phenomena} pre-formal observation'
    result, n = re.subn(pattern, new_text, html)
    if n == 0:
        print("  WARNING: pill summary line not found in HTML", file=sys.stderr)
    return result


def main() -> None:
    apply = "--apply" in sys.argv

    unknowns = count_files("unknowns-catalog/**/u-*.yaml")
    hypotheses = count_files("hypotheses/**/*.yaml")
    bridges = count_files("cross-domain/**/b-*.yaml")
    phenomena = count_files("phenomenology/**/p-*.yaml")
    total = unknowns + hypotheses + bridges + phenomena

    print(f"Catalog counts:")
    print(f"  unknowns   = {unknowns}")
    print(f"  hypotheses = {hypotheses}")
    print(f"  bridges    = {bridges}")
    print(f"  phenomena  = {phenomena}")
    print(f"  total      = {total}")

    dashboard = ROOT / "dashboard" / "index.html"
    if not dashboard.exists():
        print(f"ERROR: {dashboard} not found", file=sys.stderr)
        sys.exit(1)

    html = dashboard.read_text(encoding="utf-8")
    original = html

    html = replace_stat_id(html, "stat-unk", unknowns)
    html = replace_stat_id(html, "stat-hyp", hypotheses)
    html = replace_stat_id(html, "stat-bridges", bridges)
    html = replace_stat_id(html, "stat-phenom", phenomena)
    html = replace_pill_bridges(html, bridges)
    html = replace_pill_summary(html, unknowns, hypotheses, phenomena)

    if html == original:
        print("\nNo changes needed — dashboard is already up to date.")
        return

    if apply:
        dashboard.write_text(html, encoding="utf-8")
        print(f"\nApplied: updated {dashboard}")
    else:
        print("\nDry-run: pass --apply to write changes to dashboard/index.html")


if __name__ == "__main__":
    main()
