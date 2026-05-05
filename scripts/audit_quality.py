#!/usr/bin/env python3
"""
USDR Quality Auditor — flags low-quality catalog entries for human review.

Quality criteria:
  - Title length >= 20 chars (too short = vague)
  - Title is a question (ends with "?")
  - Not a near-duplicate of another entry (normalised title match)
  - Has systematic_gaps or suggested_hypotheses (preferred)

Usage:
    python scripts/audit_quality.py [--report REPORT_PATH]
"""
import re
import argparse
from pathlib import Path

try:
    import yaml
except ImportError:
    raise SystemExit(
        "PyYAML is required: pip install pyyaml  "
        "(or activate the repo venv first)"
    )

ROOT = Path(__file__).parent.parent


def load_yaml(p: Path) -> dict:
    return yaml.safe_load(p.read_text(encoding="utf-8")) or {}


def audit_unknowns() -> list[dict]:
    issues: list[dict] = []
    titles_seen: dict[str, str] = {}

    for path in sorted((ROOT / "unknowns-catalog").rglob("u-*.yaml")):
        try:
            entry = load_yaml(path)
        except Exception as exc:
            issues.append({
                "file": str(path.relative_to(ROOT)),
                "severity": "ERROR",
                "issue": f"YAML parse error: {exc}",
            })
            continue

        eid = entry.get("id", "")
        title: str = entry.get("title", "")
        rel = str(path.relative_to(ROOT))

        if len(title) < 20:
            issues.append({
                "file": rel, "id": eid, "severity": "WARN",
                "issue": f"Title too short ({len(title)} chars): '{title}'",
            })

        if title and not title.strip().endswith("?"):
            issues.append({
                "file": rel, "id": eid, "severity": "INFO",
                "issue": f"Title is not a question: '{title[:80]}…'" if len(title) > 80 else f"Title is not a question: '{title}'",
            })

        title_norm = re.sub(r"\W+", " ", title.lower()).strip()
        if title_norm in titles_seen:
            issues.append({
                "file": rel, "id": eid, "severity": "WARN",
                "issue": f"Possible duplicate of {titles_seen[title_norm]}: '{title[:60]}…'",
            })
        else:
            titles_seen[title_norm] = rel

        if not entry.get("systematic_gaps") and not entry.get("suggested_hypotheses"):
            issues.append({
                "file": rel, "id": eid, "severity": "INFO",
                "issue": "Missing both systematic_gaps and suggested_hypotheses",
            })

    return issues


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", default="docs/quality_report.md",
                        help="Output Markdown report path (relative to repo root)")
    args = parser.parse_args()

    print("Auditing unknowns catalog…")
    issues = audit_unknowns()

    errors = [i for i in issues if i["severity"] == "ERROR"]
    warns  = [i for i in issues if i["severity"] == "WARN"]
    infos  = [i for i in issues if i["severity"] == "INFO"]

    print(f"\nQuality Audit Results:")
    print(f"  ERRORS:   {len(errors)}")
    print(f"  WARNINGS: {len(warns)}")
    print(f"  INFO:     {len(infos)}")

    report_lines = [
        "# USDR Quality Audit Report\n\n",
        f"**Errors:** {len(errors)} | **Warnings:** {len(warns)} | **Info:** {len(infos)}\n\n",
        "## Errors\n\n",
    ]
    if errors:
        for i in errors:
            report_lines.append(f"- `{i['file']}`: {i['issue']}\n")
    else:
        report_lines.append("_No errors found._\n")

    report_lines.append("\n## Warnings\n\n")
    if warns:
        for i in warns[:50]:
            report_lines.append(
                f"- `{i.get('file','?')}` ({i.get('id','')}): {i['issue']}\n"
            )
        if len(warns) > 50:
            report_lines.append(f"\n_… and {len(warns)-50} more warnings (capped at 50)._\n")
    else:
        report_lines.append("_No warnings found._\n")

    report_lines.append("\n## Info\n\n")
    if infos:
        for i in infos[:30]:
            report_lines.append(
                f"- `{i.get('file','?')}` ({i.get('id','')}): {i['issue']}\n"
            )
        if len(infos) > 30:
            report_lines.append(f"\n_… and {len(infos)-30} more info items (capped at 30)._\n")
    else:
        report_lines.append("_No info items._\n")

    report_path = ROOT / args.report
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("".join(report_lines), encoding="utf-8")
    print(f"\nReport written to {report_path}")


if __name__ == "__main__":
    main()
