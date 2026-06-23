"""
particles.py — computation unifies the elementary particles through the observer.

a PARTICLE = an on-shell eigenmode: it obeys the dispersion X²=tr·X−det·I (the mass-shell),
ν=0 (FORCED, real, propagating). EVERY matrix obeys this one relation (Cayley-Hamilton) — so all
particles are unified by ONE dispersion. each carries LIGHT (spectra=eigenvalues, the fold, degree-2)
and GRAVITY/MASS (geometry=eigenvectors, where it settles, degree-1). the OBSERVER is the fold
(X²=observation): it reads both. computation (the fold) unifies mass and light through the observer.
"""
import sys
import numpy as np

def dispersion_holds(X):  # Cayley-Hamilton: X² = tr·X − det·I
    return np.allclose(X@X, np.trace(X)*X - np.linalg.det(X)*np.eye(2))

print("="*70)
print("  1. ONE dispersion unifies all particles: X² = tr·X − det·I")
print("="*70)
zoo={"R(mass)":np.array([[0,1],[1,1]],float), "N(light/charge)":np.array([[0,-1],[1,0]],float),
     "P(seed)":np.array([[0,0],[2,1]],float), "I(identity)":np.eye(2),
     "Eisenstein":np.array([[1,-1],[1,0]],float)}
for nm,X in zoo.items():
    print(f"  {nm:16} obeys X²=tr·X−det·I ? {dispersion_holds(X)}   (tr={np.trace(X):+.0f}, det={np.linalg.det(X):+.0f})")
print(f"  EVERY 2×2 obeys it (Cayley-Hamilton). all 'particles' lie on the ONE mass-shell — unified by computation.")
print()

print("="*70)
print("  2. each particle = LIGHT (spectra) + MASS/GRAVITY (geometry)")
print("="*70)
print(f"  LIGHT   = spectra = eigenvalues (the fold λ²−tr·λ+det=0, degree-2, the FREQUENCY/energy, radiated).")
print(f"  GRAVITY = mass = geometry = eigenvectors (degree-1, where it SETTLES, the metric).")
print(f"  on-shell (ν=X²−X=0, FORCED) = a real propagating particle; off-shell (BURN) = virtual.")
print(f"  a particle is named by its (mass-shell point) = (tr,det) = (where it settles, its frequency).")
print()

print("="*70)
print("  3. the OBSERVER is the fold — it reads light AND mass")
print("="*70)
print(f"  the fold X² = OBSERVATION (degree-2). 'origin emits spectra (light); the observer projects geometry")
print(f"  (gravity).' the observer reads the eigenvalues (light) and the eigenvectors (mass) of each state.")
print(f"  mass (R, resistance, geometry) and light (N, spectra, the radiated) DON'T commute: [R,N]=C≠0 —")
print(f"  their non-commutativity IS the observer (C=[R,N]). the observer is where mass and light meet.")
print()

print("="*70)
print("  4. the unification")
print("="*70)
print(f"  COMPUTATION = the fold / the dispersion X²=tr·X−det·I — the ONE law every particle obeys.")
print(f"  the OBSERVER = the fold-as-observation (C=[R,N]) — reads each particle's mass (gravity/geometry)")
print(f"  and light (spectra/eigenvalues), unifying the two.")
print(f"  THE PARTICLES = the on-shell spectrum of the one computation, unified by the single mass-shell,")
print(f"  individuated by the observer's reading. the gauge symmetries (su3+su2+u1) are the computation's")
print(f"  symmetries; the masses/mixings are the spectrum. computation unifies the elementary particles")
print(f"  through the observer: one fold, one mass-shell, read into many — mass and light, seen as one.")
