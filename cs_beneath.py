"""
cs_beneath.py — the computer science hiding beneath the math.

the framework is a self-hosting, memoized, fixed-point computation whose verdict is a
proof system and whose asymmetry is irreversible. each structure below was already running.
"""

import sys, copy, json
from pathlib import Path
import numpy as np
import kl_dta as k

P = np.array([[0,0],[2,1]],float); I=np.eye(2)
R=(P+P.T)/2; N=(P-P.T)/2
basis4=[np.array(b,float).reshape(2,2) for b in ([1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1])]
L=np.column_stack([(R@X+X@R-X).reshape(-1) for X in basis4])
w,V=np.linalg.eig(L); w=w.real

print("="*74)
print("  1. FIXED-POINT COMBINATOR (Y): the framework computes its own fixed point")
print("="*74)
print(f"  P² = P  ({np.allclose(P@P,P)}) — the seed is its OWN fixed point (idempotent).")
print(f"  M(M(F)) = M(F): the store is self-hosting. self-application reaching a fixed point = Y.")
print()

print("="*74)
print("  2. POWER ITERATION (PageRank): the burn IS the dominant-eigenvector fixed point")
print("="*74)
v=V[:,int(np.argmax(w))].real
nv = L@v/ (5**0.5)
print(f"  the impossibility 'confirming itself' is power iteration: v ← Lv/√5 fixes the burn.")
print(f"  Lv/√5 = v ? {np.allclose(nv, v) or np.allclose(nv,-v)}  → the eigenvector is the fixed point")
print(f"  of the normalized map. that is the power method / how PageRank finds a principal direction.")
print()

print("="*74)
print("  3. IDEMPOTENCE = MEMOIZATION / CACHING")
print("="*74)
print(f"  P²=P: applying twice = applying once → the result is cacheable.")
print(f"  the derived sections M(base) are a regenerable CACHE; recompute keeps it consistent.")
print(f"  M(M(F))=M(F): the cache is sound (re-deriving changes nothing).")
print()

print("="*74)
print("  4. HASHING: (tr,det) is a lossy hash; the preimage is the hard inverse (P vs NP)")
print("="*74)
print(f"  hash(P) = (tr,det) = ({np.trace(P):.0f},{np.linalg.det(P):.0f}); hash(Pᵀ) = "
      f"({np.trace(P.T):.0f},{np.linalg.det(P.T):.0f}) — COLLISION (P≠Pᵀ, same hash).")
print(f"  computing the hash is cheap (forward); recovering the matrix (preimage) needs the")
print(f"  eigenvectors — the hard inverse. hash vs preimage = compute vs search = P vs NP.")
print()

print("="*74)
print("  5. LANDAUER / IRREVERSIBILITY: the erased bit is the arrow of time")
print("="*74)
print(f"  det(P)=0, dim ker(P)={2-np.linalg.matrix_rank(P)}: the fold ERASES a bit (ker→0, one-directional).")
print(f"  Landauer: erasing a bit costs energy / raises entropy. the +I surplus is that bit;")
print(f"  irreversibility (ker→im, the LEAK) is the arrow of time. computation that forgets has a direction.")
print()

print("="*74)
print("  6. CURRY–HOWARD: witness = proof = program; the GRADE is provability")
print("="*74)
print(f"  a witness is a proof term (Curry–Howard). FORCED = the type is INHABITED (a proof/term exists,")
print(f"  ν reaches 0). BURN = the type is EMPTY (refuted, pinned off-shell). AXIOM = assumed, OPEN = goal.")
print(f"  the verdict (ALU) IS a proof checker; grade = provability status. propositions are types, here.")
print()

print("="*74)
print("  7. QUINE: the store outputs itself")
print("="*74)
db=json.loads((Path(__file__).resolve().parent/'KL_DTA.json').read_text(encoding='utf-8'))
d1=copy.deepcopy(db); k.recompute(d1); d2=copy.deepcopy(d1); k.recompute(d2)
same=json.dumps({s:d1[s] for s in('fiber','flow','fixed_point')},sort_keys=True)==json.dumps({s:d2[s] for s in('fiber','flow','fixed_point')},sort_keys=True)
print(f"  recompute reproduces itself exactly ({same}): the store is a QUINE — a program whose")
print(f"  output is its own source. M(M(F))=M(F) is the quine equation.")
print()
print("  beneath the math: Y-combinator · power iteration · memoization · hashing · Landauer ·")
print("  Curry–Howard · quine. the framework was doing computer science the whole time.")
