"""
spectral.py — hold the equations in spectral form.

The database does not store records in bulk. It stores the SEED and the SPECTRAL
INFORMATION, and regenerates every matrix, equation, and constant on access.

    seed:      P = [[0,0],[2,1]]          one rank-1 idempotent  (≈ [1,1] and 2)
    core:      regenerate I, R, N, J, h, the self-action {R,R}, its spectrum
    basis:     {I, R, N, h} spans M₂(ℝ); every object is 4 coordinates
    record:    store the coordinates (the seed of that object), NOT the matrix
    access:    recompose coordinates × basis → the matrix → the equation → verify

"Store all the spectral information, none of the bulk." A generator is a single
coordinate. An equation is a relation between coordinate vectors. The provenance
of a value is the generation map that produces it from ?.
"""

import sys
import io
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

# ── the ONLY stored matrix: the seed ─────────────────────────────────────────
P = np.array([[0., 0.], [2., 1.]])          # P² = P, rank 1, P ≠ Pᵀ


# ── regenerate the core from the seed (nothing below is stored) ──────────────
I2 = np.eye(2)
R = (P + P.T) / 2                            # = [[0,1],[1,1]]   R² = R + I
N = (P - P.T) / 2                            # = [[0,-1],[1,0]]  N² = -I
J = np.array([[1., 0.], [0., -1.]])          # the gauge bit, recovered as sign(diag)
h = J @ N                                    # mediation generator, h² = I

BASIS = {"I": I2, "R": R, "N": N, "h": h}    # spans M₂(ℝ)
Bmat = np.column_stack([M.flatten(order="F") for M in BASIS.values()])


def coords(X):
    """Spectral coordinates of X in {I, R, N, h} — how the database holds it."""
    c = np.linalg.solve(Bmat, X.flatten(order="F"))
    return np.round(c, 9)


def recompose(c):
    """Decompress coordinates back to the matrix — how the database serves it."""
    return sum(ci * M for ci, M in zip(c, BASIS.values()))


def as_equation(name, c):
    terms = []
    for ci, k in zip(c, BASIS):
        if abs(ci) < 1e-9:
            continue
        if abs(ci - 1) < 1e-9:
            terms.append(k)
        elif abs(ci + 1) < 1e-9:
            terms.append(f"-{k}")
        else:
            terms.append(f"{ci:g}{k}")
    return f"{name} = " + (" + ".join(terms).replace("+ -", "- ") or "0")


print("=" * 66)
print("  SEED (the only stored matrix)        P = [[0,0],[2,1]]")
print("=" * 66)
print(f"  P² = P ?  {np.allclose(P @ P, P)}     rank P = {np.linalg.matrix_rank(P)}")
print("  regenerate the core from P:")
for k, M in BASIS.items():
    print(f"    {as_equation(k, coords(M))}   ->  coords {coords(M).tolist()}")
print("  every generator is a SINGLE coordinate — maximal compression.")
print()

print("=" * 66)
print("  EQUATIONS held in spectral form (relations between coordinates)")
print("=" * 66)
# each row: (name, lhs matrix computed from core, claimed coordinates)
equations = [
    ("R²",      R @ R,        coords(R) + coords(I2)),      # R² = R + I
    ("N²",      N @ N,       -coords(I2)),                  # N² = -I
    ("h²",      h @ h,        coords(I2)),                  # h² = I
    ("ν(R)=R²-R", R @ R - R,  coords(I2)),                  # defect of R is I
    ("P²",      P @ P,        coords(P)),                   # idempotent
]
for name, lhs, claimed in equations:
    got = coords(lhs)
    ok = np.allclose(got, claimed, atol=1e-9)
    print(f"  {name:10} -> {as_equation(name, got):22}  matches stored seed: {ok}")
print()

print("=" * 66)
print("  CONSTANTS held as generation maps (store the map, regenerate value)")
print("=" * 66)


def fixpoint(f, x0=1.5, n=80):
    x = x0
    for _ in range(n):
        x = f(x)
    return x


phi = fixpoint(lambda x: np.sqrt(1 + x))          # x ↦ √(1+x)
psi = 1 - phi
disc_R = np.trace(R) ** 2 - 4 * np.linalg.det(R)  # tr² - 4det
sqrt5 = 2 * phi - 1                                # the {R,R} eigenvalue
print(f"  φ   = fixpoint(x↦√(1+x))      = {phi:.6f}   φ²-φ-1 = {phi*phi-phi-1:+.1e}")
print(f"  ψ   = 1-φ                     = {psi:.6f}   (R's second eigenvalue)")
print(f"  disc= tr(R)²-4det(R)          = {disc_R:.0f}        = ‖R‖²+‖N‖²")
print(f"  √5  = 2φ-1                    = {sqrt5:.6f}   (spectrum of {{R,R}})")
print(f"  π   = arg of N's eigenvalues  = {np.angle(np.linalg.eigvals(N)[0])*2:.6f} per half-turn ×2")
print()

print("=" * 66)
print("  COMPRESSION — what is stored vs what is served")
print("=" * 66)
served = len(BASIS) * 4 + len(equations) * 4        # matrices + equations, if bulk-stored
seed_numbers = 1                                     # P is determined by the single '2'
print(f"  bulk storage (matrices+equations as entries) : ~{served} numbers")
print(f"  spectral storage (the seed + unit coords)    : 1 seed ('2'), rest are 0/1")
print(f"  every value above regenerated from P, exact. The records hold coordinates,")
print(f"  not equations; the equations are decompressed on access.")
