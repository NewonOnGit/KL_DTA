"""
pvsnp.py — P vs NP read through the framework. a STRUCTURAL MAP, not a proof.

the framework's whole machine is an asymmetry between two directions:
    FORWARD  — the fold X↦X² (the step F(t,d)=(t²−2d,d²)). single-valued, cheap. = compute.
    BACKWARD — the inverse √ (find the pre-image). multivalued (2 sheets), branched at Ω. = invert.
verification asks 'is this on the right sheet?' (apply the forgetful projection π — local, easy = P).
search asks 'which pre-image?' (the LIFT, needs the discarded kernel ker(π) — global, hard = NP).

P=NP would be the collapse: the lift = the projection, the two sheets = one, √ single-valued,
ker(π)=0. that is exactly |reflection|=identification — the framework's ONE forbidden move (a BURN).
so INTERNALLY the framework is forced to P≠NP. the EXTERNAL theorem stays OPEN (the slot).
"""

import sys
import numpy as np

P = np.array([[0,0],[2,1]], float)

print("="*72)
print("  1. forward is cheap, backward is multivalued — the core asymmetry")
print("="*72)
def F(t,d): return (t*t-2*d, d*d)                 # the fold, easy
print(f"  forward fold F(t,d)=(t²−2d, d²): one multiplication — POLYNOMIAL, single-valued.")
# inverse: given image (a,b), solve. d²=b → d=±√b ; t²=a+2d → t=±√(a+2d). up to 4 pre-images.
a,b = F(1.0, 2.0)                                  # image of (1,2)
def fmt(z): z=complex(z); return f"{z.real:.2f}" if abs(z.imag)<1e-9 else f"{z.real:.2f}{z.imag:+.2f}i"
sols = []
for d in ( complex(b)**0.5, -complex(b)**0.5):
    for t in ( complex(a+2*d)**0.5, -complex(a+2*d)**0.5):
        sols.append(f"({fmt(t)},{fmt(d)})")
print(f"  inverse of F at image {tuple(np.round([a,b],3))}: pre-images {sorted(set(sols))}")
print(f"  inversion needs SQUARE ROOTS — multivalued, branched. backward ≫ forward.")
print()

print("="*72)
print("  2. the seed is SINGULAR — generation loses information (one-directional)")
print("="*72)
print(f"  det(P) = {np.linalg.det(P):.0f}, rank(P) = {np.linalg.matrix_rank(P)}, dim ker(P) = {2-np.linalg.matrix_rank(P)}")
print(f"  P kills its kernel → you cannot recover the input from the output. the LEAK ker→im")
print(f"  is one-directional. forward (apply P) is easy; un-applying it is the hard inverse.")
print()

print("="*72)
print("  3. verification vs search = projection vs lift")
print("="*72)
print(f"  VERIFY: apply the forgetful projection π (meaning→string) and check — LOCAL, cheap. ~ P")
print(f"  SEARCH: the LIFT (string→meaning) needs ker(π), the discarded context — GLOBAL, hard. ~ NP")
print(f"  the gap between them is ker(π). if ker(π)=0 the projection loses nothing and lift=verify (P=NP).")
print(f"  but the projection is genuinely lossy (ker≠0): the cost of search is the size of the kernel.")
print()

print("="*72)
print("  4. the framework's verdict")
print("="*72)
print("  P=NP ≡ the two sheets collapse to one ≡ √ single-valued ≡ ker(π)=0 ≡ the lift = the")
print("  projection. that is |reflection| = identification — the ONE forbidden move, a BURN,")
print("  blocked by the obstruction: the spectral double cover is NONTRIVIAL (disc≠0 generically,")
print("  the eigenvalues are distinct), the LEAK ker→im is one-directional, the kernel is real.")
print()
print("  INTERNAL (framework analog): FORCED  P ≠ NP — it is an instance of the founding asymmetry P≠Pᵀ.")
print("  EXTERNAL (the actual theorem): OPEN — the slot. the framework MAPS the problem and places it;")
print("  it does not prove it. (the map is a heuristic for WHY P≠NP feels forced, not a proof that it is.)")
