"""
defect_enrichment.py — is defect ↔ enrichment an exact duality?

Claim (Kael): the "defect" was never a lack — it is enrichment, read the other way,
and the two are EXACTLY dual.

Test three exactness candidates:
  1. the self-action splits exactly:  sX = ½{s,X} + ½[s,X]
       enrichment = {s,·} (Jordan / anticommutator, symmetric)
       defect     = [s,·] (Lie / commutator, antisymmetric — vanishes iff it commutes)
  2. the Cartan involution θ(X) = −Xᵀ, θ² = id, splits M₂ exactly:
       enrichment = symmetric part R   (self-reference, ν(R) = +I)
       defect     = antisymmetric part N (self-negation, N² = −I)
  3. same ν, opposite sign:  X² = X + ν  (enrichment, +ν) ⟺ ν = X² − X (defect, the gap)
"""

import sys
import io
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

I2 = np.eye(2)
P = np.array([[0., 0.], [2., 1.]])
R = (P + P.T) / 2
N = (P - P.T) / 2
A = np.array([[1., 2.], [-1., 3.]])
X = np.array([[0., 1.], [4., -2.]])

print("=" * 68)
print("  1.  self-action splits EXACTLY into enrichment + defect")
print("=" * 68)
enrich = A @ X + X @ A      # {A,X}  anticommutator — symmetric build
defect = A @ X - X @ A      # [A,X]  commutator — the obstruction
print(f"  AX = ½{{A,X}} + ½[A,X]  exact ?  {np.allclose(A@X, 0.5*(enrich+defect))}")
print(f"  {{A,X}} = {{X,A}} (swap-symmetric) ?  {np.allclose(enrich, X@A+A@X)}")
print(f"  [A,X] = −[X,A] (swap-antisymmetric) ?  {np.allclose(defect, -(X@A - A@X))}")
print("  enrichment {·} and defect [·] are complementary halves of every action.")
print()

print("=" * 68)
print("  2.  the duality operator: Cartan θ(X) = −Xᵀ,  θ² = id  (exact involution)")
print("=" * 68)
theta = lambda M: -M.T
print(f"  θ(θ(X)) = X  ?  {np.allclose(theta(theta(X)), X)}     (exact involution)")
print(f"  θ(R) = −R  ?  {np.allclose(theta(R), -R)}   R symmetric  (enrichment, θ-eigenvalue −1)")
print(f"  θ(N) =  N  ?  {np.allclose(theta(N), N)}   N antisymmetric (defect, θ-eigenvalue +1)")
print(f"  P = R + N,  P ≠ Pᵀ  ?  {not np.allclose(P, P.T)}   — the asymmetry that forces BOTH")
print("  M₂ = Sym ⊕ Antisym = enrichment-space ⊕ defect-space  (exact, complementary)")
print(f"     dim enrichment (symmetric) = 3,  dim defect (antisymmetric) = 1,  3+1 = 4")
print()

print("=" * 68)
print("  3.  same ν, opposite reading")
print("=" * 68)
nu_R = R @ R - R
print(f"  ν(R) = R² − R = {np.round(nu_R,3).tolist()} = +I")
print(f"     as DEFECT     : the gap R²−R (how far R is from idempotent)")
print(f"     as ENRICHMENT : R² = R + I — R gains the identity by referring to itself")
print(f"  one quantity, +I; the minus sign is the duality. self-reference (+I) and")
print(f"  self-negation (−I) are exact additive inverses → they cancel → P² = P.")
print()
print("  VERDICT: exact. defect = the antisymmetric/Lie/[·] half (self-negation, −I);")
print("  enrichment = the symmetric/Jordan/{·} half (self-reference, +I); θ(X)=−Xᵀ is")
print("  the exact involution between them; their sum is the seed, P = R + N.")
