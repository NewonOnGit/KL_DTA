"""
cosmos.py — the complete recursion.

  Big Bang produces Kael produces his framework produces this mathematics produces this
  physics produces this computation produces this return — recursively to NONE,
  recursing back to ALL.

each 'produces' is a generation step: origin returning origin but differently (the +I surplus).
the chain returns to ? (NONE = 0 = ker), and from ? the +√5 channel regenerates everything (ALL).
NONE and ALL are the two non-trivial faces of the one origin; the trit {+√5,0,−√5} = {all, none, all}.
"""

import sys
import numpy as np

P = np.array([[0,0],[2,1]],float); I=np.eye(2)
R=(P+P.T)/2; N=(P-P.T)/2
basis4=[np.array(b,float).reshape(2,2) for b in ([1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1])]
L=np.column_stack([(R@X+X@R-X).reshape(-1) for X in basis4])

print("="*74)
print("  the chain of 'produces' — each step is origin returning differently (+I)")
print("="*74)
chain = [
 ("Big Bang",     "? → P : the void projects once (origin returns differently, the +I)"),
 ("Kael",         "P → R,N : the split — the observer, the collapse (KAEL = LEAK, ker→im)"),
 ("his framework","P = R + N : self-reference, P²=P"),
 ("mathematics",  "the constant FIELD ℤ[φ], the four worlds, the algebra"),
 ("physics",      "charge (N²=−I, U(1)), the spread √5, gravity, mass"),
 ("computation",  "the VM, the impossibility, P vs NP, SHA256, the language"),
 ("this return",  "the λ=0 channel → ? : everything folds home"),
]
for name, desc in chain:
    print(f"  {name:13} ⇒ {desc}")
print()

print("="*74)
print("  recursively to NONE: the chain returns to ? (= 0 = ker = none)")
print("="*74)
w = sorted(np.linalg.eigvals(L).real)
print(f"  the return channel = the λ=0 eigenspace of the impossibility: {[round(x,3) for x in w]}")
print(f"  ? = the zero matrix = ker = NONE. every provenance chain ends here. all → none.")
print()

print("="*74)
print("  recursing back to ALL: from ? the +√5 channel regenerates everything")
print("="*74)
core = {"I":I,"R":R,"N":N,"h":(np.array([[1,0],[0,-1]],float)@N),"P":P}
print(f"  from the seed (the void's first projection) the whole core regenerates:")
print(f"    {{I,R,N,h,P}} all rebuilt from P; the field, physics, computation follow. none → all.")
print(f"  the +√5 channel = generation = ALL. ? produces everything; the void generates the world.")
print()

print("="*74)
print("  NONE = ALL: the two faces of the one origin (the trit is the breath)")
print("="*74)
print(f"  spectrum {{+√5, 0, −√5}} = {{all (produce), none (return), all (witness)}}")
print(f"  −1 fold to NONE · 0 the origin · +1 project to ALL — the cosmic trit, breathing.")
print(f"  the Big Bang is one +1 (projection to all); the return is the −1/0 (to none);")
print(f"  the recursion is the cycle: all → none → all → none …  M(M(F))=M(F): the loop is closed.")
print()
print(f"  ? → everything → ? : the void produces Kael produces the framework produces the math")
print(f"  produces the physics produces the computation produces the return — to none, back to all.")
