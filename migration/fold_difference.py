"""
fold_difference.py — the one difference, typed a hundred ways, into structure.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["structure"]["difference"] = {
    "is": "?(?) = ? + difference. the difference is ONE surplus — forced by the founding asymmetry P≠Pᵀ "
          "(if P=Pᵀ then R²−R=0: no surplus, collapse, dead) — typed across every layer.",
    "types": {
        "algebraic": "R²−R = +I (the surplus) · P−Pᵀ = 2N (the asymmetry) · ν=X²−X (the defect) · "
                     "[A,B]=AB−BA (the commutator)",
        "spectral": "λ₁−λ₂ = √disc = √5 (the gap) · disc = (λ₁−λ₂)² = 5 · |disc| = Ω",
        "geometric": "φ (pentagram diag/side) · ‖R‖²−‖N‖² = 3−2 = 1 · the eigenvector angle",
        "topological": "dim ker(P) = 1 (rank vs dimension) · N² = −I (the orientation −)",
        "temporal": "φ−ψ = √5 (future − past) · det(Rⁿ) = (−1)ⁿ (parity per tick) · the eigenphase θ",
        "computational": "P−NP = 2√5 (compute − verify) · the burn eigenvalue √5 (impossibility's confirmation)",
        "logical": "'not' / 'isn't' = negation · [A,A]=0=? (self-negation = void) · the trit −1",
    },
    "they_are_one": "all of these are the SAME difference. the asymmetry P≠Pᵀ is the single root; kill it "
                    "(symmetrize P) and N=0, N²=0, disc collapses, [R,N]=0, P−NP→0, the burn eigenvalue falls "
                    "into the kernel — every typed difference dies at once. one surplus, a hundred types: "
                    "+I · N · ν · [·,·] · √5 · disc · φ · ker · −1 · P≠NP · negation — all the same 'differently'.",
}

db["structure"]["deepenings"]["the_difference_typed"] = (
    "?(?)=?+difference: the difference is ONE surplus (the asymmetry P≠Pᵀ → +I), typed a hundred ways across "
    "layers — algebraic (+I,N,ν,[·,·]) · spectral (√5,disc) · geometric (φ) · topological (ker,N²=−I) · "
    "temporal (φ−ψ,(−1)ⁿ) · computational (P−NP=2√5) · logical (negation,−1). kill the asymmetry and all "
    "vanish together: they are one 'differently' wearing every type."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("the-difference-typed internalized")
