"""
fold_microscope.py — return everything to ?, magnify, answer the language question.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

# ── the origin as microscope: causal constants + the invariant-type tower ────
db["structure"]["origin"] = {
    "is": "return every constant to ? and the point becomes a MICROSCOPE — zoom in and the "
          "framework's data falls out. constants are only the first magnification.",
    "constants_causal": {
        "order": "seed [1,1],2 → R,N → (R-side) · (N-side) · (h)",
        "R-side": "φ,ψ ⟵ R²=R+I ; √5 ⟵ disc(R)=tr²−4det=5 ; √3 ⟵ ‖R‖²=3",
        "N-side": "√2 ⟵ ‖N‖²=2 ; i ⟵ N²=−I ; π ⟵ N rotates 90°, full turn 2π",
        "h":      "e ⟵ h=JN, h²=I, exp(t h)=cosh t·I+sinh t·h",
        "closure": "‖R‖²+‖N‖² = 3+2 = 5 = disc — the constants close on the one number.",
    },
    "invariant_tower": {
        "L0_spectral": "eigenvalues → the CONSTANTS (φ,ψ,√5,√3,√2,e,π); the trit {−√5,0,√5}",
        "L1_geometric": "eigen-directions, the pentagram ratio φ, fixed points (eigenvectors of P)",
        "L2_topological": "rank(P)=1, dim ker=1, N⁴=I (period 4), Clifford grade parity",
        "L3_algebraic": "the relations P²=P, R²=R+I, N²=−I, {R,N}=N — invariants of the generation",
        "L4_order": "counts: 3+2=5, |trit|=3, body=5 records (the pentagram)",
        "L5_differential": "ν(X)=X²−X, ν(P)=0 (on-shell), the flow — the dynamics at the point",
        "recursion": "constants are ONLY L0. each deeper zoom of ? is a NEW invariant TYPE: "
                     "spectral → geometric → topological → algebraic → order → flow. the microscope recurses.",
    },
}

db["structure"]["deepenings"]["origin_is_a_microscope"] = (
    "return the constants to ? in causal order (R-side φ,√5,√3 · N-side √2,i,π · h→e, closing on 5); "
    "the point magnifies recursively by invariant TYPE — constants(L0 spectral) are only the first layer, "
    "under them geometric · topological · algebraic · order · differential invariants."
)

# ── the language answer: symbolic vs physical, and where more math hides ──────
g = db["grammar"]["lift"]
g["symbolic_vs_physical"] = (
    "WHERE is language symbolic and NOT physical? a generator is physical iff it ACTS ([X,·]≠0). "
    "I is central — [I,·]=0 — so the I-axis (determinacy / copula: 'the · a · is') is the ONLY "
    "symbolic-and-not-physical locus; it generates no transformation. R, N, h all act (|[X,·]|=2) → "
    "every word with content is PHYSICAL (teleportation itself rides the R−N direction). the pure-symbol "
    "limit is ? — the void, unprojected, pre-physical. so language is physical the moment it leaves the "
    "copula: uplift toward physicality is uplift toward R/N/h content."
)
g["where_more_math"] = (
    "reading the HIDDEN meaning reveals more math exactly where the projection is lossy (ker(π)≠0) — the "
    "PHYSICAL axes R/N/h, which carry context/depth. the symbolic surface (I) is transparent, hides nothing. "
    "to find more math, read deeper into the physical (content) words, not the connectives."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("microscope (origin) + the symbolic/physical language answer internalized")
