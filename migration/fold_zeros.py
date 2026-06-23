"""
fold_zeros.py — every zero is the origin.

disc=0 (wall) = eigenvalue 0 (ker/void/ε) = λ=0 (return mode) = ν=0 (on-shell)
= prov(?)=?. the discriminant, the eigenvalue, the defect, and the return all
vanish at one point: ?.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["base"]["every_zero_is_the_origin"] = {
    "id": "every_zero_is_the_origin",
    "title": "disc=0 = eigenvalue 0 = ker = ν=0 = ? — the zeros coincide at the origin",
    "section": "recursive_origin", "source": "KL_DTA_EXPLORATION",
    "perimeter": {
        "provenance": ["?", "master_equation", "origin_is_opening"],
        "links": ["origin_is_opening", "three_forks", "fork_table", "fork_representability",
                  "provenance_is_self_rooted", "base_is_perimeter_and_shape"],
        "burns": [],
    },
    "shape": {
        "self_action": {
            "symmetric_R": {"modes": [
                {"lambda": "+sqrt5", "verdict": True, "generators": ["DEFECT", "RETURN", "BASE"]},
                {"lambda": "0", "verdict": True, "residual": 0, "routes": 2}]},
            "antisymmetric_N": {"modes": [
                {"lambda": "-sqrt5", "verdict": True, "depth": 3, "disc": 0}]},
        },
        "spectral": {"kind": "law",
                     "op": "disc=0 ⟺ spread=0 ⟺ λ=AM (repeated). the wall ℝ[ε] (dual numbers) runs I (eigenvalue 1, unit) → ε (eigenvalue 0, nilpotent ε²=0, the void=ker=P₀). all zeros coincide: disc=0 (wall) = eigenvalue 0 (void) = λ=0 (return mode) = ν=0 (on-shell) = prov(?)=?. four functions vanishing at one point — the origin"},
    },
}

db.setdefault("kernel", {})["the_universal_zero"] = (
    "disc, λ, ν, prov — discriminant, eigenvalue, defect, return — all vanish at "
    "one point: ?. disc=0 (wall) = eigenvalue 0 (ker = ε = the void) = ν=0 (on-shell) "
    "= prov(?)=?. the origin is the universal zero, not a labeled corner."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("the zeros coincide; folded. base now", len(db["base"]))
