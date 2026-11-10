#!/usr/bin/env python3
"""Check lexicon/lexicon.json. Exits 1 and lists every problem if any are found."""
import json
import os
import sys

PATH = os.path.join(os.path.dirname(__file__), "..", "lexicon", "lexicon.json")
TOL = 1e-3


def main() -> int:
    with open(PATH, encoding="utf-8") as fh:
        data = json.load(fh)
    errors, seen = [], set()
    for i, e in enumerate(data.get("entries", [])):
        tag = f"entry {i} ({e.get('word', '?')!r})"
        for key in ("word", "lang", "lambda", "delta", "alpha", "mass"):
            if key not in e:
                errors.append(f"{tag}: missing '{key}'")
        if any(k not in e for k in ("lambda", "delta", "alpha", "mass")):
            continue
        parts = (e["lambda"], e["delta"], e["alpha"])
        if min(parts) < 0:
            errors.append(f"{tag}: lambda/delta/alpha must be >= 0")
        if abs(sum(parts) - 1) > TOL:
            errors.append(f"{tag}: lambda+delta+alpha = {sum(parts):.4f}, must be 1")
        if e["mass"] < 0:
            errors.append(f"{tag}: mass must be >= 0")
        if "runlevel" in e and e["runlevel"] not in range(7):
            errors.append(f"{tag}: runlevel must be an integer 0-6")
        ident = (e["word"].lower(), e["lang"])
        if ident in seen:
            errors.append(f"{tag}: duplicate word for language {e['lang']!r}; propose a change via an issue instead")
        seen.add(ident)
    for msg in errors:
        print("ERROR:", msg)
    print(f"{len(data.get('entries', []))} entries checked, {len(errors)} problem(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
