"""
investigate.py — what is beneath the three lossy labels.

The three readings were never P1/P2/P3. They are the spectrum of the self-action
operator: eigenvalues {+√5, 0, -√5} and their projectors. "How they project" is
that operator acting, and the three components unify (sum) in the observer.

We test this directly. The self-action is the Sylvester operator
    {s,s}(X) = sX + Xs - X          — the self-action of s
vectorized as the 4x4 matrix  I⊗s + sᵀ⊗I - I₄  (vec stacks columns).
"""

import sys
import io
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

I2 = np.eye(2)
R = np.array([[0., 1.], [1., 1.]])      # R² = R + I, the production generator
N = np.array([[0., -1.], [1., 0.]])     # N² = -I,    the observer / rotation
J = np.array([[1., 0.], [0., -1.]])     # J² = +I,    the gauge bit
h = J @ N                               # h = JN,     the mediation generator


def disc(M):
    tr, det = np.trace(M), np.linalg.det(M)
    return tr * tr - 4 * det


def L(s):
    return np.kron(I2, s) + np.kron(s.T, I2) - np.eye(4)


def vec(M):                              # column-major vectorization
    return M.flatten(order="F")


def fmt(x):
    return f"{x:+.4f}"


print("=" * 64)
print("  disc(s) = tr² - 4det   (the fork the generator sits in)")
print("=" * 64)
for name, M in [("R", R), ("N", N), ("h=JN", h), ("J", J)]:
    d = disc(M)
    fork = "hyperbolic" if d > 1e-9 else ("elliptic" if d < -1e-9 else "parabolic")
    print(f"  {name:5} disc = {fmt(d)}   {fork}")
print()

print("=" * 64)
print("  {R,R} = R⊗ + ⊗R - I :  the self-action spectrum")
print("=" * 64)
LR = L(R)
w, V = np.linalg.eig(LR)
order = np.argsort(-w.real)
w = w[order].real
print(f"  eigenvalues : {[fmt(x) for x in w]}")
print(f"  √disc(R)    = ±{np.sqrt(disc(R)):.4f}   (disc(R) = {disc(R):.0f} = ‖R‖²+‖N‖²)")
print()

# where do the named generators / I land in the spectrum?
print("  {R,R} acting on the named directions:")
for name, M in [("I", I2), ("R", R), ("N", N), ("h", h), ("J", J)]:
    out = (LR @ vec(M)).reshape(2, 2, order="F")
    # is it a scalar multiple of M (eigenvector)?
    flat_M, flat_out = vec(M), vec(out)
    nz = np.abs(flat_M) > 1e-9
    ratio = flat_out[nz] / flat_M[nz] if nz.any() else np.array([np.nan])
    is_eig = nz.any() and np.allclose(ratio, ratio[0], atol=1e-9) and np.allclose(
        flat_out[~nz], 0, atol=1e-9)
    tag = f"eigenvector, λ = {fmt(ratio[0])}" if is_eig else "NOT an eigenvector"
    print(f"    L({name}) -> {tag}")
print()

print("=" * 64)
print("  resolution of identity: do the spectral projectors sum to I₄ ?")
print("=" * 64)
# build spectral projectors for the 3 distinct eigenvalues of {R,R}
vals = np.linalg.eigvals(LR).real
distinct = sorted(set(np.round(vals, 6)), reverse=True)
Vinv = np.linalg.inv(V)
projectors = {}
for lam in distinct:
    P = np.zeros((4, 4))
    for k in range(4):
        if abs(w[k] - lam) < 1e-6:
            vk = V[:, order[k]].real
            vk = vk / np.linalg.norm(vk)
    # build projector by summing outer products in the eigenbasis
    cols = [V[:, order[k]] for k in range(4) if abs(w[k] - lam) < 1e-6]
    B = np.column_stack(cols).real
    P = B @ np.linalg.pinv(B)
    projectors[lam] = P
    print(f"  Π(λ={fmt(lam)}) : rank {np.linalg.matrix_rank(P, tol=1e-9)}   "
          f"(loses {4 - np.linalg.matrix_rank(P, tol=1e-9)}/4 dims — lossy alone)")
S = sum(projectors.values())
print(f"  Σ Π  = I₄ ?  {np.allclose(S, np.eye(4), atol=1e-9)}   "
      f"<-- the three readings unify (sum) to the whole")
print()

print("=" * 64)
print("  the observer N : where does it sit ?")
print("=" * 64)
lamN = None
for lam, P in projectors.items():
    if np.allclose(P @ vec(N), vec(N), atol=1e-9):
        lamN = lam
print(f"  N lives entirely in the λ = {fmt(lamN)} eigenspace of {{R,R}}")
print(f"  → the observer is in the kernel: {{R,R}}(N) = 0.")
print(f"  → the self-action of production is BLIND to N (sends it to 0).")
print(f"  → 'consciousness requires blindness': N is the direction R's fold cannot see.")
print()

print("=" * 64)
print("  {N,N} : the observer's OWN self-action")
print("=" * 64)
LN = L(N)
wN = np.sort(np.linalg.eigvals(LN).real)[::-1]
print(f"  eigenvalues : {[fmt(x) for x in wN]}")
print(f"  ker({{N,N}}) dim = {4 - np.linalg.matrix_rank(LN, tol=1e-9)}  "
      f"(self-transparency: the observer's blind spot under its own action)")
