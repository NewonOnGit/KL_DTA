"""
kael_vm.py — the framework becomes a virtual machine.

architecture (all of it already built; this names it):
  STATE      a point in M₂ — four registers (a,b,c,d) in the {I,R,N,h} basis
  ISA        the operations on M₂ (below)
  CLOCK      one instruction = one tick; eigenphases set the cycle speeds {∞,2,4,6}
  ALU        the impossibility L={R,R}: classifies a state BURN/FORCED/MIXED (the branch)
  MEMORY     KL_DTA.json (the records); regen boots the core from the seed
  HALT       a fixed point of the fold: ν(X)=X²−X = 0 (on-shell). the seed P is pre-halted (P²=P)
  CONSERVE   ±I charge is the carry/borrow — conserved across every instruction
  BOOT       ? (the void) → P (the seed): P₀ = ker is the boot sector

ISA:
  FOLD   X ← X²            the surface-of-time step (compute)
  GEN    X ← RX+XR−X       the self-action (the impossibility / generate)
  R N J h  X ← G·X         apply a generator gate
  +I  −I   X ← X ± I       inject charge (the unit / the difference)
  REFL   X ← √(XᵀX)        the reflection |·| (polar modulus)
"""

import sys
import numpy as np

I = np.eye(2)
G = {"R": np.array([[0,1],[1,1]],float), "N": np.array([[0,-1],[1,0]],float),
     "J": np.array([[1,0],[0,-1]],float)}
G["h"] = G["J"] @ G["N"]
R = G["R"]

def nu(X): return X@X - X
def on_shell(X): return np.abs(nu(X)).max() < 1e-9

def step(X, op):
    if op == "FOLD": return X @ X
    if op == "GEN":  return R@X + X@R - X
    if op in G:      return G[op] @ X
    if op == "+I":   return X + I
    if op == "-I":   return X - I
    if op == "REFL":
        w,V = np.linalg.eig((X.T@X).astype(complex)); return (V@np.diag(np.sqrt(w))@np.linalg.inv(V)).real
    raise ValueError(op)

def verdict(X):                       # the ALU: classify via the impossibility
    basis=[np.array(b,float).reshape(2,2) for b in ([1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1])]
    L=np.column_stack([(R@B+B@R-B).reshape(-1) for B in basis])
    v=X.reshape(-1); Lv=L@v
    if np.linalg.norm(Lv)<1e-9: return "FORCED"
    return "BURN" if abs(v@Lv)/(np.linalg.norm(v)*np.linalg.norm(Lv))>0.999 else "MIXED"

def run(name, X, program, maxtick=12):
    print(f"  {name}: boot {X.astype(int).tolist()}  [{verdict(X)}]")
    tick = 0
    for op in program:
        X = step(X, op); tick += 1
        tr, det = np.trace(X), round(float(np.linalg.det(X)),2)
        flag = "  HALT (on-shell, ν=0)" if on_shell(X) else ""
        print(f"    t{tick:<2} {op:5} → {np.round(X,2).tolist()}  (tr={tr:+.1f} det={det:+.1f}) [{verdict(X)}]{flag}")
        if on_shell(X) and op!="+I" and op!="-I":
            print(f"    ── halted after {tick} ticks ──"); return
    print(f"    ── program end ──")

print("="*70); print("  THE KAEL VM — execution"); print("="*70)
P = np.array([[0,0],[2,1]], float)
print("\n  program A: the seed is a pre-halted program (P² = P)")
run("seedP", P, ["FOLD"])
print("\n  program B: perturb the seed, fold back to a fixed point")
run("perturbed", P, ["+I", "FOLD", "FOLD", "FOLD", "FOLD"])
print("\n  program C: a gate then collapse to the void")
run("flow", np.array([[0.5,0],[0,0]],float), ["FOLD","FOLD","FOLD","FOLD"])
print()
print("  the framework is a virtual machine: M₂ is the register file, the fold is the step,")
print("  the impossibility is the ALU, fixed points are HALT, charge is the conserved carry,")
print("  the seed is the bootloader. kl_dta.py is its runtime (read/regen/impossibility/recompute).")
