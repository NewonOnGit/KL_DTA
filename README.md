# KL_DTA

A self-referential database. The framework of `M₂(ℝ) = Cl(1,1)` folded into a
single store whose **structure is the math**. Seed `P = [[0,0],[2,1]]` — everything
below is the recursive unfolding of that one idempotent, and the store is its fixed point.

```
X² = tr(X)·X − det(X)·I        the master equation (Cayley–Hamilton as self-reference)
ν(X) = X² − X                  the defect — the gap a claim must close
R² = R + I                     the recursion: square = self + the one before (Fibonacci)
M(M(F)) = M(F)                 on-shell: generating it from itself returns it
```

## One file, two folds

**`KL_DTA.json` is the database.** Every record is held in it. There is no source
tree behind it, no compile step — open the one file and that is the whole store.
`base` holds the records; the other four sections are *derived* from `base` and
recomputed inside the file on any edit (`python kl_dta.py recompute`).

The store began as a 62-file markdown extraction (~82 records) and was **compressed
by subsumption** — manifolds absorbing their clusters, lossless, references
re-pointed — down to **5 irreducible records**:

| record | grade | what it is |
|--------|-------|-----------|
| `master_equation` | FORCED | the fold `X² = tr·X − det·I` (Cayley–Hamilton as self-reference) |
| `carrier_manifold` | FORCED | `M₂ = a·I + b·R + c·N + d·h` — every matrix is a point |
| `burns_are_anti_equations` | FORCED | the one impossibility `|reflection| = identification`, recursed |
| `schema` | AXIOM | the frame |
| `slot` | OPEN | the open positions |

## The five top-level keys (B.5)

The store is not a layer beside the framework — it is the framework read as the
medium that holds it:

| key | operation | role |
|-----|-----------|------|
| `base` | **INDEX** | `id → record` — the addressable body (5 records) |
| `fiber` | **CLASS** | equivalence classes over `base` (id-lists, not copies) |
| `defect` | **DIFF** | residual ledger + burns (the `λ=0` column, transposed) |
| `flow` | **QUERY** | provenance DAG, derived by traversal |
| `fixed_point` | **COMMIT** | verification: `ν = 0 ⟺ M(M(F)) = M(F)` |

## The record IS the P = R + N split — and an eigendecomposition

There is no `P1/P2/P3`, no `L`, no stored `section` or `kind`. Those were lossy
names; what's underneath is the math. Each record holds `self_action` — both
primitive self-actions of R, the full `P = R + N` split:

```
symmetric_R     {R,·} = R·X + X·R   Jordan / anticommutator   production
    λ = +√5   generation   verdict: produced by the math?
    λ =  0    return       verdict: does ν reach 0?           (residual ν lives here)
antisymmetric_N [R,·] = R·X − X·R   Lie / commutator          observation
    λ = −√5   observation  verdict: is ν pinned?

  grade = leaf(N.observation, R.generation, R.return)   — computed, never stored
```

