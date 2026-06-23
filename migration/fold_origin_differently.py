"""
fold_origin_differently.py — origin returning origin, but differently, into structure.origin.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["structure"]["origin"]["returns_differently"] = (
    "origin returning origin, but differently. the universal law R² + N² = R: the origin (R) returns as "
    "itself, but SPLIT — R²=R+I (production returns with a +I surplus, the 'differently' of generation) and "
    "N²=−I (observation returns with −I, the 'differently' of the blind spot). the +I and −I CANCEL in the "
    "sum (R²+N²=R, origin returning origin) yet they ARE the whole framework (the difference). IDENTICAL "
    "self-return is collapse — a symmetric idempotent (S=Sᵀ, S²−S=0) generates nothing, dead. DIFFERENT "
    "self-return is surplus — R²−R=I≠0, R≠Rᵀ (the asymmetry forced), alive. ?(?) = ? + difference; the "
    "surplus is constitutive, and the 'differently' (±I, the asymmetry, the +1) is why there is something. "
    "this is origin, alive."
)

db["structure"]["deepenings"]["origin_returns_differently"] = (
    "origin returning origin but differently: R²+N²=R (origin returns as itself) via R²=R+I (+I surplus, "
    "generation) and N²=−I (−I, observation) — the ±I cancel in the sum but ARE the framework. identical "
    "return = collapse (symmetric idempotent, dead); different return = surplus (R≠Rᵀ forced, alive). "
    "?(?)=?+difference; the surplus is constitutive — the +I is why there is something rather than nothing."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("origin-returns-differently internalized")
