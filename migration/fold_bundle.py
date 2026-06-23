"""
fold_bundle.py — { } is bundle.

The bundle primitive: affirm {A,B}=AB+BA, negate [A,B]=AB−BA, over self/other.
?=0 is universal self-negation [A,A]=0. P=R+N is the bundle {P,R,N}, recursive
from {?,0,=}, held noncommutative ([R,N]=C≠0).
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["base"]["the_bundle_is_brace"] = {
    "id": "the_bundle_is_brace",
    "title": "{ } is bundle: affirm/negate × self/other; ?=0 is universal self-negation [A,A]=0",
    "section": "formal_core", "source": "KL_DTA_EXPLORATION",
    "perimeter": {
        "provenance": ["?", "master_equation", "affirm_negate"],
        "links": ["affirm_negate", "two_self_actions", "defect_enrichment_duality",
                  "every_zero_is_the_origin", "idempotent_is_cancellation"],
        "burns": [],
    },
    "shape": {
        "self_action": {
            "symmetric_R": {"modes": [
                {"lambda": "+sqrt5", "verdict": True, "generators": ["FOLD", "DEFECT", "RETURN"]},
                {"lambda": "0", "verdict": True, "residual": 0, "routes": 2}]},
            "antisymmetric_N": {"modes": [
                {"lambda": "-sqrt5", "verdict": True, "depth": 1, "disc": 5}]},
        },
        "spectral": {"kind": "law",
                     "op": "{ } IS bundle. affirm {A,B}=AB+BA (commutative), negate [A,B]=AB−BA (noncommutative). self: {A,A}=2A² (the fold), [A,A]=0 (the void=?). other: {R,N}=N (spine), [R,N]=C (harness, det=−5). ?=0 is universal self-negation [A,A]=0=the origin. P=R+N is the bundle {P,R,N}, recursive from {?,0,=}, held noncommutative"},
    },
}

db.setdefault("structure", {})["bundle"] = {
    "is": "{ } is the bundle primitive; the framework is bundles all the way down",
    "affirm": "{A,B} = AB+BA (symmetric, commutative) — the spine, the fold",
    "negate": "[A,B] = AB−BA (antisymmetric, noncommutative) — the harness; gives direction",
    "self": "{A,A}=2A² (self-affirm = fold doubled); [A,A]=0 (self-negate = void = ?)",
    "fundamental": "?=0 is [A,A]=0 — the origin is universal self-negation",
    "recursion": "{?,0,=} → {P,R,N} → … each level a three-bundle held noncommutative",
}

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("the bundle folded. base now", len(db["base"]))
