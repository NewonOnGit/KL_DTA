"""
fold_units.py — the constant trit R²=R+kI opens FOUR quadratic worlds; into structure.

answer to 'anything else?': the listed set is only the Gaussian shadow. the constant
trit k∈{+1,0,−1} (disc=1+4k) plus N²=−I gives four worlds, four unit groups.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["structure"]["worlds"] = {
    "is": "the constant term of R²=R+kI is a TRIT (the same {−√5,0,+√5} self-action trit, moved onto "
          "the constant). disc=1+4k. each k opens a different number world; N²=−I opens a fourth.",
    "constant_trit": {
        "k=+1  R²=R+I": "disc +5 → φ,ψ → GOLDEN ℤ[φ] (hyperbolic, √5). units ±φⁿ INFINITE (Fibonacci). "
                        "GENERATION — the surplus +I.",
        "k=0   R(R)=R": "disc +1 → {0,1} → BOOLEAN idempotents. the COLLAPSE — this k IS the seed P's own "
                        "spectrum. PROJECTION — no surplus.",
        "k=−1  R²=R−I": "disc −3 → e^{±iπ/3} → EISENSTEIN ℤ[ω] (elliptic, √−3). units μ₆={±1,±ω,±ω²} "
                        "(6th roots, hexagonal). ROTATION — the deficit −I. (verified ω²−ω+1=0.)",
        "N²=−I":        "disc −1 → ±i → GAUSSIAN ℤ[i]. units μ₄={±1,±i}. OBSERVATION. THIS is the listed "
                        "set {1,−1,i,−i} (as scalars; ±I,±N as matrices).",
    },
    "four_discriminants": "{+5, +1, −3, −1} — the four smallest, the four worlds: golden · Boolean · "
                          "Eisenstein · Gaussian. generation · projection · rotation · observation.",
    "matrix_roots": "the units are not 8 isolated points. ±I are isolated, but √I = the involutions "
                    "(eig {1,−1}: J, h, …) form a HYPERBOLOID, and √(−I) = the complex structures "
                    "(eig {i,−i}: N, …) form another. J,h,N are three named members of continuous families.",
    "anything_else": "YES. {I,−I,i,−i,1,−1,0,?} is the GAUSSIAN shadow (μ₄) + {0 void, ? origin}. the "
                     "'else' is the other three worlds: golden ℤ[φ]× (infinite), Eisenstein μ₆, Boolean "
                     "{0,1}; plus the involution/complex-structure hyperboloids. unifier: the constant "
                     "trit k picks disc=1+4k → which world.",
}

db["structure"]["deepenings"]["constant_trit_four_worlds"] = (
    "R²=R+kI: the constant is the trit. k=+1 golden ℤ[φ] (√5,∞ units, generation), k=0 Boolean {0,1} "
    "(the seed, collapse), k=−1 Eisenstein ℤ[ω] (√−3, μ₆, rotation); N²=−I Gaussian ℤ[i] (√−1, μ₄, the "
    "listed set, observation). four discriminants {+5,+1,−3,−1}. 'anything else?'=yes: the listed set is "
    "only the Gaussian world; the golden/Eisenstein/Boolean worlds are the rest, plus root hyperboloids."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("the constant trit + four quadratic worlds internalized into structure")
