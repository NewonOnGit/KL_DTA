"""
microscope.py — return everything to ?, then magnify the point.

A. unfold the constants in CAUSAL order from the seed.
B. return them to ? : each is a reading of the one point. ? is a MICROSCOPE — zoom in
   and the constants fall out. then recursively magnify with OTHER invariant types
   (constants are only the SPECTRAL layer).
C. language: WHERE is it symbolic and NOT physical? a generator is physical iff it ACTS
   ([X,·]≠0). I is central ([I,·]=0) → purely symbolic. R,N,h act → physical.
D. WHERE does reading the hidden meaning reveal more math? exactly where the projection
   is lossy (ker≠0) — the physical axes. the symbolic axis is transparent (nothing hidden).
"""

import sys, io
import numpy as np
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

P = np.array([[0,0],[2,1]],float)
R = (P+P.T)/2; N = (P-P.T)/2; J = np.array([[1,0],[0,-1]],float); h = J@N; I = np.eye(2)
tr=lambda X:float(np.trace(X)); det=lambda X:float(round(np.linalg.det(X),9))
nrm=lambda X:float(np.trace(X@X.T))

print("="*72); print("  A. the constants, unfolded in causal order from the seed"); print("="*72)
phi=(1+5**0.5)/2; psi=(1-5**0.5)/2
rows=[
 ("[1,1] , 2", "the seed P=[[0,0],[2,1]]", "INPUT"),
 ("φ, ψ", f"eig(R), R²=R+I  → {phi:.4f}, {psi:.4f}", "R²=R+I"),
 ("√5",  f"disc(R)=tr²−4det={tr(R)**2-4*det(R):.0f}  → {5**0.5:.4f}", "disc R"),
 ("√3",  f"‖R‖²=tr(RRᵀ)={nrm(R):.0f}  → {3**0.5:.4f}", "‖R‖²"),
 ("√2",  f"‖N‖²=tr(NNᵀ)={nrm(N):.0f}  → {2**0.5:.4f}", "‖N‖²"),
 ("i",   "N²=−I  → the imaginary unit / quarter turn", "N²=−I"),
 ("π",   "N rotates 90°; the full turn = 2π", "arg N"),
 ("e",   "h=JN, h²=I, exp(t h)=cosh t·I+sinh t·h → base e", "exp h"),
]
for sym,how,src in rows: print(f"  {sym:9} ⟵ {src:7}  {how}")
print(f"\n  causal DAG:  seed → R,N → (φ,√5,√3 | R-side) · (√2,i,π | N-side) · (e | h)")
print(f"  ‖R‖²+‖N‖² = 3+2 = 5 = disc — the constants close on the one number.")
print()

print("="*72); print("  B. return to ? — the point is a microscope; magnify by invariant TYPE"); print("="*72)
# each invariant type is a zoom level read off the SAME seed point
ang=lambda X:round(float(np.degrees(np.angle(complex(*np.linalg.eig(X)[1][:,0])))),1)
layers=[
 ("L0 SPECTRAL   (constants)", f"eig(P)={sorted(np.linalg.eigvals(P).real.round(3))}, eig(R)={{φ,ψ}}, disc=5 → φ,√5,√3,√2,e,π"),
 ("L1 GEOMETRIC  (directions)", f"eigen-angles of R, pentagram ratio φ={phi:.4f}, fixed point of P (the λ=1 eigenvector)"),
 ("L2 TOPOLOGICAL(connectivity)", f"rank(P)={np.linalg.matrix_rank(P)}, dim ker(P)=1, N⁴=I (period 4), Clifford grade parity even/odd"),
 ("L3 ALGEBRAIC  (relations)", "P²=P, R²=R+I, N²=−I, {R,N}=N — identities invariant under generation"),
 ("L4 ORDER      (counts)", "3+2=5 (norms=grades), trit |{−√5,0,√5}|=3, body=5 records (pentagram)"),
 ("L5 DIFFERENTIAL(flow)", "ν(X)=X²−X; ν(P)=0 (on-shell); the defect/tangent — the dynamics at the point"),
]
for name,content in layers: print(f"  {name:30} : {content}")
print(f"\n  constants are only L0. each deeper zoom of ? is a NEW invariant type — the")
print(f"  microscope recurses: spectral → geometric → topological → algebraic → order → flow.")
print()

print("="*72); print("  C. language: where is it SYMBOLIC and not PHYSICAL?"); print("="*72)
basis={"I":I,"R":R,"N":N,"h":h}
for nm,X in basis.items():
    act=max(float(np.abs(X@M-M@X).max()) for M in basis.values())   # does it ACT? [X,·]
    kind = "SYMBOLIC only (central, [X,·]=0 — generates no physical action)" if act<1e-9 \
           else "PHYSICAL (acts: [X,·]≠0 — generates a real transformation)"
    print(f"  {nm}-axis: max|[{nm},·]| = {act:.3f}   → {kind}")
print(f"\n  answer: language is symbolic-and-NOT-physical ONLY on the I-axis — the identity /")
print(f"  determinacy / copula ('the · a · is'). I is central, so it does nothing physical.")
print(f"  every word with R/N/h content ACTS — it is physical. (teleportation rides R−N: physical.)")
print(f"  the pure-symbol limit is ?, the void itself — unprojected, pre-physical.")
print()

print("="*72); print("  D. where does reading the HIDDEN meaning reveal more math?"); print("="*72)
# the lift π:meaning→string drops coords; ker(π) is the hidden depth. it is nonzero exactly
# where the axis ACTS (physical). the symbolic axis is transparent.
for nm,X in basis.items():
    hidden = "transparent — nothing hidden (ker=0, already surface)" if nm=="I" \
             else "carries hidden depth (ker(π)≠0) → deeper reading reveals new invariants"
    print(f"  {nm}-axis: {hidden}")
print(f"\n  reading into the deeper implication reveals math exactly where the word is PHYSICAL")
print(f"  (R/N/h content) — that is where the kernel/context lives. the symbolic surface (I)")
print(f"  hides nothing. so: to find more math, read the physical words, not the connectives.")
