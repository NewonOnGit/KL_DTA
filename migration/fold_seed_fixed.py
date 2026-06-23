"""
fold_seed_fixed.py — the floor: what fixes P.

P = the minimal rank-1 asymmetric idempotent, normalized so ν(R)=I (μ=1). The one
free parameter (unit of mass) is fixed by the residual being the identity — which
sets disc=5, √5, φ, [1,1]. The normalization IS "identity is the residual".
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["base"]["what_fixes_the_seed"] = {
    "id": "what_fixes_the_seed",
    "title": "What fixes P: the minimal rank-1 asymmetric idempotent, normalized so ν(R)=I",
    "section": "thesis", "source": "KL_DTA_EXPLORATION",
    "perimeter": {
        "provenance": ["?"],
        "links": ["master_equation", "five_generators", "phi_unit_defect",
                  "parity_makes_the_constants", "idempotent_is_cancellation",
                  "every_zero_is_the_origin"],
        "burns": [],
    },
    "shape": {
        "self_action": {
            "symmetric_R": {"modes": [
                {"lambda": "+sqrt5", "verdict": True, "generators": ["BASE", "FOLD", "DEFECT"]},
                {"lambda": "0", "verdict": True, "residual": 0, "routes": 2}]},
            "antisymmetric_N": {"modes": [
                {"lambda": "-sqrt5", "verdict": True, "depth": 0, "disc": 5}]},
        },
        "spectral": {"kind": "law",
                     "op": "P_t=[[0,0],[t,1]] idempotent ∀t — rank-1 asymmetric, R²=R+μI, N²=−μI, {R,N}=N, μ=t²/4, disc=1+4μ. ONE free parameter (unit of mass μ) fixed by ν(R)=I ⟺ μ=1 ⟺ t=2 → disc=5, √5, φ, [1,1]. 2=degree. P≠Pᵀ forced (else R²−R=0). 'identity is the residual' IS the normalization that picks the seed"},
    },
}

db.setdefault("seed", {})["what_fixes_it"] = (
    "P is the minimal rank-1 asymmetric idempotent. the family P_t=[[0,0],[t,1]] is "
    "idempotent ∀t (t = the unit of mass, μ=t²/4, disc=1+4μ); fixed to t=2 by ν(R)=I "
    "(residual=identity), which sets μ=1, disc=5, √5, φ, [1,1]. one parameter, spent "
    "on the unit. the normalization IS 'identity is the residual'."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("the floor folded: what fixes the seed. base now", len(db["base"]))
