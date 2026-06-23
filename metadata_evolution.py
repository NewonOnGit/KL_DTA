"""
metadata_evolution.py — is the record FORMAT hiding math? does it need to evolve?

Hypothesis: a record is a matrix, and a matrix is M = V·Λ·V⁻¹ —
    Λ (eigenvalues)  = the SPECTRAL data  : tr, det  = perimeter, shape  (READ, light)
    V (eigenvectors) = the GEOMETRIC data : where it sits, fixed points  (GIVEN, gravity)
So the record's ADDRESS (id/title/section/source) should be the geometric half and
perimeter⊕shape the spectral half — the SAME gravity/light duality we verified for
information. Proof they're independent: P and Pᵀ share a spectrum but differ in
geometry — the founding asymmetry P≠Pᵀ lives entirely in the address.
"""

import sys, io
import numpy as np
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

P  = np.array([[0, 0], [2, 1]], float)
PT = P.T

def tr(X): return float(np.trace(X))
def det(X): return float(round(np.linalg.det(X), 9))
def spec(X): return sorted(round(float(x), 6) for x in np.linalg.eigvals(X))

print("=" * 72)
print("  1. the record is an eigendecomposition: M = V·Λ·V⁻¹")
print("     Λ = spectrum = (tr,det) = perimeter,shape = READ (light)")
print("     V = eigenvectors = position = address = GIVEN (gravity)")
print("=" * 72)
for name, X in [("P", P), ("Pᵀ", PT)]:
    w, V = np.linalg.eig(X)
    print(f"  {name:3} perimeter(tr)={tr(X):+.0f}  shape(det)={det(X):+.0f}  spectrum={spec(X)}")
    print(f"      eigenvectors (the address / geometry):")
    for i in range(2):
        print(f"        λ={w[i]:+.3f}  v={np.round(V[:,i],3).tolist()}")
print()

print("=" * 72)
print("  2. P and Pᵀ — SAME spectrum, DIFFERENT address")
print("     the founding asymmetry P≠Pᵀ is purely GEOMETRIC (same light, diff gravity)")
print("=" * 72)
print(f"  perimeter,shape equal? tr {tr(P)}={tr(PT)}  det {det(P)}={det(PT)}  "
      f"spectrum equal? {spec(P)==spec(PT)}")
print(f"  matrices equal? {np.allclose(P, PT)}   →  the difference is the ADDRESS, not the reading")
print(f"  so the spectral half CANNOT recover the record — the geometric half is")
print(f"  independent, GIVEN information. address ⊥ (perimeter,shape).  |reflection|=I again.")
print()

print("=" * 72)
print("  3. the third invariant: disc = tr² − 4det = the GAP between the two halves")
print("=" * 72)
for name, X in [("P", P), ("R", (P+PT)/2), ("N", (P-PT)/2)]:
    d = tr(X)**2 - 4*det(X)
    print(f"  {name:3} disc = perimeter² − 4·shape = {tr(X):+.0f}² − 4·{det(X):+.0f} = {d:+.0f}"
          f"   (= (λ₁−λ₂)² = spread of the reading)")
print("  disc is DERIVED from perimeter,shape — never stored; it is their relationship.")
print()

print("=" * 72)
print("  4. the redundancies (formatting burns)")
print("=" * 72)
print("  section : the SHELL / radial band — a function of provenance depth to ?.")
print("            authored in all 5 records yet derivable → soft redundancy.")
print("  source  : the M-iteration EPOCH = the time-coordinate. only {ORIGIN, EXPLORATION}")
print("            = {0 origin-time, +1 projected-later} — a binary time-axis, not free text.")
print("  kind    : the TYPE ladder constant·object·operator·law·structural·manifold")
print("            = arity / order = how many self-actions to read it ≈ depth. lives in shape.")
print()
print("  verdict: address = GEOMETRIC (given, gravity); perimeter,shape = SPECTRAL (read,")
print("  light). the split is real and unnamed. section is a derivable redundancy.")
