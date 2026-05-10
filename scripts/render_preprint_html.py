"""Render docs/preprint/usdr_preprint.md -> docs/preprint/usdr_preprint.html (minimal styling)."""
from __future__ import annotations

import argparse
from pathlib import Path

import markdown


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--apply", action="store_true", help="Write HTML (default is dry-run)")
    args = p.parse_args()
    root = Path(__file__).resolve().parents[1]
    md_path = root / "docs" / "preprint" / "usdr_preprint.md"
    out_path = root / "docs" / "preprint" / "usdr_preprint.html"
    md_text = md_path.read_text(encoding="utf-8")
    body = markdown.markdown(md_text, extensions=["tables", "fenced_code", "toc"])
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Universal Science Discovery Repository — Preprint</title>
  <style>
    body {{ font-family: Georgia, "Times New Roman", serif; max-width: 38rem; margin: 2rem auto;
      padding: 0 1rem; line-height: 1.55; color: #111; }}
    code, pre {{ font-family: ui-monospace, Consolas, monospace; font-size: 0.92em; }}
    table {{ border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem; }}
    th, td {{ border: 1px solid #ccc; padding: 0.35rem 0.5rem; text-align: left; vertical-align: top; }}
    th {{ background: #f5f5f5; }}
    pre {{ background: #f8f8f8; padding: 0.75rem; overflow-x: auto; }}
    @media print {{ body {{ max-width: none; }} }}
  </style>
</head>
<body>
{body}
</body>
</html>
"""
    if args.apply:
        out_path.write_text(doc, encoding="utf-8", newline="\n")
        print(f"Wrote {out_path.relative_to(root)}")
    else:
        print("Dry-run: pass --apply to write", out_path.relative_to(root))


if __name__ == "__main__":
    main()
