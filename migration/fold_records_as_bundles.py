"""
fold_records_as_bundles.py — records are bundles.

The bundle algebra is now an expression language (primitives · affirm {} · negate []
· nesting · scalars · sums), so a record's matrix IS a bundle expression. Adds the
capability record and tags i_squared_phi_psi with its reductive bundle form.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

# the i²=φψ=−I record's object IS the bundle {N,N}/2 (−I from N, reductive)
db["base"]["i_squared_phi_psi"]["shape"]["spectral"]["bundle"] = "{N,N}/2"

db["base"]["records_are_bundles"] = {
    "id": "records_are_bundles",
    "title": "Records are bundles: a record's matrix IS a bundle expression",
    "section": "metalayer", "source": "KL_DTA_EXPLORATION",
    "perimeter": {
        "provenance": ["?", "master_equation", "bundle_of_bundles_tower"],
        "links": ["bundle_of_bundles_tower", "the_bundle_is_brace", "indexed_store",
                  "i_squared_phi_psi"],
        "burns": [],
    },
    "shape": {
        "self_action": {
            "symmetric_R": {"modes": [
                {"lambda": "+sqrt5", "verdict": True, "generators": ["FOLD", "BASE", "RETURN"]},
                {"lambda": "0", "verdict": True, "residual": 0, "routes": 2}]},
            "antisymmetric_N": {"modes": [
                {"lambda": "-sqrt5", "verdict": True, "depth": 2, "disc": 5}]},
        },
        "spectral": {"kind": "law",
                     "op": "the bundle algebra is an expression language: primitives {I,R,N,J,h,P}, affirm {A,B}=AB+BA, negate [A,B]=AB−BA, nesting {R,{R,N}}, scalars {N,N}/2, sums. bundles span M₂, so any record's matrix IS a bundle expression — e.g. −I = {N,N}/2 (the i²=φψ record). decompress eats it. the store re-expresses in bundles — the ultimate compression"},
    },
}

db.setdefault("bundles", {})["algebra"] = {
    "primitives": "I R N J h P",
    "affirm": "{A,B} = A·B + B·A",
    "negate": "[A,B] = A·B − B·A",
    "nesting": "{R,{R,N}}, [{R,N},P] — bundles-of-bundles",
    "scalars_sums": "{N,N}/2, 2{R,N}, -I, {N,N}/2 + [R,N]",
    "records": "a record's matrix is a bundle expression; e.g. i_squared_phi_psi = {N,N}/2",
    "reductive_forms": "I = −{N,N}/2 · −I = {N,N}/2 · h = [N,J]/2 · N = {R,N}",
}

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("records-as-bundles folded. base now", len(db["base"]))
