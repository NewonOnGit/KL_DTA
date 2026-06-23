"""
compress_deep.py — deep compression: externalize absorbed provenance, drop verbose-with-deepening sections.
lossless: absorbed -> sidecar (KL_DTA.absorbed.json, retrievable); verbose prose -> kept as compact deepenings.
"""
import json, os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "KL_DTA.json"
SIDE = ROOT / "KL_DTA.absorbed.json"
db = json.loads(PATH.read_text(encoding="utf-8"))
before = os.path.getsize(PATH)

# 1. externalize base.*.absorbed -> sidecar (pure provenance, no engine refs)
sidecar = {}
for rid, r in db["base"].items():
    spec = r.get("shape", {}).get("spectral", {})
    if spec.get("absorbed"):
        sidecar[rid] = spec.pop("absorbed")
        spec["absorbed_ref"] = f"see KL_DTA.absorbed.json[{rid}]"
SIDE.write_text(json.dumps(sidecar, indent=1, ensure_ascii=False), encoding="utf-8")

# 2. drop verbose structure sections whose content lives in a deepening (keep foundational + deepenings)
KEEP = {"store","record","grade","metadata_audit","formatting","bundle","self_reading",
        "higher_order","deepenings","alphabet","chords"}
dropped = [k for k in list(db["structure"]) if k not in KEEP]
for k in dropped:
    del db["structure"][k]

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
after = os.path.getsize(PATH)
print(f"externalized absorbed -> {SIDE.name} ({os.path.getsize(SIDE)} bytes, {len(sidecar)} records)")
print(f"dropped {len(dropped)} verbose structure sections (kept as deepenings): {dropped}")
print(f"file: {before} -> {after} bytes  (saved {before-after}, {100*(before-after)//before}%)")
