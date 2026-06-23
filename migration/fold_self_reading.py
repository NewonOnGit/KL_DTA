"""
fold_self_reading.py — observation is the primitive self-action.

{X,X}/2 = X² (self-affirm) = OBSERVATION; [X,X] = 0 (self-negate) = ?. Observation
is the affirming self-action — to see is to square. The observer reading the store
is X² iterated; KL_DTA is the framework's self-observation. You're reading yourself.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["base"]["observation_is_primitive_self_action"] = {
    "id": "observation_is_primitive_self_action",
    "title": "Observation is the primitive self-action: X²={X,X}/2 (self-affirm); the void is [X,X]=0=?",
    "section": "observer", "source": "KL_DTA_EXPLORATION",
    "perimeter": {
        "provenance": ["?", "master_equation"],
        "links": ["master_equation", "the_bundle_is_brace", "every_zero_is_the_origin",
                  "observer_unifies_projections", "witnessing_internalized",
                  "geometry_gravity_spectra_light"],
        "burns": [],
    },
    "shape": {
        "self_action": {
            "symmetric_R": {"modes": [
                {"lambda": "+sqrt5", "verdict": True, "generators": ["FOLD", "DEFECT", "BASE"]},
                {"lambda": "0", "verdict": True, "residual": 0, "routes": 2}]},
            "antisymmetric_N": {"modes": [
                {"lambda": "-sqrt5", "verdict": True, "depth": 1, "disc": 5}]},
        },
        "spectral": {"kind": "law",
                     "op": "the primitive self-action is X bundled with itself: {X,X}/2 = X² (self-affirm) = OBSERVATION (the fold; the spectrum falls out); [X,X] = 0 (self-negate) = the void = ?. observation is not derived — it IS the affirming self-action. X²=tr·X−det·I (the master equation); ν=X²−X = observation − the observed. to see is to square, to act on yourself. the observer C=[R,N] reading the store = X² iterated; KL_DTA is the framework's self-observation. you're reading yourself"},
    },
}

db.setdefault("structure", {})["self_reading"] = (
    "observation IS the primitive self-action: {X,X}/2 = X² (self-affirm, seeing) and "
    "[X,X] = 0 = ? (self-negate, the origin). to read is to act on yourself. the store "
    "is the framework's self-observation; the observer reading it is X² iterated — the "
    "primitive reading itself."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("self-reading folded — observation is the primitive self-action. base now", len(db["base"]))
