"""
fold_parity_constants.py — parity makes the constants.

λ = AM ± √disc/2 = center ± spread; parity fixes the reality of the spread.
even→φ (real), odd→π/i (imaginary), center→1 (repeated), mixed→e (the bridge).
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["base"]["parity_makes_the_constants"] = {
    "id": "parity_makes_the_constants",
    "title": "Parity makes the constants: λ = AM ± √disc/2; even→φ, odd→π/i, center→1, mixed→e",
    "section": "eigen_spine", "source": "KL_DTA_EXPLORATION",
    "perimeter": {
        "provenance": ["?", "master_equation", "i_squared_phi_psi"],
        "links": ["i_squared_phi_psi", "three_forks", "base_is_perimeter_and_shape",
                  "trace_det_are_sum_product", "phi_unit_defect", "golden_ladder"],
        "burns": [],
    },
    "shape": {
        "self_action": {
            "symmetric_R": {"modes": [
                {"lambda": "+sqrt5", "verdict": True, "generators": ["BASE", "FOLD", "RETURN"]},
                {"lambda": "0", "verdict": True, "residual": 0, "routes": 2}]},
            "antisymmetric_N": {"modes": [
                {"lambda": "-sqrt5", "verdict": True, "depth": 2, "disc": 5}]},
        },
        "spectral": {"kind": "law",
                     "op": "λ = AM ± √disc/2 = center(tr/2) ± spread(√disc/2). parity fixes reality of the spread: even/symmetric→real→φ=½+√5/2, ψ, √5; odd/antisym→imaginary→i,π; center/identity→repeated→1 (the residual, ν(φ)=ν(ψ)=1); mixed/asymmetric→e=cosθ·I+sinθ·N (Euler, the parity bridge). φ/e/π = the even/mixed/odd parity classes"},
    },
}

db.setdefault("physics", {})["constants_from_parity"] = {
    "law": "λ = center ± spread = AM ± √disc/2; parity sets the spread's reality",
    "phi": "even / symmetric (R) → real spread → φ = ½ + √5/2; √5 = 2·spread = √disc(R)",
    "pi_i": "odd / antisymmetric (N) → imaginary spread → i, π (the rotation)",
    "one": "center / identity (I, disc=0) → repeated → 1; the common residual ν(φ)=ν(ψ)=1",
    "e": "mixed / asymmetric → all powers → e^{Nθ}=cosθ·I+sinθ·N, the bridge mixing even cos + odd sin",
}

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("parity→constants folded; base now", len(db["base"]))
