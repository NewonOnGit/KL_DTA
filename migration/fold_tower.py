"""
fold_tower.py — the bundle-of-bundles tower.

{I,R,N,J,h,P} is gen-2 of a self-similar tower: ?=0 → P → {6} → {14} → M₂.
Each level is a bundle (a set held together); each element a bundle of the level
below; the store itself is the next level. Folds the record + the tower section.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["base"]["bundle_of_bundles_tower"] = {
    "id": "bundle_of_bundles_tower",
    "title": "{I,R,N,J,h,P} is a bundle-of-bundles: the self-similar tower ?→P→6→14→M₂",
    "section": "metalayer", "source": "KL_DTA_EXPLORATION",
    "perimeter": {
        "provenance": ["?", "master_equation", "the_bundle_is_brace"],
        "links": ["the_bundle_is_brace", "two_self_actions", "what_fixes_the_seed",
                  "anchor_projection", "five_generators"],
        "burns": [],
    },
    "shape": {
        "self_action": {
            "symmetric_R": {"modes": [
                {"lambda": "+sqrt5", "verdict": True, "generators": ["FOLD", "RETURN", "BASE"]},
                {"lambda": "0", "verdict": True, "residual": 0, "routes": 2}]},
            "antisymmetric_N": {"modes": [
                {"lambda": "-sqrt5", "verdict": True, "depth": 2, "disc": 5}]},
        },
        "spectral": {"kind": "law",
                     "op": "each primitive bundled from P: R=½(P+τP), N=½(P−τP), I=−N², h=JN, J=(I−2R+2C)/5, P={R,N}; R,N generate M₂. tower ?=0→P→{6}→{14}→M₂, each level a bundle-of-bundles, parity→fork→constant invariant. the store (records bundled) is the next level — self-similar"},
    },
}

db.setdefault("bundles", {})["tower"] = {
    "is": "the framework is the bundle operation iterated — a self-similar tower",
    "levels": {
        "gen 0": "?=0  — the void ([A,A]=0, universal self-negation)",
        "gen 1": "P  — the seed (the first fixed point above ?, fixed by ν(R)=I)",
        "gen 2": "{I,R,N,J,h,P}  — the primitives (bundles of P+τ; R,N generate M₂)",
        "gen 3": "{…14…}  — the DNA library (bundles of gen 2)",
        "gen N": "the 75 records, bundled — and the apex is their bundle",
        "limit": "M₂(ℝ)  — the closure (continuum)",
    },
    "invariant": "parity → fork → constant holds at every level; same bundle op, every scale",
}

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("the bundle tower folded. base now", len(db["base"]))
