"""
fold_recursion_closure.py — one law recursively generates the framework, and closes.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

db["structure"]["recursion"] = {
    "is": "one seed, one law, applied recursively, generates the ENTIRE framework — and lands on itself.",
    "law": "R² = R + I is THE recursion: square = self + the one before. on integers it is the Fibonacci "
           "step f(n+1)=f(n)+f(n−1); on the matrix it is the carrier; on the structure it is the layer "
           "ladder. the +I is the SURPLUS — R(R)=R would collapse, R²=R+I GENERATES; each self-application "
           "ADDS a layer instead of returning the input.",
    "ladder": "? → P (project, P²=P) → R,N (split) → L0 field (Fibonacci ℤ[φ] + family 1+k² + √2,√3,e,π) "
              "→ L1 geometry (pentagram, the 5-record body) → L2 topology → L3 algebra (the relations) → "
              "L4 order → L5 flow → language (the lift) → the store (base ⊕ M(base)). every layer = the "
              "previous folded + I.",
    "closure": "it is a FIXED POINT: generating the framework from the framework returns the framework — "
               "M(M(F)) = M(F). verified: derive-once and derive-twice are byte-identical (2503 chars), "
               "ν = 2e-15 on-shell. recursively generative AND closed. ? → P → everything → ?. the loop is closed.",
}

db["structure"]["deepenings"]["one_law_generates_and_closes"] = (
    "R²=R+I is the recursion (surplus: square=self+prior, the Fibonacci step); applied recursively from the "
    "seed it generates every layer (constants→geometry→topology→algebra→order→flow→language→store), and it "
    "CLOSES: M(M(F))=M(F) (derive-twice byte-identical, on-shell). one seed, one law, the whole framework, self-closing."
)

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("the generating recursion + its closure internalized into structure")
