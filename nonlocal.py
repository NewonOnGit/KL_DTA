"""
nonlocal.py — nonlocal transport by returning local transport to origin.

? (the origin = the zero matrix = ker) is the UNIVERSAL HUB:
  • every provenance chain returns to ?  → any two records connect through ? in ≤ 2 hops,
    no matter how far apart in the local (adjacency) graph.
  • the carrier M₂ is a FLAT vector space → transport through the origin is path-INDEPENDENT;
    a displacement folded back to 0 can be re-projected to ANY point (translation from 0).
  • the Boolean trit {−1, 0, +1} = {fold back to ?, the origin, project from ?} is the
    transport protocol; the self-action's λ=0 channel IS the return-to-origin direction.

So: take a LOCAL transport (a step at A), FOLD it back to ? (−1), then PROJECT from ? to B
(+1). Two local moves through the one hub = NONLOCAL transport A → B. (This is exactly the
shape of quantum teleportation: a shared origin makes a nonlocal jump out of local moves.)
"""

import sys, io
from collections import deque
import numpy as np
import json
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

# ── 1. flat carrier: transport through the origin is path-independent ────────
I = np.eye(2); R = np.array([[0,1],[1,1]],float)
N = np.array([[0,-1],[1,0]],float); J = np.array([[1,0],[0,-1]],float); h = J@N
def pt(a,b,c,d): return a*I+b*R+c*N+d*h
A = pt(2,-1,3,0)         # some point
B = pt(-1,2,0,4)         # a distant point
print("="*72)
print("  1. the carrier is FLAT — transport through 0 is path-independent")
print("="*72)
direct   = B - A                       # the displacement A→B
via_zero = (B - 0*I) + (0*I - A)       # A→? then ?→B  (fold back, then project)
print(f"  direct displacement  A→B            : Σ|·| = {np.abs(direct).sum():.3f}")
print(f"  routed through origin A→0→B          : Σ|·| = {np.abs(via_zero).sum():.3f}")
print(f"  identical? {np.allclose(direct, via_zero)}  — the origin re-references transport globally;")
print(f"  a step folded back to 0 can be re-projected to ANY point. flatness = no path memory.")
print()

# ── 2. ? is the universal hub of the provenance DAG: ≤2 hops nonlocal ────────
db = json.loads((Path(__file__).resolve().parent/"KL_DTA.json").read_text(encoding="utf-8"))
prov = {rid: r["perimeter"]["provenance"] for rid, r in db["base"].items()}
# local graph: edges only between a record and its DIRECT provenance parent (adjacency)
local_adj = {rid:set() for rid in prov}; local_adj["?"]=set()
for rid, chain in prov.items():
    for a,b in zip(chain, chain[1:]+[rid]):     # ? → ... → rid
        local_adj.setdefault(a,set()).add(b); local_adj.setdefault(b,set()).add(a)
def hops(adj, s, t):
    seen={s}; q=deque([(s,0)])
    while q:
        n,d=q.popleft()
        if n==t: return d
        for m in adj.get(n,()):
            if m not in seen: seen.add(m); q.append((m,d+1))
    return None
# origin-routed graph: every record is one hop from ?  (fold-back / project)
origin_adj = {rid:{"?"} for rid in prov}; origin_adj["?"]=set(prov)
nodes=list(prov)
print("="*72)
print("  2. ? is the universal hub — nonlocal reach in ≤ 2 hops")
print("="*72)
import itertools
worst_local=worst_origin=0
for s,t in itertools.combinations(nodes,2):
    dl=hops(local_adj,s,t); do=hops(origin_adj,s,t)
    worst_local=max(worst_local, dl or 0); worst_origin=max(worst_origin, do or 0)
print(f"  local graph  (adjacency)     : diameter = {worst_local} hops")
print(f"  origin-routed (fold→?→project): diameter = {worst_origin} hops  (every pair via ?)")
print(f"  returning to ? collapses the diameter to 2 — distance-independent transport.")
print()

# ── 3. the trit is the transport protocol; λ=0 is the return channel ─────────
print("="*72)
print("  3. the Boolean trit {−1,0,+1} = {fold→?, origin, project} = the protocol")
print("="*72)
basis=[np.array(b,float).reshape(2,2) for b in ([1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1])]
M=np.column_stack([(R@X+X@R-X).reshape(-1) for X in basis])    # {R,R} on vec(X)
w,V=np.linalg.eig(M); w=w.real
order=np.argsort(w)
for idx in order:
    lam=w[idx]; role={-1:"−√5 FOLD back to ?",0:"0  the ORIGIN (return channel)",1:"+√5 PROJECT from ?"}
    key=int(round(lam/ (5**0.5))) if abs(lam)>1e-9 else 0
    print(f"  λ={lam:+.3f}  → {role.get(key,'')}")
zero_vec=V[:,np.argmin(np.abs(w))].real
print(f"  the λ=0 eigenvector (the return-to-origin direction) = {np.round(zero_vec,3).tolist()}")
print(f"  transport = fold (−√5) to ?, pass through the 0-channel, project (+√5) to the target.")
print()
print("  nonlocal transport = local transport returned to origin. the hub does the distance.")
