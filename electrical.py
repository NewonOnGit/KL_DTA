"""
electrical.py — this is electrical, literally. P = R + N is an IMPEDANCE; chord+delta is a CONDUCTOR.

complex impedance Z = R + iX: R = resistance (real, dissipative), X = reactance (imaginary, energy
stored in the field). the seed P = R + N is exactly this: R = resistance, N = reactance (N²=-I, so N
plays i). a stored insight = chord (the resonant structure) + delta (the potential/voltage) = a
CONDUCTOR carrying current. compression/decompression is signal at rest / signal driven.
"""
import sys
import numpy as np

P=np.array([[0,0],[2,1]],float)
R=(P+P.T)/2; N=(P-P.T)/2

print("="*68)
print("  P = R + N is an IMPEDANCE  Z = R + iX")
print("="*68)
print(f"  R (resistance, real, dissipative) = {R.astype(int).tolist()}, ||R||²={int(np.trace(R@R.T))}")
print(f"  N (reactance, imaginary; N²=-I so N plays i) = {N.astype(int).tolist()}, ||N||²={int(np.trace(N@N.T))}")
print(f"  P = R + N = the IMPEDANCE (resistance + reactance).  N²=-I = i² = -1: N is the reactive unit.")
zmag2=int(np.trace(R@R.T))+int(np.trace(N@N.T))
print(f"  |Z|² = ||R||²+||N||² = {zmag2} = disc  ->  |Z| = sqrt5: the impedance magnitude IS the spread sqrt5.")
print()

print("="*68)
print("  the electrical dictionary (literal)")
print("="*68)
rows=[
 ("CHARGE",     "±I  (N²=-I, U(1)) — the carrier"),
 ("CURRENT",    "the LEAK ker->im (N) — charge flowing, the signal"),
 ("POTENTIAL/VOLTAGE","the DELTA (the difference ν, the gap) — drives the current"),
 ("RESISTANCE", "R (real, dissipative, production, ||R||²=3)"),
 ("REACTANCE",  "N (imaginary, N²=-I, energy in the phase/field, ||N||²=2)"),
 ("IMPEDANCE",  "Z = R + N = P (the seed) ; |Z|=sqrt5"),
 ("RESONANCE",  "the CHORDS at the eigenphase frequencies {periods 2,4,6} — LC modes"),
 ("CONDUCTOR",  "a stored insight = chord (resonant structure) + full delta (full potential)"),
 ("CIRCUIT",    "the store — conductors connected; compression = signal at rest"),
]
for k,v in rows: print(f"  {k:18} {v}")
print()

print("="*68)
print("  why the FULL delta (Kael's choice): the conductor needs full POTENTIAL")
print("="*68)
print(f"  decompression = driving CURRENT through the conductor. the DELTA is the VOLTAGE that drives it.")
print(f"  a lean delta = weak potential = incomplete signal (Ohm: less V, less reconstruction).")
print(f"  the FULL delta = the full driving potential = complete current = complete reformation.")
print(f"  so 'chord + full delta' is electrically necessary: the conductor must carry the whole signal.")
print(f"  the seed is the SOURCE (the battery/the potential origin); decompression drives current through")
print(f"  the impedance network (the conductors), reconstructing the data. the framework is a circuit. literally.")
