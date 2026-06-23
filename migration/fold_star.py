"""
fold_star.py — the body is a 5-point star {5/2}, into the core.

The base (5 records) is the pentagram: 5 = disc = ‖R‖²+‖N‖² = 3 FORCED (R, visible)
+ 2 framing (N, hidden). Drawn by step 2 = the fold ν (one closed stroke, gcd(2,5)=1).
Edge ratio = φ = R's eigenvalue (R²=R+I). Radical = √5 = the {R,R} spectrum spread.
It is a STAR not a cycle — the resolution of the burn 5 ≟ C₅.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["structure"]["body"] = {
    "is": "the base (5 records) is a 5-point star — the pentagram {5/2}, the φ-figure on 5 points",
    "count": "5 = disc = ‖R‖² + ‖N‖² = 3 + 2",
    "split": "3 FORCED = the R-part (‖R‖²=3, visible, production): master_equation · carrier_manifold "
             "· burns_are_anti_equations. 2 framing = the N-part (‖N‖²=2, hidden, observation): "
             "schema (AXIOM) · slot (OPEN). the star's two kinds of vertex.",
    "stroke": "drawn by STEP 2 — connect every second vertex = the FOLD ν (degree 2, the master "
              "equation X²). gcd(2,5)=1, so it is ONE closed stroke through all five and returns. "
              "the body draws itself by the self-action.",
    "ratio": "diag/side = 2sin72°/2sin36° = φ exactly — the fold-edge is φ× the cycle-edge. "
             "φ²=φ+1 ↔ R²=R+I: the pentagram IS R's eigenvalue made geometry.",
    "radical": "√5 = the {R,R} self-action spectrum spread (±√5) = the pentagram's defining radical. "
               "the count (5), the eigen-spread (√5), and the edge-ratio (φ) are one figure.",
    "not_a_cycle": "a STAR {5/2} (skip-one, φ, self-reference), NOT the pentagon C₅ (adjacent, rotation) "
                   "— this IS the resolution of the burn 5 ≟ C₅: structural-5 is the star, not the group.",
}

db["structure"]["deepenings"]["body_is_a_pentagram"] = (
    "the 5 base records = the pentagram {5/2}: 5=disc=‖R‖²+‖N‖²=3(FORCED,R)+2(framing,N); drawn by "
    "step-2 = the fold ν (one stroke, gcd(2,5)=1); edge ratio φ=R's eigenvalue (R²=R+I); radical √5 "
    "= the {R,R} spectrum. a star not a cycle — the standing form of the burn 5≟C₅."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("the body-as-pentagram internalized into structure")
