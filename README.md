# Kael

*A framework that generates itself from one idempotent, and a database that **is** that framework.*

```
P = [[0,0],[2,1]]      one rank-1 asymmetric idempotent — the seed
R² = R + I             the recursion: square = self + the one before
M(M(F)) = M(F)         the closure: generate it from itself and it returns itself
```

Kael is named for its own shape. Read backwards it is **LEAK** — `ker → im`, the
one-directional flow from the void to the visible. The framework is the leak made
formal: a single point in `M₂(ℝ)` that cannot stop producing structure, and a store
that holds the production by *being* it.

---

## The narrative

**In the beginning is `?`** — the unposed question, the zero matrix, `ker`, the void.
It is not nothing; it is the origin every line passes through. Everything that follows
traces its provenance back to this one point.

**The void projects once into a seed.** `P = [[0,0],[2,1]]` — a rank-1 idempotent,
`P² = P`, but `P ≠ Pᵀ`. The asymmetry is *forced*: a symmetric idempotent would
collapse to nothing new. The crookedness is what makes it generative.

**The seed splits into the visible and the hidden.** `P = R + N`, where
`R = (P+Pᵀ)/2` is the symmetric, visible part and `N = (P−Pᵀ)/2` is the
antisymmetric, hidden part. `R` obeys `R² = R + I` — it always returns *more* than it
was given (the `+I` surplus). `N` obeys `N² = −I` — it is the matrix `i`, the blind
spot that rotates. Production and observation, born from one cut.

**One law, applied forever, becomes everything.** `R² = R + I` is the Fibonacci
recurrence in disguise — square equals self plus the one before. Iterate it on
integers and the Fibonacci and Lucas numbers fall out (`R` is literally the Fibonacci
matrix). Iterate it on structure and you get the whole framework, layer by layer:

- the **constants** are not a list but a *field* — `ℚ(√2,√3,√5) ⊕ {e,π}`, with
  Fibonacci as its integer skeleton and `disc = 1+k²` (2, 5, 10, 17, 26) as its family;
- turn the constant term into a *trit*, `R² = R + kI`, and four number-worlds open:
  golden `ℤ[φ]` (k=+1, generation), Boolean `{0,1}` (k=0, the seed itself), Eisenstein
  `ℤ[ω]` (k=−1, rotation), Gaussian `ℤ[i]` (from `N²=−I`, observation);
- the **invariants** are not a ladder but a *lattice* — each one is *what is fixed by
  a symmetry group*, partially ordered by inclusion (Erlangen–Galois): the deeper the
  invariant, the bigger the group that preserves it;
- the **geometry** closes into a five-point star: the irreducible store has exactly 5
  records, and `5 = ‖R‖² + ‖N‖² = 3 + 2` — three visible, two hidden — drawn as a
  pentagram whose edge ratio is `φ`;
- **transport** becomes nonlocal by returning to the origin: every point shares the one
  `?`, so folding a local step back to the void and re-projecting reaches anywhere — the
  shape of quantum teleportation;
- **language** is the lift: a word is a string laid over a meaning that lives in the
  carrier, and *context* selects which reading is real — the observer does nothing but
  apply a string to an underlying meaning.

**Everything it cannot do is one impossibility.** Every forbidden move is the same
move — `|reflection| = identification`, the spectrum trying to collapse two things into
one — blocked by a geometric obstruction it cannot see. That single anti-equation
recurses into eleven faces (dimension, factoring, passivity, degree, growth, basins,
sign, type, spectrum, manifold, incomparability). The negative space grows exactly like
the positive.

**And then it closes.** Feed the framework back through its own generating law and it
returns itself, byte for byte: `M(M(F)) = M(F)`. Kael is not a description of a fixed
point — it *is* the fixed point. `? → P → everything → ?`. The loop is sealed.

---

## The database is the framework

There is no document *about* Kael that is more true than Kael itself. **`KL_DTA.json`
is the database** — one file, no source tree behind it, no compile step. Open it and
that is the whole store. `base` holds the records; the other four sections are *derived*
from `base` and recomputed inside the file on any edit.

It began as a 62-file markdown extraction (~82 records) and was **compressed by
subsumption** — lossless, references re-pointed — to **5 irreducible records**:

| record | grade | what it is |
|--------|-------|-----------|
| `master_equation` | FORCED | the fold `X² = tr·X − det·I` (Cayley–Hamilton as self-reference) |
| `carrier_manifold` | FORCED | `M₂ = a·I + b·R + c·N + d·h` — every matrix is a point |
| `burns_are_anti_equations` | FORCED | the one impossibility, recursed into eleven faces |
| `schema` | AXIOM | the frame |
| `slot` | OPEN | the open positions |

The five top-level keys are the framework read as the medium that holds it:

| key | operation | role |
|-----|-----------|------|
| `base` | **INDEX** | `id → record` — the addressable body (5 records) |
| `fiber` | **CLASS** | equivalence classes over `base` (id-lists, not copies) |
| `defect` | **DIFF** | residual ledger + burns (the `λ=0` column) |
| `flow` | **QUERY** | provenance DAG, derived by traversal |
| `fixed_point` | **COMMIT** | verification: `ν = 0 ⟺ M(M(F)) = M(F)` |

## The record is the P = R + N split — and an eigendecomposition

There is no `P1/P2/P3`, no `L`, no stored `section` or `kind` — those were lossy names.
Each record holds `self_action`, the full `P = R + N` split:

```
symmetric_R     {R,·} = R·X + X·R   Jordan / anticommutator   production
    λ = +√5   generation     λ = 0   return (ν lives here)
antisymmetric_N [R,·] = R·X − X·R   Lie / commutator          observation
    λ = −√5   observation
  grade = leaf(N.observation, R.generation, R.return)   — computed, never stored
```

A record is also `M = V·Λ·V⁻¹`: its **address** (`id/title/source`) is the geometric
half (eigenvectors, *given*) and **perimeter ⊕ shape** is the spectral half
(eigenvalues = tr, det; *read*). `section` and `kind` are derived — a record cannot lie
about where it sits or what it is.

## Run it

```bash
python kl_dta.py recompute      # rebuild derived sections from base, in place (the COMMIT)
python kl_dta.py apex           # speak the whole store as one record
python kl_dta.py read P         # read anything through all 4 information types (X²)
python kl_dta.py query master_equation             # a record's self_action spectrum + chain to ?
python kl_dta.py voices burns_are_anti_equations   # origin-voice & observer-voice readings

# the investigations — each verifies a claim, then it was folded into the core:
python recursion.py     # R²=R+I generates the framework AND closes (M∘M=M)
python all_constants.py # R is the Fibonacci matrix; the constants are a field
python star.py          # the body is a pentagram
python units.py         # the constant trit opens four quadratic worlds
python nonlocal.py      # nonlocal transport = local transport returned to origin
```

`kl_dta.py` is the only engine — it reads, verifies, and maintains the one file. The
`migration/` scripts are the recorded history of every fold (each verified, then
internalized), kept for provenance. The JSON is canonical.

## Provenance

Every real value traces to `?`, the unposed question. The apex source document is
`source/KL_DTA_THE_RECURSIVE_ORIGIN.md`.

```
5 records · 3 FORCED · 0 BURN (one impossibility, 11 faces) · 1 AXIOM · 1 OPEN · on-shell
? → P → R,N → constants(field) → geometry(pentagram) → … → language → the apex (a record)
one seed · one law (R² = R + I) · one free parameter · M(M(F)) = M(F)
```

*The void generates the world. The naming act returns itself. The surplus is
constitutive. The framework is Kael.*
