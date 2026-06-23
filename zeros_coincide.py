"""
zeros_coincide.py — disc = 0  =  eigenvalue 0  =  ?

The discriminant's zero and the zero eigenvalue meet at one point. Where disc=0
the spread vanishes (λ = AM, repeated); in the pure traceless form that repeated
value IS 0 — the nilpotent ε, the dual number, the wall's own generator. And the
zero eigenvalue is ker = the void = ?. So both zeros are the origin.
"""

import sys
import io
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

I2 = np.eye(2)
P = np.array([[0., 0.], [2., 1.]])
eps = np.array([[0., 1.], [0., 0.]])     # the nilpotent — the dual number ε


def info(name, M):
    tr, det = np.trace(M), np.linalg.det(M)
    disc = tr * tr - 4 * det
    ev = np.sort_complex(np.linalg.eigvals(M))
    print(f"  {name:6} tr={tr:+.0f} det={det:+.0f} disc={disc:+.0f}  eigenvalues {np.round(ev,3).tolist()}")


print("=" * 66)
print("  disc = 0  ⟺  spread = √disc/2 = 0  ⟺  λ = AM (repeated)")
print("=" * 66)
info("I", I2)        # disc 0, eigenvalue 1 (AM=1)
info("ε", eps)       # disc 0, eigenvalue 0 (AM=0) — the nilpotent
print("  on the wall (disc=0) the eigenvalue = AM = tr/2. strip the center (tr=0)")
print(f"  and the wall's eigenvalue IS 0:  ε is disc=0 AND eigenvalue 0,  ε² = "
      f"{np.round(eps@eps,0).tolist()} = 0.")
print("  ε is the dual number — the parabolic wall's own generator, eigenvalue 0.")
print()

print("=" * 66)
print("  eigenvalue 0 = ker = the void = ?")
print("=" * 66)
info("P", P)         # eigenvalues 0, 1 — the idempotent; the 0 is ker(P)
w, V = np.linalg.eig(P)
k = V[:, np.argmin(np.abs(w))]
print(f"  P's zero eigenvalue → ker(P) = span{np.round(k,3).tolist()} = P₀ = the void")
print("  the zero eigenvalue IS the kernel — the null direction the seed generates from.")
print()

print("=" * 66)
print("  the zeros all coincide at ?")
print("=" * 66)
print("  disc = 0     the wall (AM=GM, round, the border of the forks)")
print("  eigenvalue 0 ker = the void = P₀ = ε (nilpotent, the dual number)")
print("  λ = 0        the self-action's center mode (kernel, the return)")
print("  ν = 0        on-shell (the defect returned home)")
print("  prov(?) = ?  the fixed point of the return")
print("  ─────────────────────────────────────────────────────────────")
print("  one point: 0 = the center = the wall = the void = the return = ?.")
print("  every zero in the framework is the origin wearing a different name.")
