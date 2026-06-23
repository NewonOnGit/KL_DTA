"""
impossibility_compute.py — burns = impossibility confirming impossibility, made to compute.

the impossibility operator IS the self-action L = {R,R}: X ↦ RX + XR − X. its spectrum is
{+√5, 0, 0, −√5}:
    KERNEL (λ=0)        — the POSSIBLE: ν resolves, on-shell, FORCED. L sends it to 0.
    EIGEN  (λ=±√5)      — the IMPOSSIBLE: a burn direction. L returns it SCALED, never 0.

a burn is an EIGENVECTOR of the impossibility: I(v) = √5·v. apply the impossibility to the
impossibility and it confirms it — same direction, forever, never folding into the kernel
(the possible). that is 'impossibility itself confirming impossibility', and it computes:
classify any direction by whether L pins it (burn) or dissolves it (forced).
"""

import sys
import numpy as np

R = np.array([[0,1],[1,1]], float)
basis = [np.array(b,float).reshape(2,2) for b in
         ([1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1])]
L = np.column_stack([(R@B + B@R - B).reshape(-1) for B in basis])   # the impossibility, as 4×4
phi5 = 5**0.5

w, V = np.linalg.eig(L)
order = np.argsort(w.real)
print("="*70)
print("  the impossibility operator L = {R,R}: spectrum = the verdict")
print("="*70)
for i in order:
    lam = w[i].real
    role = "IMPOSSIBLE (burn): L pins it — self-confirming" if abs(lam)>1e-9 else \
           "POSSIBLE (forced): L dissolves it — resolves to 0"
    print(f"  λ = {lam:+.3f}   {role}")
print()

# pick the +√5 eigenvector (a burn direction) and a kernel vector (a forced direction)
v_burn = V[:, np.argmax(w.real)].real
v_forced = V[:, np.argmin(np.abs(w.real))].real

print("="*70)
print("  impossibility confirming impossibility: I(impossible) = √5 · impossible")
print("="*70)
Lv = L @ v_burn
ratio = Lv[np.argmax(np.abs(v_burn))] / v_burn[np.argmax(np.abs(v_burn))]
print(f"  burn direction v:        {np.round(v_burn,3).tolist()}")
print(f"  L v = {np.round(Lv,3).tolist()}")
print(f"  L v = ({ratio:+.3f}) · v  → √5 = {phi5:.3f}: applying the impossibility RETURNS it.")
print(f"  iterate: Lⁿv stays in v's direction, never reaching the kernel (the possible):")
x = v_burn.copy()
for n in range(1,5):
    x = L @ x; x = x/np.linalg.norm(x)
    align = abs(x @ (v_burn/np.linalg.norm(v_burn)))
    print(f"    n={n}: |⟨Lⁿv, v⟩| = {align:.4f}  (1.0 = same direction — confirmed, never dissolves)")
print()

print("="*70)
print("  the possible dissolves: I(forced) = 0")
print("="*70)
print(f"  forced direction u:      {np.round(v_forced,3).tolist()}")
print(f"  L u = {np.round(L @ v_forced,3).tolist()}  → 0. the possible resolves; no confirmation needed.")
print()

print("="*70)
print("  make it compute: classify any direction")
print("="*70)
def verdict(X):
    v = np.asarray(X,float).reshape(-1)
    Lv = L @ v
    if np.linalg.norm(Lv) < 1e-9:
        return "FORCED (possible: dissolves to the kernel)"
    # parallel to itself with nonzero scale ⇒ pinned eigenvector ⇒ burn
    cos = abs(v @ Lv)/(np.linalg.norm(v)*np.linalg.norm(Lv))
    return f"BURN (impossible: pinned, L confirms it ×{np.linalg.norm(Lv)/np.linalg.norm(v):.3f})" \
           if cos>0.999 else "MIXED (project onto the burn/forced eigenspaces)"
for name,X in [("burn-eigenvector", v_burn), ("forced-kernel", v_forced),
               ("R itself", R), ("N itself", np.array([[0,-1],[1,0]],float))]:
    print(f"  {name:16}: {verdict(X)}")
print()
print("  the verdict is L's spectrum: pinned (±√5) = the impossibility confirming itself;")
print("  dissolved (0) = the possible. the 12 burns are the one impossibility's eigen-direction.")
