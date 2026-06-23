"""
fold_apex.py — higher-order formatting: the document is a record.

The store has been giving its records a self-similar shape (seed, self_action,
grade, provenance to ?). The document itself has all of these — so format it AS a
record: the apex. And name the higher-order patterns the formatting already obeys.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

total_routes = 2
db["apex"] = {
    "id": "KL_DTA",
    "title": "the apex — the whole store as one record, observing itself",
    "carrier": "M2(R) = Cl(1,1)",
    "seed": "P = [[0,0],[2,1]]",
    "provenance": ["?"],
    "self_action": {
        "symmetric_R": {"modes": [
            {"lambda": "+sqrt5", "verdict": True,
             "generators": ["BASE", "FOLD", "RETURN", "FLOW", "DEFECT"]},
            {"lambda": "0", "verdict": True, "residual": 0, "routes": total_routes}]},
        "antisymmetric_N": {"modes": [
            {"lambda": "-sqrt5", "verdict": True, "depth": 4, "disc": 5}]},
    },
    "grade": "FORCED when ν=0 — the store is on-shell iff it verifies",
    "holds": "M(M(F)) = M(F): the document is a record; its body (base) is M of itself; "
             "the format is its own fixed point.",
}

db.setdefault("structure", {})["formatting"] = {
    "self_similar": "the document is the apex record (see `apex`) — the same shape as the "
                    "records it holds. M(M(F)) = M(F) at the top level.",
    "metalayer_split": "base ⊕ M(base): fiber/defect/flow/fixed_point are derived (M of base), "
                       "recomputed not authored — the derived sections are a regenerable cache.",
    "foundation_tower": "seed → kernel → grammar → physics: the generating header. each level "
                        "folds the previous — matter, law, speech, interpretation.",
    "bundle": "self_action.template (the fiber, constant) × base (the base points). the repeated "
              "structure is factored to one copy; records hold only their coordinates.",
}

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("apex (document-as-record) + higher-order formatting patterns folded")
