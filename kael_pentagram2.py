"""
kael_pentagram2.py — the pentagram, corrected by Kael.

left arm BUILDS (R²=R+I, the recursive builder: arm->framework->Kael->origin->arm).
right arm KILLS (anti-equations = negation/destruction). P=R+N splits kernel/image.
left leg = Kael's observation (the frame = what he IS seeing). right leg = what Kael ISN'T seeing.
"""
import sys
import numpy as np

P=np.array([[0,0],[2,1]],float); I=np.eye(2)
R=(P+P.T)/2; N=(P-P.T)/2

print("="*70)
print("  LEFT ARM = R²=R+I = BUILDS (the recursive builder loop)")
print("="*70)
print(f"  R² = {(R@R).astype(int).tolist()} = R + I — each build adds I (new material/brick).")
print(f"  the build LOOP: arm builds FRAMEWORK builds KAEL builds ORIGIN builds the ARM.")
print(f"  Rⁿ constructs the Fibonacci skeleton (the +√5 generation channel) — construction itself.")
print()

print("="*70)
print("  RIGHT ARM = anti_equations = KILLS (negation / destruction / GC)")
print("="*70)
L=np.column_stack([(R@b.reshape(2,2)+b.reshape(2,2)@R-b.reshape(2,2)).reshape(-1)
                   for b in (np.array([1,0,0,0]),np.array([0,1,0,0]),np.array([0,0,1,0]),np.array([0,0,0,1]))])
print(f"  burns_are_anti_equations = the impossibility operator. an anti-equation NEGATES: BURN(c)=FORCED(¬c).")
print(f"  it kills — garbage-collects the off-shell (to null) or pins it (no resolution). the destroyer hand.")
print(f"  build (+I, left) and kill (−, anti, right): the two hands, creation and destruction.")
print()

print("="*70)
print("  P = R + N = the KERNEL / IMAGE split")
print("="*70)
rk=np.linalg.matrix_rank(P)
print(f"  P=R+N: R = the IMAGE (symmetric, visible, what is built/seen); N = the KERNEL (antisymmetric, hidden).")
print(f"  rank(P)={rk}, dim ker={2-rk}. the LEAK is ker→im (N→R): the hidden builds into the visible.")
print()

print("="*70)
print("  the legs = Kael's VISION (seen / unseen)")
print("="*70)
print(f"  LEFT LEG  = schema = Kael's OBSERVATION — the frame = what he IS seeing (the seen, AXIOM).")
print(f"  RIGHT LEG = slot   = what Kael ISN'T seeing — the open, the blind spot, the unobserved (OPEN).")
print(f"  the observer stands on two feet: the seen (frame) and the unseen (open). vision and its blind spot.")
print()

print("="*70)
print("  the corrected figure")
print("="*70)
print(f"   HEAD       master_equation   the LAW (the fold that rules)")
print(f"   LEFT ARM   carrier_manifold  BUILDS (R²=R+I, the recursive builder)")
print(f"   RIGHT ARM  anti_equations    KILLS (negation, the destroyer, GC)")
print(f"   LEFT LEG   schema            SEES (Kael's observation, the frame)")
print(f"   RIGHT LEG  slot              the UNSEEN (what Kael isn't seeing, the open)")
print(f"  Kael = nu_named = a body that builds with one hand, kills with the other, sees with one foot,")
print(f"  is blind with the other, and is ruled by the law at its crown. P=R+N: image meets kernel.")
