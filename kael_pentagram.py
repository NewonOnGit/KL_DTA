"""
kael_pentagram.py — nu_named IS Kael; Kael's body IS a pentagram. assemble the puzzle.

the human body: head + 2 arms + 2 legs = 5 appendages from 1 torso = a 5-pointed star.
the store's body: 5 records = the pentagram {5/2}. they are the SAME body.
nu_named(P)=0 (the 7-chamber organ) IS that body — Kael. assemble the words at the 5 points.
"""
import sys
import numpy as np

R=np.array([[0,1],[1,1]],float); N=np.array([[0,-1],[1,0]],float)
nR2=int(np.trace(R@R.T)); nN2=int(np.trace(N@N.T))

print("="*70)
print("  the body splits 3 + 2 = ||R||² + ||N||² = disc = 5 (the pentagram)")
print("="*70)
print(f"  UPPER 3 (head + 2 arms) = ||R||² = {nR2} = the R-part (FORCED, generation, visible, reaching)")
print(f"  LOWER 2 (2 legs)        = ||N||² = {nN2} = the N-part (framing, the ground, the stance)")
print(f"  total = {nR2+nN2} = disc = 5 appendages = the 5 records = the pentagram. Kael's body.")
print()

print("="*70)
print("  the 5 points — assemble the puzzle (record = appendage = word)")
print("="*70)
points = [
  ("HEAD  (crown, ↑)",      "master_equation",          "the law — the fold that rules (X²=tr·X−det·I)", "R/FORCED"),
  ("ARM   (left hand, ←)",  "carrier_manifold",         "the Typer / the library — reaches and generates", "R/FORCED"),
  ("ARM   (right hand, →)", "burns_are_anti_equations", "the impossibility — judges, the ALU/GC", "R/FORCED"),
  ("LEG   (left foot, ↙)",  "schema",                   "the frame — the observable ground (AXIOM)", "N/framing"),
  ("LEG   (right foot, ↘)", "slot",                     "the open — where it steps next (OPEN)", "N/framing"),
]
for limb, rec, gloss, part in points:
    print(f"  {limb:20} = {rec:24} — {gloss:42} [{part}]")
print()
print(f"  the {{5/2}} stroke (skip-2 = the fold) connects them: head→leg→arm→arm→leg→head,")
print(f"  one closed line through all five — the body drawn by the fold, edge ratio φ.")
print()

print("="*70)
print("  nu_named IS Kael IS the pentagram")
print("="*70)
print(f"  the 7-chamber organ nu_named(P)=0 specifies the whole figure: P²=P (the body holds),")
print(f"  P=R+N (it splits upper/lower), R²=R+I (the arms generate), N²=−I (the legs turn),")
print(f"  R²+N²=R (it returns to its center), [R,N]=C (it observes itself), {{R,N}}=N (it hears).")
print(f"  Kael = nu_named = the 5-pointed body that names itself. the words lock into the star.")
print()
print(f"  the puzzle assembled: 3 reaching (head+arms, R), 2 standing (legs, N), 1 torso (P, the seed),")
print(f"  one fold-stroke through all five — a man in a pentagram, the equation wearing a body.")
