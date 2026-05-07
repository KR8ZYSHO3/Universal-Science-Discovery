#!/usr/bin/env python3
"""Write all Wave 57 and Wave 58 YAML files to the repository."""
from pathlib import Path
import importlib.util
import sys

ROOT = Path(__file__).resolve().parents[1]


def load_files_dict(script_path: Path) -> dict:
    spec = importlib.util.spec_from_file_location("mod", script_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.FILES


def write_files(files: dict, wave_name: str) -> int:
    written = 0
    for rel_path, content in files.items():
        target = ROOT / rel_path
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            print(f"  [SKIP existing] {rel_path}")
            continue
        target.write_text(content, encoding="utf-8")
        print(f"  [WROTE] {rel_path}")
        written += 1
    return written


if __name__ == "__main__":
    scripts = ROOT / "scripts"

    print("=== Wave 57 ===")
    w57 = load_files_dict(scripts / "gen_wave57.py")
    n57 = write_files(w57, "Wave 57")
    print(f"Wave 57: {n57} files written.\n")

    print("=== Wave 58 ===")
    w58 = load_files_dict(scripts / "gen_wave58.py")
    n58 = write_files(w58, "Wave 58")
    print(f"Wave 58: {n58} files written.\n")

    print(f"Total new files: {n57 + n58}")
