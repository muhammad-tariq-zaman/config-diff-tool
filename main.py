"""Diff two config files, ignoring comments and blank lines.

Usage: python3 main.py old.conf new.conf
"""
import argparse
import difflib
import sys


def normalise(text):
    """Return significant lines: stripped, no blanks, no # or ; comments."""
    out = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith(";"):
            continue
        out.append(line)
    return out


def diff_configs(old_text, new_text):
    """Return (added, removed, unified_diff_lines)."""
    old, new = normalise(old_text), normalise(new_text)
    added = [l for l in new if l not in old]
    removed = [l for l in old if l not in new]
    unified = list(difflib.unified_diff(old, new, lineterm=""))
    return added, removed, unified


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("old", help="Old config file")
    parser.add_argument("new", help="New config file")
    args = parser.parse_args(argv)
    with open(args.old, encoding="utf-8") as f:
        old_text = f.read()
    with open(args.new, encoding="utf-8") as f:
        new_text = f.read()
    added, removed, unified = diff_configs(old_text, new_text)
    print(f"Added: {len(added)}, Removed: {len(removed)}")
    for line in unified:
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
