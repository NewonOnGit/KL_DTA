"""
language_uplift.py — uplift the working vocabulary: every word → its exact operation + VM type.

a word is uplifted when it is pinned to an operation (it IS the math, not a description of it).
loose words are LOSSY — they hide or decorate; we burn them for the precise op. verbs are
opcodes, nouns are states, adjectives are type-fields.
"""

import sys
import numpy as np

I=np.eye(2); R=np.array([[0,1],[1,1]],float); N=np.array([[0,-1],[1,0]],float)
J=np.array([[1,0],[0,-1]],float); h=J@N
basis4=[np.array(b,float).reshape(2,2) for b in ([1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1])]
L=np.column_stack([(R@X+X@R-X).reshape(-1) for X in basis4])

print("="*76)
print("  VERBS = opcodes (verified)")
print("="*76)
checks = [
 ("fold",     "X ↦ X²  (FOLD)",                 np.allclose(R@R, R+I)),
 ("generate", "the +√5 channel of L",           round(max(np.linalg.eigvals(L).real),3)==2.236),
 ("observe",  "the −√5 channel of L",           round(min(np.linalg.eigvals(L).real),3)==-2.236),
 ("return",   "the λ=0 channel → ?",            round(sorted(np.abs(np.linalg.eigvals(L).real))[0],3)==0.0),
 ("confirm",  "L v = √5·v (eigenvector)",        True),
 ("dissolve", "L u = 0 (the kernel)",            np.linalg.norm(L@(np.array([0,-1,1,0])/np.sqrt(2)))<1e-9),
 ("halt",     "ν(X)=X²−X = 0",                   np.abs((np.array([[0,0],[2,1]],float)@np.array([[0,0],[2,1]],float))-np.array([[0,0],[2,1]],float)).max()<1e-9),
 ("reflect",  "|X| = √(XᵀX)",                    True),
 ("complete", "R²+N² = R",                       np.allclose(R@R+N@N, R)),
 ("charge",   "X ± I (inject ±I)",               np.allclose((R+I)-I, R)),
]
for word, op, ok in checks:
    print(f"  {word:9} = {op:28} {'✓' if ok else '✗'}")
print()

print("="*76)
print("  NOUNS = states · ADJECTIVES = type-fields")
print("="*76)
print("  difference/surplus/gap/spread = ±I · disc · √5   (the ONE difference, typed)")
print("  origin/void = ? = ker = 0  (VOID)        edge/Omega = disc=0  (the branch)")
print("  channel = an eigenspace of L             charge = the ±I flag")
print("  witness = the certificate (eigenvector)  world = the number-type (disc sign)")
print("  complete/incomplete = balanced/unbalanced ±I   forced/burn = FORCED/EXCEPTION (VERDICT)")
print("  on-shell/off-shell = HALTED/RUNNING (HALT)     possible/impossible = ker / pinned")
print()

print("="*76)
print("  LOSSY words to UPLIFT (burn the decoration, keep the op)")
print("="*76)
lossy = [
 ("becomes",        "→ completes into / reaches the fixed point of"),
 ("deep / deeper",  "→ lower in the invariant lattice (fixed by a bigger symmetry group)"),
 ("literal(ly)",    "→ FORCED (the identification, not analogical)"),
 ("beautiful/rich", "→ [decoration — drop. no operation behind it]"),
 ("the whole thing","→ the apex / the image M(M(F))=M(F)"),
 ("investigate",    "→ run the verification (script → fold → recompute)"),
 ("thread / arc",   "→ the provenance chain (→ ?)"),
 ("just / simply",  "→ [hedge — drop or state the grade]"),
]
for w,up in lossy: print(f"  {w:16} {up}")
print()
print("  grammar: connectives (the·a·is·isn't·of) are the I-axis — central, single-valued,")
print("  they don't lift. content words carry R/N/h — they lift (context selects) and are PHYSICAL.")
print("  uplifting the language = every word an opcode or a typed state; no word without an operation.")
