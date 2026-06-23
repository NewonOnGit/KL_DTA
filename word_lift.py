"""
word_lift.py — where language LIFTS, and how context selects meaning.

The claim, made mechanical:
  a WORD = a string applied to an underlying meaning. the meaning is a point in the
  carrier  W = a·I + b·R + c·N + d·h.  the four coordinates ARE the simultaneous
  meanings — the basis is the axes of reading:
       I  determinacy / this           (index)
       R  symbolic / production (φ)     (the algebra)
       N  observation / phase (i,π)     (the mirror)
       h  mediation / flow (e)          (the dynamics / physical)
  these are MANUALLY TYPED into the word (the authored part). after that the math runs.

  the observer applies string→meaning. that map is a LIFT:
       π : meaning ↦ string     forgets the coordinates (easy, lossy)
       lift : string ↦ meaning  needs CONTEXT to choose within the fiber (hard)
  ker(π) = the coordinate spread = the ambiguity = exactly what context must supply.
  CONTEXT is a matrix C (the neighbours); the active reading is the axis of W whose
  meaning-direction best overlaps C — argmax ⟨basis_axis, C⟩. let the math do its thing.

  WHERE it lifts: a word lifts exactly where its meaning has >1 nonzero coordinate.
  one coordinate = no lift (the connectives, the primitives — single-valued projectors).
  many coordinates = polysemy = the lift, resolved by context.
"""

import sys, io
import numpy as np
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

I = np.eye(2)
R = np.array([[0, 1], [1, 1]], float)
N = np.array([[0, -1], [1, 0]], float)
h = np.array([[0, 1], [-1, 0]], float) @ N  # h = JN ; J=diag(1,-1)
J = np.array([[1, 0], [0, -1]], float); h = J @ N
BASIS = {"I": I, "R": R, "N": N, "h": h}
AXIS = {"I": "determinacy/this", "R": "symbolic/production(φ)",
        "N": "observation/phase(i,π)", "h": "mediation/flow(e,physical)"}

def ip(A, B):                      # context overlap = trace inner product
    return float(np.trace(A.T @ B))

def meaning(word):                 # build the meaning matrix from coords
    return sum(c * BASIS[a] for a, c in word["coords"].items())

def polysemy(word):                # WHERE/how much it lifts = nonzero coordinates
    return [a for a, c in word["coords"].items() if abs(c) > 1e-9]

def lift(word, context):           # string + context -> the active reading
    axes = polysemy(word)
    scores = {a: ip(BASIS[a], context) for a in axes}
    active = max(scores, key=lambda a: scores[a])
    return active, word["readings"][active], scores

# one polysemous content word, three meanings manually typed in:
fold = {
    "string": "fold",
    "coords": {"R": 1.0, "N": 1.0, "h": 1.0},          # lives on three axes — it LIFTS
    "readings": {
        "R": "X² — squaring, the master-equation operation (symbolic)",
        "N": "reflection — the pentagram stroke, |reflection| (geometric)",
        "h": "propagation — the action, the field folding through space (physical)",
    },
}
# a connective for contrast — single coordinate, does NOT lift:
is_ = {"string": "is", "coords": {"I": 1.0},
       "readings": {"I": "the copula / the fixed point X=fold(X)"}}

# three contexts (neighbour matrices), each weighted toward one axis:
CONTEXTS = {
    "an algebra clause":      2*R + 0.2*N + 0.2*h,
    "a mirror/observer clause": 0.2*R + 2*N + 0.2*h,
    "a field/space clause":   0.2*R + 0.2*N + 2*h,
}

print("=" * 74)
print("  the word 'fold' — meaning typed across 3 axes; π keeps only the string")
print("=" * 74)
print(f"  string : '{fold['string']}'   coords {fold['coords']}")
print(f"  π(fold) = '{fold['string']}'  (drops all coordinates — lossy)")
print(f"  ker(π)  = the 3 coordinates = the ambiguity context must resolve")
print(f"  polysemy (where it lifts) = {polysemy(fold)}   →  3-fold lift")
print()

print("=" * 74)
print("  the lift: same string, context selects the meaning")
print("=" * 74)
for cname, C in CONTEXTS.items():
    active, reading, scores = lift(fold, C)
    sc = {a: round(s, 2) for a, s in scores.items()}
    print(f"  in {cname:24} → axis {active}  «{reading}»")
    print(f"      overlaps {sc}")
print()

print("=" * 74)
print("  the contrast: 'is' does NOT lift (one coordinate, single-valued)")
print("=" * 74)
for cname, C in CONTEXTS.items():
    active, reading, _ = lift(is_, C)
    print(f"  in {cname:24} → axis {active}  «{reading}»  (same in every context)")
print()

print("=" * 74)
print("  the structure")
print("=" * 74)
print("  • word = string (address) ⊕ meaning-coords (spectral content) — the SAME")
print("    eigendecomposition the records use; a word IS a record.")
print("  • author the coords + the per-axis readings (manual); selection is computed.")
print("  • π drops the coords (string is the lossy image); the LIFT restores them, and")
print("    CONTEXT = ker(π) supplied = the data that says which reading is on-shell.")
print("  • lift degree = #nonzero coords = polysemy. connectives have degree 1 (no lift);")
print("    content words have degree >1 (they lift). that is WHERE language lifts.")
print("  • |reflection| = identification: string and meaning become one only IN CONTEXT.")
