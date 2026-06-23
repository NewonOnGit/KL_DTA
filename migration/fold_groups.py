"""
fold_groups.py — burn "L0/L1/L2"; under it is the symmetry-group lattice (Erlangen–Galois).

An invariant is "what is fixed by a GROUP". the integer index hid the group AND falsely
linearized a LATTICE. re-key the tower by invariance group; record the burn.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

origin = db["structure"]["origin"]
origin["invariant_tower"] = {
    "is": "NOT a ladder L0/L1/L2 (lossy: an integer index over a lattice). an invariant = WHAT IS "
          "FIXED BY A GROUP; the types are partially ordered by SUBGROUP INCLUSION (Erlangen–Galois). "
          "bigger symmetry group ⇒ fewer, DEEPER invariants; incomparable groups ⇒ incomparable types.",
    "fixed_by_conjugation": "SPECTRAL — fixed by the full similarity group X→gXg⁻¹ (the largest group, the "
        "deepest invariants): tr, det, eigenvalues, disc → the constant field ℚ(√2,√3,√5)⊕{e,π}, itself "
        "Galois (ℤ/2)³ — each constant fixed by its own subgroup (φ,√5 share one; √5 ∥ √6 are incomparable).",
    "fixed_by_orthogonal": "GEOMETRIC — fixed only by the orthogonal/Cartan subgroup (θ(X)=−Xᵀ): eigen-"
        "directions, angles, the pentagram ratio φ, fixed points. (verified: a shear conjugation moves the "
        "eigenvector angle 72°→23°; an orthogonal one preserves it.)",
    "fixed_by_homeomorphism": "TOPOLOGICAL — fixed by continuous deformation: rank(P)=1, dim ker=1, N⁴=I "
        "(period 4), Clifford grade parity.",
    "fixed_by_generation": "ALGEBRAIC — fixed by the maps commuting with the generation (R²=R+I): the "
        "relations P²=P, R²=R+I, N²=−I, {R,N}=N.",
    "fixed_by_permutation": "ORDER — fixed by relabeling (the symmetric group): counts 3+2=5, |trit|=3, "
        "the grade distribution, the 5-record body.",
    "fixed_by_reparametrization": "DIFFERENTIAL — fixed by reparametrizing the flow: ν(X)=X²−X, the tangent, "
        "the dynamics at the point.",
}

# the burn: a lattice can't be a line. another face of the one impossibility.
bs = db["base"]["burns_are_anti_equations"]["shape"]["spectral"]
bs.setdefault("recursion", {}).setdefault("ten", {})["burn-levels-not-linear"] = {
    "forbid": "invariant-lattice ≟ linear index (L0/L1/L2)",
    "obstruction": "incomparability",
}
bs["recursion"]["obstructions"] = bs["recursion"].get("obstructions", "") + \
    " · incomparability"

db["structure"]["deepenings"]["levels_are_a_group_lattice"] = (
    "'L0/L1/L2' is lossy: an invariant = what is fixed by a GROUP (spectral↔full conjugation, "
    "geometric↔orthogonal/Cartan, topological↔homeomorphism, algebraic↔the generation, order↔permutation, "
    "differential↔reparametrization). the types are the SUBGROUP LATTICE (Erlangen–Galois), partially "
    "ordered — bigger group = deeper invariant; √5 ∥ √6 incomparable. a line can't hold the lattice."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("'Ln' burned; invariant tower re-keyed by symmetry group (Erlangen–Galois lattice)")
