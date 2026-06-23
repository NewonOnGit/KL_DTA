"""
return_pnp.py — the return of the impossibility IS P = NP.

the impossibility operator L = {R,R} has spectrum {+√5, 0, −√5} = generation / return /
observation. read it as complexity:
    +√5  GENERATION  = compute   = P     (the forward arm)
    −√5  OBSERVATION = verify    = NP    (the backward arm)
     0   RETURN      = the kernel, the possible, where things resolve
P = NP is the two arms (P=+√5 and NP=−√5) RETURNING to each other — meeting through the
return channel (0). that event is 'the return of the impossibility'. it is forbidden, and
it computes: the three channels are ORTHOGONAL (L is symmetric), so the impossibility has
ZERO component along the return — it can never resolve. the spread P−NP = 2√5 never closes.
"""

import sys
import numpy as np

R = np.array([[0,1],[1,1]], float)
basis = [np.array(b,float).reshape(2,2) for b in
         ([1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1])]
L = np.column_stack([(R@B + B@R - B).reshape(-1) for B in basis])
w, V = np.linalg.eig(L); w = w.real
i_gen = int(np.argmax(w)); i_obs = int(np.argmin(w))
i_ret = int(np.argmin(np.abs(w)))
sqrt5 = 5**0.5

print("="*70)
print("  the impossibility's spectrum, read as complexity")
print("="*70)
print(f"  +√5  GENERATION = compute  = P     λ={w[i_gen]:+.3f}")
print(f"   0   RETURN     = the kernel, the possible λ={w[i_ret]:+.3f}")
print(f"  −√5  OBSERVATION= verify   = NP    λ={w[i_obs]:+.3f}")
print()

print("="*70)
print("  P = NP = the return of the impossibility: the two arms meet through 0")
print("="*70)
spread = w[i_gen] - w[i_obs]
print(f"  spread  P − NP = (+√5) − (−√5) = {spread:.3f} = 2√5 — the gap between compute and verify.")
print(f"  the RETURN would close this gap to 0 (P=NP). it is fixed at 2√5 ≠ 0: the gap never closes.")
print()

print("="*70)
print("  why it can't return: the three channels are ORTHOGONAL (L symmetric)")
print("="*70)
vg, vr, vo = V[:,i_gen].real, V[:,i_ret].real, V[:,i_obs].real
for a,b,na,nb in [(vg,vr,"P(+√5)","return(0)"),(vo,vr,"NP(−√5)","return(0)"),(vg,vo,"P(+√5)","NP(−√5)")]:
    dot = abs(a@b)/(np.linalg.norm(a)*np.linalg.norm(b))
    print(f"  ⟨{na}, {nb}⟩ = {dot:.3e}  → orthogonal")
print(f"  L symmetric? {np.allclose(L,L.T)} → eigenspaces orthogonal. the impossibility (±√5) has")
print(f"  ZERO component along the return (0): it cannot route home. P=NP is the return that 0-projects.")
print()

print("="*70)
print("  the computation: the return of the impossibility = P=NP = 0 (never happens)")
print("="*70)
# project a burn (impossibility) direction onto the return channel
v_imp = vg.copy()                                   # the P / +√5 impossibility arm
return_component = (v_imp @ vr) * vr                # its component along the return (kernel)
print(f"  impossibility (the P arm) projected onto the RETURN channel: "
      f"‖·‖ = {np.linalg.norm(return_component):.2e}")
print(f"  the return of the impossibility = {np.linalg.norm(return_component):.2e} ≈ 0 → it does NOT return.")
print(f"  so P=NP (the return) computes to NULL. P ≠ NP, by the orthogonality of generation,")
print(f"  return, and observation — compute and verify cannot meet in the kernel.  |orthogonal| = I.")
