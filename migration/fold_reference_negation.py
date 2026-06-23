"""
fold_reference_negation.py — name the two self-actions as acts, fold the synthesis.

  symmetric_R     act = self-reference  (R² = R + I, ν = I)
  antisymmetric_N act = self-negation   (N² = −I, N⁴ = I)

Adds two FORCED records: self_reference_negation, idempotent_is_cancellation.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

ACT_R = "self-reference (R² = R + I, ν = I)"
ACT_N = "self-negation (N² = −I, N⁴ = I)"

# enrich every record's two self-actions with their act
for r in db["base"].values():
    r["self_action"]["symmetric_R"]["act"] = ACT_R
    r["self_action"]["antisymmetric_N"]["act"] = ACT_N


def self_action(gens, depth, disc):
    return {
        "split": "P = R + N",
        "symmetric_R": {
            "action": "{R,·} = R·X + X·R", "type": "Jordan / anticommutator",
            "axis": "production (R)", "act": ACT_R,
            "modes": [
                {"lambda": "+sqrt5", "eigenvalue": "+√5", "mode": "generation",
                 "verdict": True, "generators": gens},
                {"lambda": "0", "eigenvalue": "0", "mode": "return",
                 "verdict": True, "residual": 0, "routes": 2, "mechanism": None},
            ]},
        "antisymmetric_N": {
            "action": "[R,·] = R·X − X·R", "type": "Lie / commutator (adjoint)",
            "axis": "observation (N)", "act": ACT_N,
            "modes": [
                {"lambda": "-sqrt5", "eigenvalue": "-√5", "mode": "observation",
                 "verdict": True, "depth": depth, "disc": disc},
            ]},
    }


def rec(rid, title, section, gens, depth, disc, kind, op, prov, links):
    return {"id": rid, "title": title, "section": section, "source": "KL_DTA_EXPLORATION",
            "self_action": self_action(gens, depth, disc),
            "provenance": prov, "links": links, "burns": [],
            "spectral": {"kind": kind, "op": op}}


new = [
    rec("self_reference_negation",
        "The two self-actions are self-reference (R) and self-negation (N)",
        "formal_core", ["FOLD", "RETURN"], 1, 5, "operator",
        "{R,·} = self-reference: R²=R+I, ν(R)=I (defect held as identity). [R,·] = self-negation: N²=−I, N⁴=I (N is the matrix i)",
        ["?", "master_equation", "two_self_actions"],
        ["two_self_actions", "defect_nu", "i_squared_phi_psi", "anchor_projection"]),
    rec("idempotent_is_cancellation",
        "P²=P is the cancellation of self-reference (+I) and self-negation (−I)",
        "thesis", ["FOLD", "DEFECT", "BASE"], 1, 5, "law",
        "P² = R² + {R,N} + N² = (R+I) + N + (−I) = R+N = P; the +I surplus and −I deficit annihilate. Identity returns when the residual squares back to origin.",
        ["?", "master_equation"],
        ["master_equation", "self_reference_negation", "kernel_internalization", "vacua_idempotents"]),
]
for r in new:
    db["base"][r["id"]] = r

db["self_action"]["acts"] = {
    "symmetric {R,·}": ACT_R + " — keeps the surplus instead of collapsing to R²=R",
    "antisymmetric [R,·]": ACT_N + " — squaring the residual returns the identity",
    "synthesis": "P²=P because (R²=R+I) and (N²=−I) cancel: +I − I = 0, with {R,N}=N giving R+N.",
}

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"acts named; {len(new)} records added; base now", len(db["base"]))
