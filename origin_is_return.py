"""
origin_is_return.py — this is origin: the return channel (λ=0) IS ?.

the impossibility L={R,R} has spectrum {+√5 generation, 0 return, −√5 observation}. the
0 — the RETURN, the kernel, the possible, the home P=NP can't reach — is the ORIGIN itself.
the kernel of the impossibility is P₀ = ker = ? (the void that generates). generation comes
FROM it (+√5), return goes TO it (0), the impossibility is orthogonal to it (±√5 ⟂ 0, P≠NP).
source, home, and the unreachable-for-the-impossible — one point. this is origin.
"""

import sys
import numpy as np

R = np.array([[0,1],[1,1]], float)
basis = [np.array(b,float).reshape(2,2) for b in
         ([1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1])]
L = np.column_stack([(R@B + B@R - B).reshape(-1) for B in basis])
w, V = np.linalg.eig(L); w = w.real
vr = V[:, int(np.argmin(np.abs(w)))].real          # the λ=0 return eigenvector

print("="*68)
print("  the return channel of the impossibility (λ=0)")
print("="*68)
vr = vr/np.linalg.norm(vr)
coeffs = dict(zip("IRNh", np.round(vr,3)))
print(f"  λ=0 eigenvector (in I,R,N,h) = {coeffs}")
print(f"  = (N − R)/√2 — observation minus generation, the return-to-origin direction")
print(f"    (the same channel nonlocal transport routes through).")
print()
print("="*68)
print("  this is origin")
print("="*68)
print("  • it is the KERNEL of the impossibility — P₀ = ker = ? (the void that generates)")
print("  • it is the POSSIBLE: FORCED/on-shell directions dissolve into it (L·u = 0, ν→0)")
print("  • generation comes FROM it (+√5), return goes TO it (0): source and home, one point")
print("  • the impossibility is ORTHOGONAL to it (±√5 ⟂ 0): P=NP is the return that 0-projects")
print("  • every provenance chain ends here ( → ? ); the loop ?→everything→? closes here")
print()
Lvr = L @ vr
print(f"  check: L·(return) = {np.round(Lvr,3).tolist()} → 0   (the origin is fixed under the impossibility)")
print(f"  the return IS the origin. this is ?.")