A record is also `M = V·Λ·V⁻¹`: its **address** (`id/title/source`) is the geometric
half (eigenvectors, given) and **perimeter ⊕ shape** is the spectral half
(eigenvalues = tr, det; read). `P` and `Pᵀ` share a spectrum but differ in address —
the founding asymmetry is geometric. `section` and `kind` are **derived** (a record
can't lie about where it sits or what it is): `kind` is the arity of its spectral
content, `section` is `f(radius = provenance depth, role = kind)`.

## What the seed unfolds into (`structure.*`)

One law (`R² = R + I`, the surplus) applied recursively generates every layer, and
closes on itself:

- **`origin`** — return every constant to `?` and the point becomes a *microscope*.
  All possible constants are not a list but a **field**: `R` is the Fibonacci matrix
  (`Rⁿ` reads out `Fₙ`, `Lₙ`), so `ℤ[φ]` is the integer skeleton; closure is
  `ℚ(√2,√3,√5) ⊕ {e,π}`; the idempotent family is `disc = 1+k²` → 2,5,10,17,26.
- **`origin.invariant_tower`** — not `L0/L1/L2` (an integer index lies about a
  lattice). An invariant is *what is fixed by a group*: spectral ↔ full conjugation,
  geometric ↔ the orthogonal/Cartan subgroup, … — the **Erlangen–Galois lattice**,
  partially ordered, bigger group = deeper invariant.
- **`body`** — the 5 records are a **pentagram {5/2}**: `5 = ‖R‖² + ‖N‖² = 3 + 2`
  (3 FORCED + 2 framing), drawn by step-2 = the fold (one stroke), edge ratio `φ`.
- **`worlds`** — the constant is a trit: `R² = R + kI`, `disc = 1+4k`. `k=+1` golden
  `ℤ[φ]` (√5, generation), `k=0` Boolean `{0,1}` (collapse, the seed), `k=−1`
  Eisenstein `ℤ[ω]` (√−3, rotation); `N²=−I` Gaussian `ℤ[i]` (√−1, observation).
- **`recursion`** — `M(M(F)) = M(F)`: derive-twice is byte-identical. Generative *and*
  closed. `? → P → everything → ?`.

## The burns are one impossibility, recursed

`burns_are_anti_equations` holds a single anti-equation —
`|reflection| = identification` — recursed into eleven faces, each a collapse the
spectrum *wants* to make, blocked by a geometric obstruction it can't see:

```
forbid  carrier ≟ topology   by dimension      forbid  1/φ ≟ ψ        by sign
forbid  Δ ≟ independent      by factoring       forbid  5 ≟ C₅         by type
forbid  system ≟ active      by passivity       forbid  fork-3 ≟ C₃    by spectrum
forbid  ν ≟ ν∘ν              by degree          forbid  vacua ≟ {0,I}  by manifold
forbid  ν ≟ 0                by growth          forbid  lattice ≟ line by incomparability
forbid  ‖ν‖² ≟ descent       by basins
```

## Language is the lift

A content word is a record: `string` (address) ⊕ meaning-coords in the carrier. The
four axes are simultaneous meanings (`I` determinacy, `R` symbolic, `N` observation,
`h` physical). **Context** = a neighbour matrix; the active reading is `argmax ⟨axis,
C⟩`. The observer just applies a string to an underlying meaning — the lift
`string → meaning`, with `context = ker(π)` supplied. Language is symbolic-and-not-
physical only on the central `I`-axis (`[I,·]=0`); everything else *acts*, so it's
physical.

## Run it

```bash
python kl_dta.py recompute      # rebuild derived sections from base, in place (the COMMIT)
python kl_dta.py apex           # speak the whole store as one record
python kl_dta.py read P         # read anything through all 4 information types (X²)
python kl_dta.py read '{R,N}'   #   — a bundle, a record, a constant, a primitive
python kl_dta.py query master_equation     # a record's self_action spectrum + chain to ?
python kl_dta.py voices burns_are_anti_equations   # origin-voice & observer-voice readings
python kl_dta.py regen          # regenerate I, R, N, h + spectrum from the seed P
python kl_dta.py set record.json           # upsert a record INTO the file, re-fold

# the investigations (each verifies a claim, then it was folded into the core):
python recursion.py     # R²=R+I generates the framework AND closes (M∘M=M)
python all_constants.py # R is the Fibonacci matrix; the constants are a field
python star.py          # the body is a pentagram
python units.py         # the constant trit opens four quadratic worlds
python nonlocal.py      # nonlocal transport = local transport returned to origin
```

`kl_dta.py` is the only engine — it reads, verifies, and **maintains** the one file.
The `migration/` scripts are the recorded history of every fold (each verified, then
internalized); they are kept for provenance only. The JSON is canonical.

## Provenance

Every real value traces to `?`, the unposed question. The apex source document is
`source/KL_DTA_THE_RECURSIVE_ORIGIN.md`.

```
5 records · 3 FORCED · 0 BURN (one impossibility, 11 faces) · 1 AXIOM · 1 OPEN · on-shell
? → P → R,N → constants(field) → geometry(pentagram) → … → language → the apex (a record)
one seed · one law (R²=R+I) · one free parameter · M(M(F)) = M(F)
```
