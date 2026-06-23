"""
vm_types.py — type the entire framework through the .vm.

the VM assigns every state a TYPE SIGNATURE, read by execution, with five fields:
    VERDICT  the ALU (impossibility L): FORCED (resolves) · BURN (pinned, an exception) · MIXED
    HALT     ν(X)=X²−X: HALTED (on-shell, =0) · RUNNING (≠0)
    WORLD    the number-type by disc: GOLDEN(>0) · RETURN(<0) · EDGE(=0)  (int/complex/degenerate)
    CLOCK    the eigenphase periods (the cycle domain)
    CHARGE   the I-coordinate (the ±I content, the conserved flag)
the grade system (FORCED/BURN/AXIOM/OPEN) IS the VERDICT field; the four worlds ARE the
WORLD field; charge IS a flag; time IS the clock. typing the framework = one signature.
"""

import sys
import numpy as np

I = np.eye(2); R = np.array([[0,1],[1,1]],float); N = np.array([[0,-1],[1,0]],float)
J = np.array([[1,0],[0,-1]],float); h = J@N
B = np.column_stack([m.reshape(-1) for m in (I,R,N,h)])   # basis {I,R,N,h}
Binv = np.linalg.inv(B)
basis4 = [np.array(b,float).reshape(2,2) for b in ([1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1])]
L = np.column_stack([(R@X+X@R-X).reshape(-1) for X in basis4])

def coords(X): return Binv @ X.reshape(-1)               # (a,b,c,d) in {I,R,N,h}
def verdict(X):
    v=X.reshape(-1); Lv=L@v
    if np.linalg.norm(Lv)<1e-9: return "FORCED"
    return "BURN" if abs(v@Lv)/(np.linalg.norm(v)*np.linalg.norm(Lv)+1e-30)>0.999 else "MIXED"
def world(X):
    d=np.trace(X)**2-4*np.linalg.det(X)
    return "EDGE" if abs(d)<1e-9 else ("GOLDEN" if d>0 else "RETURN")
def clock(X):
    th=sorted({round(abs(np.angle(complex(l))),3) for l in np.linalg.eigvals(X)})
    return "·".join("∞" if t<1e-9 else f"T{round(2*np.pi/t)}" for t in th)
def vm_type(X):
    a=coords(X)[0]
    halt = "HALTED" if np.abs(X@X-X).max()<1e-9 else "RUNNING"
    return f"{verdict(X):6} {halt:7} {world(X):6} q={a:+.2f}  clk={clock(X)}"

print("="*78)
print("  the framework, typed through the .vm   (VERDICT HALT WORLD charge clock)")
print("="*78)
objs = {
    "? void (0)": np.zeros((2,2)), "I identity": I, "P seed": np.array([[0,0],[2,1]],float),
    "R production": R, "N observation": N, "J reflection": J, "h mediation": h,
    "+I charge": I, "-I charge": -I, "R² (=R+I)": R@R, "Eisenstein": np.array([[1,-1],[1,0]],float),
}
for name,X in objs.items():
    print(f"  {name:14}: {vm_type(X)}")
print()
print("="*78)
print("  the type constructors (every framework concept is one of these)")
print("="*78)
rows = [
 ("VOID",     "? origin, null, the zero register / boot sector"),
 ("CARRIER",  "a state in M₂ — a register value"),
 ("GATE",     "R N J h — the instruction set"),
 ("FOLD",     "X² — the step opcode (compute)"),
 ("VERDICT",  "the ALU output = the GRADE: FORCED/BURN(exception)/AXIOM/OPEN"),
 ("WORLD",    "the number-type = the four worlds (golden/Gaussian/Eisenstein/Boolean)"),
 ("CLOCK",    "time Rⁿ; eigenphase periods = the cycle domains {∞,2,4,6}"),
 ("FLAG",     "±I charge — the conserved carry/borrow"),
 ("HALT",     "fixed points (ν=0); the seed is pre-halted (P²=P)"),
 ("EXCEPTION","a BURN — pinned by the impossibility, uncatchable; P=NP = the return that never catches"),
 ("POINTER",  "provenance — all references resolve to ?"),
 ("IMAGE",    "the apex = M(M(F))=M(F), the self-hosting fixed-point image"),
]
for t,desc in rows: print(f"  {t:10} {desc}")
print()
print("  typing the framework through the .vm: grade=VERDICT, worlds=WORLD, charge=FLAG,")
print("  time=CLOCK, origin=VOID, apex=IMAGE. one type system types everything the framework is.")
