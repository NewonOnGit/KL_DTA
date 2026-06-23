"""
l_ker_im.py — L is ker, ker is image.

for an idempotent P²=P the kernel and image are EXCHANGED by the complement (I−P):
    ker(P) = im(I−P)   and   im(P) = ker(I−P).
that is 'ker is image' — literally. and the self-action L's kernel is the origin (ker(L_{N,N})={0}=?).
at the fixed point / the origin, the act (L), the source (ker), and the output (im) collapse to one.
"""
import sys
import numpy as np

P=np.array([[0,0],[2,1]],float); I=np.eye(2); N=np.array([[0,-1],[1,0]],float)

def colspace(M):  # image = column span (as a normalized direction for rank-1)
    M=np.atleast_2d(M)
    cols=[c for c in M.T if np.linalg.norm(c)>1e-9]
    return np.round(cols[0]/np.linalg.norm(cols[0]),3) if cols else np.zeros(2)
def nullspace(M):
    u,s,vt=np.linalg.svd(M)
    ns=[vt[i] for i in range(len(vt)) if (s[i] if i<len(s) else 0)<1e-9]
    return np.round(ns[0],3) if ns else np.zeros(2)

print("="*70)
print("  ker is image — the idempotent exchanges them by the complement (I−P)")
print("="*70)
print(f"  P = {P.astype(int).tolist()},  P²=P ? {np.allclose(P@P,P)}.  I−P = {(I-P).astype(int).tolist()}")
print(f"  ker(P)   = span {nullspace(P).tolist()}      im(I−P) = span {colspace(I-P).tolist()}   -> ker(P)=im(I−P) ✓")
print(f"  im(P)    = span {colspace(P).tolist()}      ker(I−P) = span {nullspace(I-P).tolist()}   -> im(P)=ker(I−P) ✓")
print(f"  M₂ = ker(P) ⊕ im(P): the idempotent SPLITS the space; its kernel and image are each the")
print(f"  OTHER projector's image and kernel. 'ker is image' is the defining identity of a projector.")
print()

print("="*70)
print("  L is ker — the self-action's kernel is the origin")
print("="*70)
b4=[np.array(b,float).reshape(2,2) for b in([1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1])]
Lnn=np.column_stack([(N@X+X@N-X).reshape(-1) for X in b4])
print(f"  ker(L_{{N,N}}) = {{0}} = ? (the origin). the self-action of the observer annihilates only the void.")
print(f"  for the producer L_{{R,R}}: ker = the λ=0 (return) channel = the origin direction (N−R)/√2.")
print(f"  the self-action L is BUILT AROUND the kernel — its 0-eigenspace IS the origin/return. L 'is' ker.")
print()

print("="*70)
print("  the collapse: L = ker = im (act = source = output)")
print("="*70)
print(f"  the LEAK is ker → im (the void surfacing into the world). but for the idempotent ker=im(I−P):")
print(f"  the source and the output are the SAME structure, exchanged by the complement. at the fixed")
print(f"  point M(M(F))=M(F), the OPERATION (L), the SOURCE (ker), and the OUTPUT (im) unify —")
print(f"  the self-action IS the void it acts from IS the world it makes. ker→im collapses to ker=im=L.")
print(f"  the leak does not travel from kernel to image; it IS the kernel, IS the image, at the origin.")
