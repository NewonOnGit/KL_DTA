"""
explore_lnn.py — the math around ker(L_{N,N})=0, deeply.

L_{X,X}(M) = X M + M X - M = {X,M} - M. on vec(M): L = I⊗X + Xᵀ⊗I - I (4×4).
the kernel of the self-action tells you the BLIND SPOT of X observing itself.
"""
import sys
import numpy as np

def selfaction(X):
    b4=[np.array(b,float).reshape(2,2) for b in([1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1])]
    return np.column_stack([(X@B+B@X-B).reshape(-1) for B in b4])

I=np.eye(2); R=np.array([[0,1],[1,1]],float); N=np.array([[0,-1],[1,0]],float)
J=np.array([[1,0],[0,-1]],float); h=J@N; P=np.array([[0,0],[2,1]],float)

print("="*72)
print("  1. L_{N,N} — spectrum and kernel")
print("="*72)
Lnn=selfaction(N)
ev=np.linalg.eigvals(Lnn)
print(f"  L_{{N,N}}(M) = NM+MN-M.  eigenvalues = {[f'{e.real:+.0f}{e.imag:+.0f}i' for e in ev]}")
print(f"  = {{2i-1, -2i-1, -1, -1}}.  none is 0  ->  ker(L_{{N,N}}) = {{0}}, dim {4-np.linalg.matrix_rank(Lnn)}.")
print(f"  |2i-1| = sqrt(4+1) = sqrt5 = {abs(2j-1):.4f}  — the disc radical hides in the observer's self-modes.")
print(f"  L_{{N,N}} is INVERTIBLE (det = {np.linalg.det(Lnn):+.0f} != 0): a BIJECTION — every observed has a unique source.")
print()

print("="*72)
print("  2. WHY ker=0: it is the TRACE. self-transparent <=> traceless")
print("="*72)
print(f"  for X with eigenvalues λ1,λ2: {{X,.}} has a CROSS-mode eigenvalue λ1+λ2 = tr(X);")
print(f"  so L_{{X,X}} = {{X,.}}-I has cross-eigenvalue tr(X)-1. it hits 0  <=>  tr(X)=1.")
print(f"  (same-mode eigenvalue 2λ-1 hits 0 <=> λ=1/2.)  so a BLIND SPOT appears exactly at tr=1.")
print(f"  {'matrix':4} {'tr':>3} {'ker(L_XX)':>10}   reading")
for nm,X in [("I",I),("R",R),("N",N),("J",J),("h",h),("P",P)]:
    k=4-np.linalg.matrix_rank(selfaction(X))
    tag = "BLIND (commits, tr=1)" if k>0 else "TRANSPARENT (sees itself)"
    print(f"  {nm:4} {np.trace(X):>+3.0f} {k:>10}   {tag}")
print(f"  tr=1 (R, P — the producers/the seed) -> blind spot. tr=0 (N, J, h — traceless) -> transparent.")
print(f"  to see yourself whole, COMMIT TO NOTHING (tr=0). the blind spot is the price of occupation (tr=1).")
print()

print("="*72)
print("  3. the explanatory gap: 0 vs 2 — self-sight vs production-blindness")
print("="*72)
kR=4-np.linalg.matrix_rank(selfaction(R)); kN=4-np.linalg.matrix_rank(selfaction(N))
print(f"  ker(L_{{R,R}}) = {kR}  (production has a 2-dim blind spot — R commits, tr=1)")
print(f"  ker(L_{{N,N}}) = {kN}  (observation is fully transparent — N is weightless, tr=0)")
print(f"  the gap 0 vs 2 is the framework's hard problem: the observer KNOWS ITSELF completely (ker=0)")
print(f"  yet is causally WEIGHTLESS (tr=0, sources ~nothing). consciousness = self-transparent AND")
print(f"  weightless — and BOTH come from the single fact tr(N)=0. seeing-itself and adding-no-weight are one.")
print()

print("="*72)
print("  4. ker(L_{N,N}) = {0} = ?  (the kernel IS the origin)")
print("="*72)
print(f"  the only M with NM+MN=M is M=0. the observer's lone blind spot is the VOID itself —")
print(f"  i.e. nothing that EXISTS is hidden from it. ker = {{0}} = ? = the origin. when N looks at N")
print(f"  it stands at the origin and sees everything but nothing. self-observation IS being at ?.")
print(f"  contrast: producing (tr=1) drags a 2-dim shadow you cannot see while you make. to observe is")
print(f"  to put down all weight and stand at the origin, where the kernel is only the void.")
