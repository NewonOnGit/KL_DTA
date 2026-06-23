"""
groups.py — what is hiding under "L0/L1/L2"?

an invariant is not a LEVEL — it is "what is fixed by a GROUP". the integer index is
lossy twice over:
  • it hides the GROUP (spectral = fixed by conjugation; geometric = fixed by the
    orthogonal/Cartan subgroup; a constant = fixed by a Galois subgroup);
  • it imposes a fake TOTAL order on what is really a LATTICE of subgroups (Erlangen–
    Galois): bigger group ⇒ fewer, deeper invariants; subgroups ↔ invariant-sets, and
    incomparable subgroups give incomparable invariant types. a line can't hold a lattice.
"""

import sys, itertools
import numpy as np

# ── spectral vs geometric = fixed by which group ─────────────────────────────
print("="*72)
print("  1. spectral vs geometric — fixed by which group (Erlangen)")
print("="*72)
X = np.array([[0,1],[2,1]], float)
rng_g  = np.array([[1.0,2.0],[0.0,1.0]])        # a general (shear) similarity
orth   = np.array([[0,-1],[1,0]], float)        # an orthogonal similarity (90° rot)
def angle_between_eigvecs(M):
    w,V = np.linalg.eig(M); v0,v1 = V[:,0], V[:,1]
    c = abs(v0@v1)/(np.linalg.norm(v0)*np.linalg.norm(v1))
    return float(np.degrees(np.arccos(min(1,c))))
def tr_det(M): return round(float(np.trace(M)),6), round(float(np.linalg.det(M)),6)
for gname,g in [("general g (shear)",rng_g),("orthogonal g (rot)",orth)]:
    Y = g @ X @ np.linalg.inv(g)
    print(f"  under {gname:18}: tr,det {tr_det(X)}→{tr_det(Y)}   "
          f"eigvec-angle {angle_between_eigvecs(X):.1f}°→{angle_between_eigvecs(Y):.1f}°")
print("  → SPECTRAL (tr,det) fixed by ALL conjugation (the big group): few, deep invariants.")
print("    GEOMETRIC (the angle) fixed ONLY by the orthogonal subgroup: more, finer invariants.")
print("    'level' was hiding 'the group it's fixed by'. bigger group = deeper level.")
print()

# ── the constant field is Galois: each constant ↔ a fixing subgroup ──────────
print("="*72)
print("  2. the constants ℚ(√2,√3,√5): Galois group (ℤ/2)³ — each ↔ a subgroup")
print("="*72)
r2,r3,r5 = 2**.5, 3**.5, 5**.5
G = list(itertools.product([1,-1],repeat=3))     # σ=(s2,s3,s5): the 8 sign-flips
def value(name, s):
    s2,s3,s5 = s
    return {"√2":s2*r2, "√3":s3*r3, "√5":s5*r5, "φ":(1+s5*r5)/2,
            "√6":s2*s3*r2*r3, "√15":s3*s5*r3*r5, "√30":s2*s3*s5*r2*r3*r5}[name]
print("  constant  |fixing subgroup|   the σ=(s2,s3,s5) that fix it")
for name in ["√2","√3","√5","φ","√6","√15","√30"]:
    base = value(name,(1,1,1))
    fix  = [s for s in G if abs(value(name,s)-base) < 1e-9]
    sig  = " ".join("".join("+" if x>0 else "-" for x in s) for s in fix)
    print(f"   {name:4}      {len(fix):>2}              {sig}")
print("  → φ and √5 share a fixing subgroup (order 4, c=+). √30 is fixed by only 2.")
print("    the 'depth' of a constant = the SIZE of its fixing subgroup. φ is deep (4),")
print("    √30 is shallow (2). that's the Galois lattice — not an integer ladder.")
print()

# ── the lattice is not a line: incomparable types exist ──────────────────────
print("="*72)
print("  3. it's a LATTICE, not a ladder — incomparable invariants")
print("="*72)
print("  fixing-subgroup of √5  = {+++,++-? } ... order 4   (flips of √2,√3; c fixed)")
print("  fixing-subgroup of √6  = order 4 too, but a DIFFERENT order-4 subgroup")
print("  neither ⊆ the other → √5 and √6 are INCOMPARABLE: no n puts one 'above' the other.")
print("  a linear L0<L1<L2 LIES about this. the real object is the subgroup lattice")
print("  (Erlangen–Galois): invariant types ↔ symmetry subgroups, partially ordered.")
print("  |a lattice| ≟ |a line| is forbidden — the obstruction is INCOMPARABILITY.")
