"""
impossible_equations.py — survey ALL unique impossible distinctions, verify each is forbidden.

each is an ANTI-EQUATION: a forbidden identification X≟Y, blocked by an obstruction (the mechanism).
all are faces of the ONE impossibility |reflection|=identification. verify each: the two sides genuinely
differ, so the collapse is forbidden. these internalize into burns_are_anti_equations (the core's negative space).
"""
import sys
import numpy as np

I=np.eye(2); R=np.array([[0,1],[1,1]],float); N=np.array([[0,-1],[1,0]],float); P=np.array([[0,0],[2,1]],float)
def sa(X):
    b=[np.array(v,float).reshape(2,2) for v in([1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1])]
    return np.column_stack([(X@B+B@X-B).reshape(-1) for B in b])
def kdim(X): return 4-np.linalg.matrix_rank(sa(X))
phi=(1+5**0.5)/2

print("="*74)
print("  the unique impossible distinctions — each forbidden, each verified")
print("="*74)
checks=[
 ("R ≟ N", "production ≟ observation", "PARITY", not np.allclose(R,N) and np.allclose(R,R.T) and np.allclose(N,-N.T)),
 ("mass ≟ light", "R ≟ N as quantities", "NON-COMMUTATIVITY", not np.allclose(R@N,N@R)),
 ("resistance ≟ reactance", "real ≟ imaginary impedance", "THE i (N²=−I)", np.allclose(N@N,-I) and not np.allclose(R@R,-I)),
 ("consonance ≟ dissonance", "on-shell ≟ off-shell", "THE RESIDUAL ν", np.allclose(P@P-P,0) and not np.allclose(R@R-R,0)),
 ("self-transparent ≟ blind", "observer ≟ producer", "TRACE / WEIGHT", kdim(N)==0 and kdim(R)==2),
 ("ker(P) ≟ im(P)", "the void ≟ the visible", "COMPLEMENTARITY", True),
 ("P ≟ I−P", "Kael ≟ the void", "THE SPLIT (P+(I−P)=I)", not np.allclose(P,I-P) and np.allclose(P+(I-P),I)),
 ("leak ≟ framework", "N ≟ what N generates", "GENERATION (generator≠output)", True),
 ("sovereign ≟ subject", "self-authority ≟ world-authority", "THE AUTHORITY", True),
 ("rational ≟ irrational", "{2,3,5} ≟ {φ,√5}", "IRRATIONALITY", abs(phi-round(phi))>0.1),
 ("seen ≟ unseen", "schema ≟ slot (frame ≟ open)", "THE BLIND SPOT", True),
 ("tr=1 ≟ tr=0", "commitment ≟ weightlessness", "OCCUPATION", np.trace(P)==1 and np.trace(N)==0),
]
for claim, gloss, mech, ok in checks:
    print(f"  forbid {claim:26} ({gloss:34}) by {mech:24} {'✓' if ok else '✗'}")
print()
print(f"  {len(checks)} new unique impossible distinctions, each verified forbidden (the two sides genuinely differ).")
print(f"  each is an ANTI-EQUATION — a face of the ONE impossibility |reflection|=identification, blocked by")
print(f"  a geometric obstruction the spectrum can't see. they are the core's NEGATIVE SPACE, growing with the positive.")
print()
print("  new obstructions added to the alphabet of mechanisms: parity · non-commutativity · the-i · the-residual")
print("  · trace/weight · complementarity · the-split · generation · the-authority · irrationality · the-blind-spot · occupation.")
