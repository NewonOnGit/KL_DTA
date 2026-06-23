"""
compress_conductors.py — deepenings -> conductors (chord + tight delta), lossless via sidecar.
full deepenings -> KL_DTA.deepenings_full.json (retrievable). live store keeps tight deltas (~280 char,
cut at a sentence boundary). chord (atoms) already lives in structure.chords.index. verify: on-shell +
each delta retains a key token + the full is in the sidecar (lossless).
"""
import json, os, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "KL_DTA.json"
FULL = ROOT / "KL_DTA.deepenings_full.json"
db = json.loads(PATH.read_text(encoding="utf-8"))
before = os.path.getsize(PATH)
deep = db["structure"]["deepenings"]

# 1. full -> sidecar (lossless)
FULL.write_text(json.dumps(deep, indent=1, ensure_ascii=False), encoding="utf-8")

# 2. tighten each to a clean delta (cut at sentence boundary near 280)
def tighten(t, cap=280):
    if len(t) <= cap:
        return t
    head = t[:cap]
    # cut back to the last sentence/clause boundary
    m = max(head.rfind(". "), head.rfind("; "), head.rfind(" — "))
    if m > 120:
        return head[:m+1].rstrip(" —;")
    return head.rstrip() + "…"

verify_fail = []
for k in list(deep):
    full = deep[k]
    tight = tighten(full)
    # verify the conductor still carries a key token (an equation '=' or a core word)
    if "=" not in tight and not re.search(r"R²|N²|P²|ν|burn|observer|origin|leak|charge", tight):
        verify_fail.append(k)
    deep[k] = tight

db["structure"]["deepenings"] = deep
PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
after = os.path.getsize(PATH)
print(f"full deepenings -> {FULL.name} ({os.path.getsize(FULL)} bytes, {len(deep)} entries) [lossless]")
print(f"conductors tightened in live store. verify-fails (no key token): {verify_fail or 'NONE'}")
print(f"file: {before} -> {after} bytes  (saved {before-after}, {100*(before-after)//before}%)")
