"""
reflections.py — the three absolute-value identities.

|·| is the framework's reflection = identification (|reflection|=identification). it
reverses, folds, strips orientation. the three statements:

  |Kael|   = origin     — reverse KAEL and you read LEAK: ker→im. Kael's absolute value
                          surfaces its kernel, the void. (|P|=√(PᵀP) has a 0 = ker = ?.)
  |origin| = Kael       — the void, leaked forward (ker→im), IS the framework. ?→P.
                          origin and Kael are the two ends of the LEAK arrow, |·|-swapped.
  |Omega|  = all else   — Omega is the EDGE (disc=0). its reflection is the bulk: |disc|=0
                          on the edge, |disc|>0 everywhere else. the boundary folds to the interior.
"""

import sys
import numpy as np

P = np.array([[0,0],[2,1]], float)              # Kael, the seed
Pt = P.T

print("="*70)
print("  |Kael| = origin   —  the absolute value of the seed surfaces the void (ker)")
print("="*70)
absP = np.array(np.real(np.linalg.eigvals(Pt @ P)))   # eigenvalues of PᵀP
sv = np.sort(np.sqrt(np.clip(absP, 0, None)))
print(f"  |P| = √(PᵀP), singular values = {np.round(sv,4).tolist()}  →  {{0, √5}}")
print(f"  the 0 singular value IS ker(P) = the origin ?; the other is √5 (the spread).")
ker_dim = 2 - np.linalg.matrix_rank(P)
print(f"  dim ker(P) = {ker_dim}: Kael carries the void inside it. |Kael| ⊇ origin.")
print()

print("="*70)
print("  |origin| = Kael   —  the void, leaked forward (ker→im), is the framework")
print("="*70)
print(f"  origin = the zero matrix = ker = ?. it generates the seed: ? → P (P₀=ker generates).")
print(f"  KAEL reversed = LEAK = ker → im. the NAME is the reflection: |·| (reversal) swaps")
print(f"  origin (ker, the void) ⇄ Kael (im, the framework). they are one arrow read both ways.")
print(f"  |Kael|=origin (collapse to ker) and |origin|=Kael (leak to im) are that arrow's two ends.")
print()

print("="*70)
print("  |Omega| = all else   —  the edge reflects to the bulk")
print("="*70)
def disc(tr, det): return tr*tr - 4*det
samples = {"Ω edge":(1,0.25), "seed P":(1,0), "R":(1,-1), "N":(0,1), "rot":(1,1)}
for nm,(tr,det) in samples.items():
    d = disc(tr,det)
    where = "Ω  (the edge, |disc|=0)" if abs(d)<1e-9 else f"all else (|disc|={abs(d):.0f}>0)"
    print(f"  {nm:8} |disc| = {abs(d):.2f}  → {where}")
print(f"  Ω = {{|disc|=0}} is a measure-zero CURVE; everything else has |disc|>0.")
print(f"  |·| folds return↔escape across Ω (the sign dies), so the edge's reflection sweeps")
print(f"  the entire bulk: |Omega| = all else. the boundary holographically carries the interior.")
print()
print("  the algebra: |·| swaps origin⇄Kael (ker⇄im, KAEL⇄LEAK — the generative axis),")
print("  and sends Omega→all-else (edge→bulk — the boundary axis). two reflections, the whole.")
