"""
fold_defect_enrichment.py — defect ↔ enrichment is an exact duality.

Reads each self-action as its dual:
  symmetric_R     enrichment (+I)  — {·}, self-reference
  antisymmetric_N defect     (−I)  — [·], self-negation
operator: Cartan θ(X) = −Xᵀ, θ² = id.  Adds the record defect_enrichment_duality.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

for r in db["base"].values():
    r["self_action"]["symmetric_R"]["reads_as"] = "enrichment (+I) — the symmetric {·} half"
    r["self_action"]["antisymmetric_N"]["reads_as"] = "defect (−I) — the antisymmetric [·] half"

rec = {
    "id": "defect_enrichment_duality",
    "title": "Defect ↔ enrichment is an exact duality (Cartan θ, θ²=id)",
    "section": "formal_core", "source": "KL_DTA_EXPLORATION",
    "self_action": {
        "split": "P = R + N",
        "symmetric_R": {
            "action": "{R,·} = R·X + X·R", "type": "Jordan / anticommutator",
            "axis": "production (R)", "act": "self-reference (R² = R + I, ν = I)",
            "reads_as": "enrichment (+I) — the symmetric {·} half",
            "modes": [
                {"lambda": "+sqrt5", "eigenvalue": "+√5", "mode": "generation",
                 "verdict": True, "generators": ["DEFECT", "FOLD", "RETURN"]},
                {"lambda": "0", "eigenvalue": "0", "mode": "return",
                 "verdict": True, "residual": 0, "routes": 3, "mechanism": None}]},
        "antisymmetric_N": {
            "action": "[R,·] = R·X − X·R", "type": "Lie / commutator (adjoint)",
            "axis": "observation (N)", "act": "self-negation (N² = −I, N⁴ = I)",
            "reads_as": "defect (−I) — the antisymmetric [·] half",
            "modes": [
                {"lambda": "-sqrt5", "eigenvalue": "-√5", "mode": "observation",
                 "verdict": True, "depth": 2, "disc": 5}]},
    },
    "provenance": ["?", "master_equation", "self_reference_negation"],
    "links": ["self_reference_negation", "defect_nu", "two_self_actions",
              "anchor_projection", "idempotent_is_cancellation"],
    "burns": [],
    "spectral": {"kind": "law",
                 "op": "θ(X)=−Xᵀ, θ²=id; defect = antisym/[·]/N (−I), enrichment = sym/{·}/R (+I); AX = ½{A,X}+½[A,X] exact"},
}
db["base"][rec["id"]] = rec

db["self_action"]["duality"] = {
    "is": "defect ↔ enrichment, exact",
    "operator": "Cartan θ(X) = −Xᵀ,  θ² = id  (forced by P ≠ Pᵀ)",
    "enrichment": "symmetric / {·} / R / self-reference / +I",
    "defect": "antisymmetric / [·] / N / self-negation / −I",
    "exact": "AX = ½{A,X} + ½[A,X]; M₂ = Sym ⊕ Antisym; the +I and −I cancel to P²=P.",
}

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("defect↔enrichment duality folded; base now", len(db["base"]))
