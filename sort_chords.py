"""
sort_chords.py — tag each deepening (insight) with its atoms, then SORT the chords.
sort key: root = lowest atom present, then chord-size (simple first), then name.
adds structure.chords = {by_atom (the chord chart), index (name->atoms)} and reorders deepenings.
"""
import json, re
from pathlib import Path

PATH = Path(__file__).resolve().parent / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))
deep = db["structure"]["deepenings"]

# atom -> keyword signatures (lowercase substring match over name+text)
KW = {
  "A1": ["p²=p","p^2=p","idempotent","fold is reflection","seed_fixed"],
  "A2": ["asymmetry","p≠pᵀ","p!=p^t","one difference","the difference","?+difference","?(?)","surplus","why there"],
  "A3": ["r²=r+i","r^2=r+i","fibonacci","golden","φ","phi"],
  "A4": ["n²=−i","n²=-i","n^2=-i","charge","u(1)","rotation","the i (","spinor","quaternion"],
  "A5": ["p=r+n","the split","r+n (","visible","hidden"],
  "A6": ["r²+n²=r","r^2+n^2=r","origin return","conservation","completion","completely incomplete","returns differently"],
  "A7": ["[r,n]","commutator","harness","observer","metamorphism","2-cell","3-cell","0-cell","cell tower","companion"],
  "A8": ["{r,n}","anticommutator","observation channel"],
  "A9": ["trit","±√5","+√5,0","triad","boolean spectrum"],
  "A10":["m(m(f))","self-host","self-reference","recursion","quine","y combinator","y-combinator","fixed point","apex"],
  "A11":["ker→im","ker->im","leak","irreversib","one-directional","landauer","kael"],
  "A12":["disc","discriminant","√5","sqrt5","2,3,5","pentagram","omega","‖r‖","norm(r)","edge","|disc|","worlds","music","harmonic"],
}
def atoms_of(name, text):
    blob = (name + " " + str(text)).lower()
    found = [a for a,kws in KW.items() if any(k in blob for k in kws)]
    return found or ["A1"]   # default root if nothing matched

tagged = {name: atoms_of(name, txt) for name, txt in deep.items()}
def rootnum(a): return int(a[1:])
def key(name):
    ats = sorted(tagged[name], key=rootnum)
    return (rootnum(ats[0]), len(ats), name)

ordered = sorted(deep, key=key)
db["structure"]["deepenings"] = {name: deep[name] for name in ordered}   # reordered, lossless

# the chord chart: by atom (the "key"), and the index
by_atom = {f"A{i}": [] for i in range(1,13)}
for name in ordered:
    for a in sorted(tagged[name], key=rootnum):
        by_atom[a].append(name)
db["structure"]["chords"] = {
  "is": "the equation-chords sorted. each insight (deepening) is a chord of atoms (A1..A12). sorted by "
        "root atom, then chord-size. by_atom = the chord chart (which insights play in each key); index = name->atoms.",
  "by_atom": {a: lst for a,lst in by_atom.items() if lst},
  "index": {name: "+".join(sorted(tagged[name], key=rootnum)) for name in ordered},
}
PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")

# report
print("CHORDS SORTED — by root atom (the key), simple chords first\n")
ATOM = {"A1":"P²=P","A2":"P≠Pᵀ","A3":"R²=R+I","A4":"N²=−I","A5":"P=R+N","A6":"R²+N²=R",
        "A7":"[R,N]=C","A8":"{R,N}=N","A9":"trit","A10":"M(M(F))","A11":"ker→im","A12":"disc/√5"}
for a in [f"A{i}" for i in range(1,13)]:
    rooted = [n for n in ordered if sorted(tagged[n], key=rootnum)[0]==a]
    if not rooted: continue
    print(f"  {a} ({ATOM[a]}) — {len(rooted)} chords:")
    for n in rooted:
        print(f"      {n:42} = {'+'.join(sorted(tagged[n], key=rootnum))}")
print(f"\n  {len(ordered)} chords sorted across {sum(1 for a in by_atom if by_atom[a])} atom-keys.")
