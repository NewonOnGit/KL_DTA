"""
cut2_carrier_typer.py — the carrier manifold becomes the Typer / functor / library.

a morphism of morphisms: every object is a point (a,b,c,d) of the manifold, and the manifold
moves / types / names / notates / indexes all of them. tables are books pulled by title, read
on demand, never shelved.
"""

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "KL_DTA.json"
db = json.loads(PATH.read_text(encoding="utf-8"))

cm = db["base"]["carrier_manifold"]
cm["morphism"] = {
    "type": "Functor — a morphism of morphisms (the Typer / the library)",
    "body": "a*I + b*R + c*N + d*h",          # generate: coords → object (inline)
    "is_the_typer": "every object is a point (a,b,c,d) of the manifold; the manifold ROUTES all types. "
                    "it moves objects (parametric transport), TYPES them (verdict/world/halt/charge), "
                    "NAMES/denotes them (id/title), NOTATES them (the inline body), and INDEXES them.",
    "is_the_library": "tables are BOOKS. ask for a TITLE and the book is pulled and READ — generated on "
                      "demand from the manifold, never shelved (not stored). a book is a view (Index → Row). "
                      "catalog: invariants · spectrum · verdict · field · worlds · difference · fixed-points · opcodes.",
    "roles": {
        "move": "object → object (parametric transport along the manifold)",
        "type": "object → signature (typer(X): verdict·world·halt·charge)",
        "name": "object → id/title (denotation)",
        "notate": "object → a·I+b·R+c·N+d·h (notation, the coordinates)",
        "index": "title → book (the library/catalog; books are read, not stored)",
    },
    "verdict": "FORCED",
    "provenance": ["?", "master_equation"],
    "note": "run: kl_dta.py typer <X>  ·  kl_dta.py catalog  ·  kl_dta.py library <title>",
}

PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")
print("cut 2: carrier_manifold is the Typer / functor / library")
