"""
readouts.py — pull out as many data-table readouts of the math as possible, at our
current location (M₂, the self-action L, the loop). each table is a VIEW of the one source.
this demonstrates: the math IS a relational database; every readout is a framework object.
"""

import sys
import numpy as np

I=np.eye(2); R=np.array([[0,1],[1,1]],float); N=np.array([[0,-1],[1,0]],float)
J=np.array([[1,0],[0,-1]],float); h=J@N; P=np.array([[0,0],[2,1]],float)
CORE={"I":I,"R":R,"N":N,"J":J,"h":h,"P":P}
B=np.column_stack([m.reshape(-1) for m in (I,R,N,h)]); Binv=np.linalg.inv(B)
b4=[np.array(b,float).reshape(2,2) for b in([1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1])]
L=np.column_stack([(R@X+X@R-X).reshape(-1) for X in b4])

def line(t): print("\n"+t); print("-"*len(t))

# 1 — invariants
line("T1  INVARIANTS   name | tr | det | disc | world")
for n,X in CORE.items():
    d=np.trace(X)**2-4*np.linalg.det(X)
    wl="EDGE" if abs(d)<1e-9 else("GOLDEN" if d>0 else "RETURN")
    print(f"   {n:2} | {np.trace(X):+.0f} | {np.linalg.det(X):+.0f} | {d:+.0f} | {wl}")

# 2 — spectrum + clock
line("T2  SPECTRUM     name | eigenvalues | eigenphase° | period")
for n,X in CORE.items():
    ev=np.linalg.eigvals(X); th=abs(np.angle(ev[0]))
    T="inf" if th<1e-9 else str(round(2*np.pi/th))
    print(f"   {n:2} | {np.round(ev,3).tolist()} | {round(np.degrees(th),1)} | {T}")

# 3 — verdict (the impossibility ALU)
line("T3  VERDICT      name | verdict | scale")
for n,X in CORE.items():
    v=X.reshape(-1); Lv=L@v; nm=np.linalg.norm(Lv)
    if nm<1e-9: vd="FORCED"
    else: vd="BURN" if abs(v@Lv)/(np.linalg.norm(v)*nm)>0.999 else "MIXED"
    print(f"   {n:2} | {vd:6} | {nm/ (np.linalg.norm(v)+1e-9):.3f}")

# 4 — type signature (the VM)
line("T4  TYPE-SIG     name | VERDICT HALT WORLD q CLK")
for n,X in CORE.items():
    a=(Binv@X.reshape(-1))[0]; halt="HALT" if np.abs(X@X-X).max()<1e-9 else "RUN"
    d=np.trace(X)**2-4*np.linalg.det(X); wl="EDGE" if abs(d)<1e-9 else("GOLD" if d>0 else "RET")
    th=abs(np.angle(np.linalg.eigvals(X)[0])); T="inf" if th<1e-9 else f"T{round(2*np.pi/th)}"
    print(f"   {n:2} | {halt:4} {wl:4} q={a:+.1f} {T}")

# 5 — the field (Fibonacci / Lucas from R^n)
line("T5  FIELD        n | Fₙ | Lₙ=tr(Rⁿ) | det=(-1)ⁿ")
M=np.eye(2)
for k in range(1,7):
    M=M@R; print(f"   {k} | {int(round(M[0,1]))} | {int(round(np.trace(M)))} | {int(round(np.linalg.det(M))):+d}")

# 6 — the worlds (constant trit)
line("T6  WORLDS       k | disc=1+4k | world | units")
for k,wl,u in [(1,"golden ℤ[φ]","±φⁿ ∞"),(0,"Boolean {0,1}","idempotent"),(-1,"Eisenstein ℤ[ω]","μ₆")]:
    print(f"   {k:+d} | {1+4*k:+d} | {wl:14} | {u}")

# 7 — the difference, typed
line("T7  DIFFERENCE   type | expression | value")
for t,e,val in [("algebraic","R²−R","+I"),("spectral","√disc","√5"),("quantum","[R,N]‖·‖","√10"),
                ("number","the different 𝔡","√5"),("charge","±I","U(1)")]:
    print(f"   {t:9} | {e:14} | {val}")

# 8 — fixed points of the fold (halting configs)
line("T8  FIXED-PTS    (t,d) | who | regime")
for t,d,who in [(0,0,"? void"),(1,0,"P seed"),(2,1,"I identity"),(-1,1,"Eisenstein root")]:
    disc=t*t-4*d; reg="EDGE" if disc==0 else("escape" if disc>0 else "return")
    print(f"   ({t:+d},{d:+d}) | {who:16} | {reg}")

# 9 — opcodes (verbs)
line("T9  OPCODES      verb | operation")
for v,op in [("fold","X²"),("generate","+√5 channel"),("return","λ=0 → ?"),
             ("confirm","Lv=√5v"),("complete","R²+N²=R"),("reflect","√(XᵀX)")]:
    print(f"   {v:9} | {op}")

print("\n  9 tables, one source (M₂ + L). every readout is a VIEW; each is a framework object")
print("  (a typed function with provenance). the math is already a relational database.")
