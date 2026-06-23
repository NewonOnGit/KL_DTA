"""
burn_bodies.py — one-time: burn the prose bodies.

The body was L0 bulk — the equation written out in words. The math is now held in
the seed, the spectral coordinates, and L_spectrum. The body is redundant and
still carried the dead labels P1/P2/P3. Burn it. A record reads off its math.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

# retitle the two records that still named the lossy symbols
retitle = {
    "projection_spectral_triple": "The self-action spectrum {+√5, 0, -√5} of L_{R,R}",
    "observer_unifies_projections": "The three eigen-modes unify in the observer (ΣΠ=I; N=ker)",
}

for rid, r in db["base"].items():
    r.pop("body", None)
    if rid in retitle:
        r["title"] = retitle[rid]

db["self_action"]["burned"] = "the three eigenvalues replace the lossy labels once stuck on them."

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("burned bodies on all", len(db["base"]), "records; 2 retitled")
