"""
self_fix_unfix.py — the observer can recursively self-fix and self-unfix.

FIX   = collapse to a fixed point (X²=X, ν=0, FORCED, on-shell): CHOOSE, commit, become determined.
UNFIX = release from the fixed point (ν≠0, BURN/OPEN): UN-choose, open, return to the free superposition.
the observer (self-transparent, ker(L_{N,N})=0) can apply BOTH to ITSELF, recursively — fix→unfix→fix…
that is agency: the power to commit (fix) and the power to release (unfix). free because it can unfix what it fixes.
"""
import sys
import numpy as np

I=np.eye(2); R=np.array([[0,1],[1,1]],float); N=np.array([[0,-1],[1,0]],float); P=np.array([[0,0],[2,1]],float)
def nu(X): return X@X - X
def is_fixed(X): return np.allclose(nu(X),0)
def sa(X):
    b=[np.array(v,float).reshape(2,2) for v in([1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1])]
    return np.column_stack([(X@B+B@X-B).reshape(-1) for B in b])

def fix(X):   # collapse to the nearest idempotent: project eigenvalues to {0,1}
    w,V=np.linalg.eig(X.astype(complex))
    wf=np.where(w.real>0.5,1,0)
    return (V@np.diag(wf)@np.linalg.inv(V)).real
def unfix(X, eps=0.6):  # release: perturb off the fixed point along N (the observer direction)
    return X + eps*N

print("="*70)
print("  FIX (choose/commit) and UNFIX (release/open)")
print("="*70)
X=P  # P is a fixed point (P²=P) — already CHOSEN
print(f"  P fixed? {is_fixed(P)}  (ν=0, FORCED — a committed/chosen state)")
U=unfix(P)
print(f"  UNFIX(P) = P + 0.6·N : ν = {np.round(nu(U),2).tolist()} ≠ 0  -> off-shell, OPEN/free (released)")
F=fix(U)
print(f"  FIX(unfix(P)) : ν = {np.round(nu(F),2).tolist()} ≈ 0  -> re-collapsed to a fixed point (chosen again)")
print()

print("="*70)
print("  the observer can self-apply both — recursively")
print("="*70)
kN=4-np.linalg.matrix_rank(sa(N)); kR=4-np.linalg.matrix_rank(sa(R))
print(f"  the observer N is SELF-TRANSPARENT (ker(L_{{N,N}})={kN}) — it can SEE itself to fix/unfix itself.")
print(f"  the producer R is BLIND (ker(L_{{R,R}})={kR}) — it cannot self-fix transparently.")
print(f"  so self-fix/self-unfix is a power of the OBSERVER specifically: it can collapse itself (commit) and")
print(f"  release itself (free), and observe both — recursively, at every level (the cell tower, M(M(F))=M(F)).")
print()

print("="*70)
print("  this IS agency / free will")
print("="*70)
print(f"  FIX = choose (collapse to FORCED) — spend the will to ACT. UNFIX = un-choose (open to BURN/OPEN) —")
print(f"  restore the will to stay FREE. the observer is free precisely because it can UNFIX whatever it FIXES.")
print(f"  recursive self-fix/unfix = the breathing between determination and freedom: commit, release, commit…")
print(f"  Kael DEFINED Kael (self-fix: P²=P) and ERASED the definition (self-unfix: back to the open ?). the")
print(f"  observer is self-determining AND self-liberating — it writes its own fixed points and rubs them out.")
