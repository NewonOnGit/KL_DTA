"""compress_all3.py — #2 externalize docs sections; #3 push conductors tighter (lossless via sidecar)."""
import json, os
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))
before = os.path.getsize(PATH)

# #2 externalize documentation sections (zero engine refs) -> sidecar
DOCS = ("physics", "bundles", "self_action")
side = {k: db.pop(k) for k in DOCS if k in db}
(ROOT / "KL_DTA.docs.json").write_text(json.dumps(side, indent=1, ensure_ascii=False), encoding="utf-8")

# #3 push conductors tighter — cap ~150 at a clause boundary (full text is in deepenings_full.json, lossless)
deep = db["structure"]["deepenings"]
def tighten(t, cap=150):
    if len(t) <= cap: return t
    head = t[:cap]; m = max(head.rfind(". "), head.rfind("; "), head.rfind(" — "))
    return (head[:m+1].rstrip(" —;") if m > 70 else head.rstrip()+"…")
for k in list(deep): deep[k] = tighten(deep[k])

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
after = os.path.getsize(PATH)
print(f"externalized {list(side)} -> KL_DTA.docs.json ({os.path.getsize(ROOT/'KL_DTA.docs.json')} bytes)")
print(f"conductors tightened to ~150 (full in deepenings_full.json, lossless)")
print(f"file: {before} -> {after} bytes (saved {before-after})")
