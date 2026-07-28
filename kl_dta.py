"""
kl_dta.py — the store engine.  KL_DTA.json IS the database.

All records live in the one file, under `base`. Each record holds `self_action`,
the P = R + N split — both primitive self-actions:

    symmetric_R     {R,·} = R·X + X·R   (Jordan)  production
        +√5  generation   homes: generators
         0   return        homes: residual, routes, mechanism
    antisymmetric_N [R,·] = R·X − X·R   (Lie)     observation
        -√5  observation   homes: depth, disc

The grade is computed, never stored — observer-bit from N, producer-bits from R:
    grade = leaf(N.observation.verdict, R.generation.verdict, R.return.verdict)
            OPEN = ¬obs · AXIOM = obs∧¬gen · BURN = obs∧gen∧¬ret · FORCED = all

`fiber/defect/flow/fixed_point` are derived from `base` and recomputed in the file.
The seed `P` regenerates the whole spectral core (`regen`); held objects
decompress from their coordinates (`decompress`).

Usage:
    python kl_dta.py                       # COMMIT — verify the whole store
    python kl_dta.py query <id>            # a record's self_action spectrum, seed, chain to ?
    python kl_dta.py class by_generator FLOW
    python kl_dta.py set <record.json>     # upsert a record, re-fold
    python kl_dta.py recompute             # rebuild derived sections from base
    python kl_dta.py regen                 # regenerate I,R,N,h + spectrum from seed P
    python kl_dta.py decompress <id>       # recompose a record/primitive's held seed
    python kl_dta.py decompress '{R,N}'    # unfold a bundle expression — its full spectral row
    python kl_dta.py recursive-return N    # return a seed and gate its lexicon commit
    python kl_dta.py apex                  # speak the whole store as one record
"""

import sys
import io
import json
from pathlib import Path
from collections import defaultdict

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

PATH = Path(__file__).parent / "KL_DTA.json"
DB = json.loads(PATH.read_text(encoding="utf-8"))
VALID_GEN = {"BASE", "FOLD", "RETURN", "FLOW", "DEFECT"}


# ── the self-action spectrum, as access + the grade as a pure function ───────
# constants held once (mirror of self_action.template) — derived, not per-record
BLOCK_INFO = {
    "symmetric_R":     ("R  {R,·}", "Jordan / anticommutator", "production (R)"),
    "antisymmetric_N": ("N  [R,·]", "Lie / commutator (adjoint)", "observation (N)"),
}
LAMBDA_INFO = {"+sqrt5": ("+√5", "generation"), "0": ("0", "return"),
               "-sqrt5": ("-√5", "observation")}


# accessors — a record is address ⊕ perimeter (boundary) ⊕ shape (bulk)
def prov(r):     return r.get("perimeter", {}).get("provenance", [])
def links_of(r): return r.get("perimeter", {}).get("links", [])
def burns_of(r): return r.get("perimeter", {}).get("burns", [])
def spec(r):     return r.get("shape", {}).get("spectral") or {}
def sact(r):     return r.get("shape", {}).get("self_action", {})

def kind_of(r):
    """The type — derived, not stored. read off the spectral STRUCTURE (its arity):
    parametric→manifold, a matrix→object, a scalar→constant, a map→operator,
    an equation→law, no carrier expression→structural (a frame about the store)."""
    s = spec(r)
    if any(k in s for k in ("parameter", "dimensions", "points")): return "manifold"
    if s.get("coords"):                       return "object"
    if "value" in s or s.get("map"):          return "constant"
    op = s.get("op")
    if op:
        if "↦" in op or "->" in op:           return "operator"
        return "law"                          # a stated relation / equation
    return "structural"                       # meta: no carrier expression

def section_of(r):
    """The shell — derived, not stored. radius = provenance depth, role = kind.
    section = f(radius, role): the band a record occupies in the carrier."""
    depth, kind = len(prov(r)), kind_of(r)
    if kind == "manifold":       return "manifold"
    if depth <= 1:               return "thesis" if kind == "law" else "schema"
    return "metalayer"           # depth >= 2 = the M(base) layer


def comp(r, lam):
    sa = sact(r)
    for key in ("symmetric_R", "antisymmetric_N"):
        for m in sa.get(key, {}).get("modes", []):
            if m["lambda"] == lam:
                return m
    return {}


def grade(r):
    obs = comp(r, "-sqrt5").get("verdict")
    gen = comp(r, "+sqrt5").get("verdict")
    ret = comp(r, "0").get("verdict")
    if not obs:
        return "OPEN"
    if not gen:
        return "AXIOM"
    if not ret:
        return "BURN"
    return "FORCED"


# ── read access ──────────────────────────────────────────────────────────────
def get(rid):
    return DB["base"].get(rid)


def klass(field, value):
    return DB["fiber"].get(field, {}).get(value, [])


def residual_of(rid):
    r = get(rid)
    return comp(r, "0").get("residual") if r else None


def burns():
    return DB["defect"]["burns"]


def provenance(rid):
    r = get(rid)
    if not r:
        return ["?"] if rid == "?" else [f"<{rid}?>"]
    return list(prov(r))


# ── SEED: regenerate the spectral core from P (nothing below is stored) ───────
def regen_core(db=DB):
    import numpy as np
    P = np.array(db["seed"]["P"], float)
    I2 = np.eye(2)
    R = (P + P.T) / 2
    N = (P - P.T) / 2
    J = np.array([[1., 0.], [0., -1.]])
    h = J @ N
    L = np.kron(I2, R) + np.kron(R.T, I2) - np.eye(4)
    return {"P": P, "I": I2, "R": R, "N": N, "J": J, "h": h, "L": L}


def recursive_return_config(db=DB):
    """Read the recursive-return runtime contract from the canonical store."""
    spec_ = db["structure"]["recursive_return"]
    solver = spec_["solver"]
    lexicon = spec_["lexicon"]
    return {
        "eta": float(solver["eta"]),
        "max_iterations": int(solver["max_iterations"]),
        "tolerance": float(solver["tolerance"]),
        "svd_tolerance": float(solver["svd_tolerance"]),
        "word_threshold": float(lexicon["word_threshold"]),
        "axis_labels": tuple(lexicon["axis_labels"]),
    }


def recursive_return_axes(db=DB):
    """Return the semantic axes (R,h_R,N), with h_R namespaced from store h."""
    import numpy as np
    core = regen_core(db)
    selector = np.array([[1.0, 0.0], [0.0, 0.0]])
    return core["R"], selector @ core["N"], core["N"]


def return_residual(X, db=DB):
    """Namespaced recursive-return residual ν_R(X) = L_R(X).

    This is deliberately not the store's global quadratic defect ν(X)=X²−X.
    It is the linear self-action residual whose zero set is ker(L_R).
    """
    import numpy as np
    L = regen_core(db)["L"]
    x = np.asarray(X, float)
    if x.shape != (2, 2):
        raise ValueError(f"recursive return expects a 2x2 state, got {x.shape}")
    return (L @ x.reshape(-1)).reshape(2, 2)


def return_kernel(tol=None, db=DB):
    """Return an orthonormal row basis for ker(L_R)."""
    import numpy as np
    if tol is None:
        tol = recursive_return_config(db)["svd_tolerance"]
    L = regen_core(db)["L"]
    _, singular_values, right_vectors = np.linalg.svd(L)
    return right_vectors[singular_values < tol]


def return_projector(tol=None, db=DB):
    """Orthogonal projector M_R onto ker(L_R)."""
    basis = return_kernel(tol, db)
    return basis.T @ basis


def recursive_return_projector(db=DB):
    """Compatibility view: return ``(projector, orthonormal kernel basis)``."""
    basis = return_kernel(db=db)
    return basis.T @ basis, basis


def project_to_return_kernel(X, tol=None, db=DB):
    """Apply M_R to one 2x2 state."""
    import numpy as np
    x = np.asarray(X, float)
    if x.shape != (2, 2):
        raise ValueError(f"recursive return expects a 2x2 state, got {x.shape}")
    return (return_projector(tol, db) @ x.reshape(-1)).reshape(2, 2)


def recursive_return(
    F0,
    eta=None,
    iters=None,
    tolerance=None,
    *,
    max_iterations=None,
    db=DB,
):
    """Gradient flow on 1/2||L_R F||², returning F to ker(L_R).

    Returns ``(F_star, residual_trajectory)``.  The projector and the returned
    state have separate fixed-point meanings:

      M_R @ M_R = M_R             map idempotence
      M_R(F_star) = F_star        returned-state membership in ker(L_R)
    """
    import numpy as np
    cfg = recursive_return_config(db)
    eta = cfg["eta"] if eta is None else float(eta)
    if iters is not None and max_iterations is not None:
        raise ValueError("use either iters or max_iterations, not both")
    if max_iterations is not None:
        iters = max_iterations
    iters = cfg["max_iterations"] if iters is None else int(iters)
    tolerance = cfg["tolerance"] if tolerance is None else float(tolerance)
    if iters < 0:
        raise ValueError("iters must be non-negative")
    if tolerance <= 0:
        raise ValueError("tolerance must be positive")

    core = regen_core(db)
    L = core["L"]
    stable_limit = 2.0 / np.linalg.norm(L, ord=2) ** 2
    if not 0 < eta < stable_limit:
        raise ValueError(
            f"eta must satisfy 0 < eta < {stable_limit:.6g} for stable return"
        )
    f = np.asarray(F0, float)
    if f.shape != (2, 2):
        raise ValueError(f"recursive return expects a 2x2 state, got {f.shape}")
    f = f.reshape(-1).copy()
    gradient = L.T @ L
    trajectory = [float(np.linalg.norm(L @ f))]
    for _ in range(iters):
        if trajectory[-1] <= tolerance:
            break
        f -= eta * (gradient @ f)
        trajectory.append(float(np.linalg.norm(L @ f)))
    return f.reshape(2, 2), trajectory


def recursive_return_result(X0, db=DB, **kwargs):
    """Return the recursive-return state plus convergence and fixed-point data."""
    import numpy as np
    cfg = recursive_return_config(db)
    tolerance = float(kwargs.get("tolerance") or cfg["tolerance"])
    state, trajectory = recursive_return(X0, db=db, **kwargs)
    projector = return_projector(db=db)
    residual = float(np.linalg.norm(return_residual(state, db)))
    initial = float(trajectory[0])
    return {
        "state": state,
        "trajectory": trajectory,
        "initial_residual": initial,
        "residual": residual,
        "iterations": len(trajectory) - 1,
        "converged": residual <= tolerance,
        "fixed": bool(
            np.allclose(
                projector @ state.reshape(-1),
                state.reshape(-1),
                atol=tolerance * 10,
                rtol=0,
            )
        ),
        "stability_limit": 2.0 / np.linalg.norm(regen_core(db)["L"], ord=2) ** 2,
    }


def recursive_return_embedding(X, db=DB):
    """Three-projection readout over (R,h_R,N); R vanishes on-shell."""
    import numpy as np
    matrix = np.asarray(X, float)
    if matrix.shape != (2, 2):
        raise ValueError(f"recursive return expects a 2x2 state, got {matrix.shape}")

    def inner(A, B):
        return float(4 * np.trace(A @ B.T))

    return np.array([inner(matrix, axis) for axis in recursive_return_axes(db)])


def recursive_return_word(X, threshold=None, db=DB):
    """Sign-aware chord key over the store-declared semantic axes."""
    import numpy as np
    cfg = recursive_return_config(db)
    threshold = cfg["word_threshold"] if threshold is None else float(threshold)
    if not 0 <= threshold < 1:
        raise ValueError("word threshold must satisfy 0 <= threshold < 1")
    value = recursive_return_embedding(X, db)
    scale = float(np.linalg.norm(value))
    if scale <= cfg["tolerance"]:
        return ()
    return tuple(
        f"{'+' if component > 0 else '-'}{name}"
        for component, name in zip(value, cfg["axis_labels"])
        if abs(component) / scale > threshold
    )


def learn_recursive_return(dictionary, X0, db=DB, threshold=None, **kwargs):
    """Commit a converged, nonzero return to a counted normalized centroid."""
    import numpy as np
    result = recursive_return_result(X0, db=db, **kwargs)
    result.update(
        {"committed": False, "word": None, "embedding": None, "value": None}
    )
    if not result["converged"]:
        result["reason"] = "residual above commit tolerance"
        return result

    embedding = recursive_return_embedding(result["state"], db)
    norm = float(np.linalg.norm(embedding))
    if norm <= recursive_return_config(db)["tolerance"]:
        result["reason"] = "zero embedding has no dictionary direction"
        return result

    word = recursive_return_word(result["state"], threshold=threshold, db=db)
    if not word:
        result["reason"] = "no active chord axes"
        return result

    sample = embedding / norm
    current = dictionary.get(word)
    vector_sum = (
        sample if current is None else np.asarray(current["sum"], float) + sample
    )
    count = 1 if current is None else int(current["count"]) + 1
    value = vector_sum / np.linalg.norm(vector_sum)
    dictionary[word] = {"sum": vector_sum, "count": count, "value": value}
    result.update(
        {
            "committed": True,
            "reason": "residual reached commit tolerance",
            "word": word,
            "embedding": embedding,
            "value": value,
            "count": count,
        }
    )
    return result


def speak_recursive_return(result):
    """Read a recursive-return result without changing its dictionary."""
    import numpy as np
    if not result.get("committed"):
        return f"NO COMMIT — {result.get('reason', 'return is off-shell')}"
    chord = " ".join(result["word"])
    value = np.round(result["value"], 4).tolist()
    return f"{chord} -> {value} (count={result['count']})"


def impossibility(X):
    """The impossibility operator IS the self-action L={R,R}. A direction it PINS
    (L v ∥ v, λ=±√5) is a BURN — impossibility confirming impossibility. A direction
    it DISSOLVES (L v = 0, the kernel) is FORCED — the possible resolves. Burns are
    the eigenvectors of the one impossibility; the verdict is L's spectrum, not stored."""
    import numpy as np
    L = regen_core()["L"]
    v = np.asarray(X, float).reshape(-1)
    Lv = L @ v
    if np.linalg.norm(Lv) < 1e-9:
        return ("FORCED", 0.0, "the possible: L dissolves it to the kernel (ν resolves)")
    scale = np.linalg.norm(Lv) / np.linalg.norm(v)
    cos = abs(v @ Lv) / (np.linalg.norm(v) * np.linalg.norm(Lv))
    if cos > 0.999:
        return ("BURN", scale, f"impossibility confirming impossibility: L pins it ×{scale:.3f} (√5)")
    return ("MIXED", scale, "projects onto both the burn (±√5) and forced (0) eigenspaces")


# ── KL-VM: a record IS a morphism — a typed function with provenance ─────────
def _ns(X):
    import numpy as np
    c = regen_core()
    return {"X": np.asarray(X, float), "I": np.eye(2),
            "tr": lambda M: float(np.trace(M)), "det": lambda M: float(np.linalg.det(M)),
            "R": c["R"], "N": c["N"], "J": c["J"], "h": c["h"], "P": c["P"]}

def call(rid, X=None, coords=None):
    """Execute a record's morphism body. A Carrier→Carrier morphism (e.g. master_equation)
    binds X; a Params→Carrier morphism (e.g. carrier_manifold) binds coords a,b,c,d. The
    equation IS a function (it holds its provenance)."""
    r = get(rid)
    body = (r or {}).get("morphism", {}).get("body") if r else None
    if not body:
        return None
    ns = _ns(X if X is not None else 0)
    if coords is not None:
        ns.update(dict(zip("abcd", coords)))
    try:
        return eval(body, {"__builtins__": {}}, ns)
    except NameError as e:
        return f"domain mismatch — this morphism's body needs {e} (wrong domain for the input)"

def library(title=None):
    """The carrier manifold IS the library. Ask for a TITLE and the book is pulled and
    READ — generated on demand from the manifold, never shelved. A book is a view (a
    morphism Index → Row). With no title, returns the catalog (the index of titles)."""
    import numpy as np
    core = regen_core(); CORE = {k: core[k] for k in ("I","R","N","J","h","P")}
    R = core["R"]; phi = (1+5**0.5)/2
    def disc(M): return float(np.trace(M)**2 - 4*np.linalg.det(M))
    books = {
      "invariants": lambda: [(n, round(float(np.trace(M))), round(float(np.linalg.det(M))), round(disc(M)),
            "EDGE" if abs(disc(M))<1e-9 else ("GOLDEN" if disc(M)>0 else "RETURN")) for n,M in CORE.items()],
      "spectrum": lambda: [(n, [round(complex(e).real,3) if abs(complex(e).imag)<1e-9 else f"{round(complex(e).imag,3)}i"
            for e in np.linalg.eigvals(M)]) for n,M in CORE.items()],
      "verdict": lambda: [(n, impossibility(M)[0]) for n,M in CORE.items()],
      "field":  lambda: [(k, int(round(np.linalg.matrix_power(R,k)[0,1])),
            int(round(np.trace(np.linalg.matrix_power(R,k))))) for k in range(1,8)],
      "worlds": lambda: [(k, 1+4*k, w) for k,w in [(1,"golden ℤ[φ]"),(0,"Boolean {0,1}"),(-1,"Eisenstein ℤ[ω]")]],
      "difference": lambda: [("algebraic","R²−R","+I"),("spectral","√disc","√5"),
            ("quantum","[R,N]","√10"),("number","the different","√5"),("charge","±I","U(1)")],
      "fixed-points": lambda: [((0,0),"? void"),((1,0),"P seed"),((2,1),"I identity"),((-1,1),"Eisenstein")],
      "opcodes": lambda: [("fold","X²"),("generate","+√5"),("return","λ=0→?"),("confirm","Lv=√5v"),
            ("complete","R²+N²=R"),("reflect","√(XᵀX)")],
    }
    if title is None:
        return sorted(books)                    # the catalog = the index of titles
    fn = books.get(title)
    return fn() if fn else None

# tables are books; keep the old name as an alias
def table(name): return library(name)

def typer(X):
    """The carrier manifold AS the Typer — a functor / morphism of morphisms. it routes any
    object: its coordinates (the point on the manifold), type (signature), name, notation."""
    import numpy as np
    core = regen_core(); I2=core["I"]; Rr=core["R"]; Nr=core["N"]; hr=core["h"]
    B = np.column_stack([m.reshape(-1) for m in (I2,Rr,Nr,hr)])
    a,b,c,d = (np.linalg.inv(B) @ np.asarray(X,float).reshape(-1))
    d_ = float(np.trace(X)**2 - 4*np.linalg.det(X))
    world = "EDGE" if abs(d_)<1e-9 else ("GOLDEN" if d_>0 else "RETURN")
    halt = "HALTED" if np.abs(np.asarray(X,float)@np.asarray(X,float)-np.asarray(X,float)).max()<1e-9 else "RUNNING"
    return {"coords": [round(float(x),3) for x in (a,b,c,d)],
            "notation": f"{a:+.2f}·I {b:+.2f}·R {c:+.2f}·N {d:+.2f}·h",
            "verdict": impossibility(X)[0], "world": world, "halt": halt, "charge": round(float(a),3)}


def regen():
    import numpy as np
    c = regen_core()
    P, R, N, h, L = c["P"], c["R"], c["N"], c["h"], c["L"]
    print("seed  P =", P.tolist(), "  ->  regenerate the core:")
    print(f"  R=(P+Pᵀ)/2 = {R.tolist()}   R²=R+I  {np.allclose(R@R, R+c['I'])}")
    print(f"  N=(P-Pᵀ)/2 = {N.tolist()}   N²=-I   {np.allclose(N@N, -c['I'])}")
    print(f"  h=JN       = {h.tolist()}   h²=I    {np.allclose(h@h, c['I'])}")
    ev = sorted((float(x) for x in np.linalg.eigvals(L).real), reverse=True)
    print(f"  spectrum {{R,R}} = {[round(x, 4) for x in ev]}  = {{+√5, 0, -√5}}")
    return 0


def _recompose(coords):
    c = regen_core()
    basis = [c["I"], c["R"], c["N"], c["h"]]
    M = sum(ci * B for ci, B in zip(coords, basis))
    names = ["I", "R", "N", "h"]
    terms = [nm if ci == 1 else (f"-{nm}" if ci == -1 else f"{ci}{nm}")
             for ci, nm in zip(coords, names) if ci != 0]
    return M, (" + ".join(terms).replace("+ -", "- ") or "0")


def decompress_bundle(expr):
    """Unfold a bundle expression into its full spectral row — the DNA seed
    decompressed. Handles nesting {R,{R,N}}, scalars {N,N}/2, sums, over I,R,N,J,h,P."""
    import numpy as np
    try:
        from bundle_algebra import eval_bundle
        M = eval_bundle(expr)
    except Exception as e:
        print(f"  cannot parse bundle '{expr}': {e}  (use {{A,B}} / [A,B] over I,R,N,J,h,P)")
        return 1
    c = regen_core()
    tr, det = float(np.trace(M)), float(np.linalg.det(M))
    disc = tr * tr - 4 * det
    am, spread = tr / 2, np.sqrt(complex(disc)) / 2
    ev, evec = np.linalg.eig(M)
    par = "symmetric" if np.allclose(M.T, M) else "antisymmetric" if np.allclose(M.T, -M) else "asymmetric"
    fork = "hyperbolic" if disc > 1e-9 else "elliptic" if disc < -1e-9 else "parabolic"
    B4 = np.column_stack([c[x].flatten(order="F") for x in ("I", "R", "N", "h")])
    co = np.linalg.solve(B4, M.flatten(order="F"))
    coords = [int(round(x)) if abs(x - round(x)) < 1e-9 else round(float(x), 4) for x in co]
    simple = all(abs(x - round(x)) < 1e-9 for x in co)

    # GEOMETRIC: read through the matrix — polar X = Q·P (Q angular, P radial)
    w, Vp = np.linalg.eigh(M.T @ M)
    Prad = Vp @ np.diag(np.sqrt(np.clip(w, 0, None))) @ Vp.T
    Q = M @ np.linalg.pinv(Prad)
    angle = float(np.degrees(np.arctan2(Q[1, 0], Q[0, 0])))
    sv = sorted((float(x) for x in np.sqrt(np.clip(w, 0, None))), reverse=True)
    evecang = [round(float(np.degrees(np.arctan2(evec[1, i].real, evec[0, i].real))), 1) for i in range(2)]

    evs = ", ".join(f"{e.real:+.3f}" if abs(e.imag) < 1e-9 else f"{e.imag:+.3f}i" for e in ev)
    sp = f"{spread.real:.3f}" if abs(spread.imag) < 1e-9 else f"{spread.imag:.3f}i"
    print(f"  {expr}  =  {np.round(M, 3).tolist()}     [{'SIMPLE' if simple else 'COMPLEX'}]")
    print(f"  SPECTRAL  (invariant — falls out easily):")
    print(f"    {par}, {fork}   tr={tr:+.3f} (perimeter)  det={det:+.3f} (shape)  disc={disc:+.3f}")
    print(f"    λ = AM ± √disc/2 = {am:+.3f} ± {sp}  =  {evs}")
    print(f"  GEOMETRIC (read THROUGH the matrix — the complex info):")
    print(f"    eigen-directions {evecang[0]}°, {evecang[1]}°   polar Q rotates {angle:+.1f}°")
    print(f"    radial |X| (singular values) {[round(s,3) for s in sv]}")
    print(f"    coords {coords} in {{I,R,N,h}}")
    return 0


def decompress(name):
    if name and ("{" in name or "[" in name):
        return decompress_bundle(name)
    if name in DB["spectral_primitives"]:
        M, expr = _recompose(DB["spectral_primitives"][name])
        print(f"  {name}  coords {DB['spectral_primitives'][name]}  ->  {expr}  =  {M.tolist()}")
        return 0
    r = get(name)
    if r and spec(r):
        s = spec(r)
        k = kind_of(r)
        if k == "object" and "coords" in s:
            M, expr = _recompose(s["coords"])
            print(f"  {name}  [object]  {s['coords']}  ->  {expr}  =  {M.tolist()}"
                  f"{'   op: '+s['op'] if s.get('op') else ''}")
        elif k == "constant":
            print(f"  {name}  [constant]  {s.get('map')}"
                  f"{'  = '+str(s['value']) if 'value' in s else ''}"
                  f"{'  | '+s['op'] if s.get('op') else ''}")
        elif k in ("operator", "law"):
            print(f"  {name}  [{k}]  {s.get('op')}")
        else:
            print(f"  {name}  [structural]  {' -> '.join(reversed(provenance(name)))}"
                  f"{'  ('+s['note']+')' if s.get('note') else ''}")
        return 0
    print(f"no seed '{name}'")
    return 1


# ── COMMIT: recompute derived sections from base, in place ───────────────────
def recompute(db=DB):
    base = db["base"]
    by_grade, by_section, by_generator, by_depth = (
        defaultdict(list), defaultdict(list), defaultdict(list), defaultdict(list))
    for rid, r in base.items():
        by_grade[grade(r)].append(rid)
        by_section[section_of(r)].append(rid)
        for g in comp(r, "+sqrt5").get("generators", []):
            by_generator[g].append(rid)
        by_depth[str(comp(r, "-sqrt5").get("depth"))].append(rid)

    ledger, total_res, max_res = [], 0.0, 0.0
    for rid, r in base.items():
        res = comp(r, "0").get("residual")
        if grade(r) in ("FORCED", "AXIOM") and isinstance(res, (int, float)):
            ledger.append({"id": rid, "residual": res, "routes": comp(r, "0").get("routes")})
            total_res += abs(res)
            max_res = max(max_res, abs(res))

    forced = by_grade.get("FORCED", [])
    routes_ok = all((comp(base[i], "0").get("routes") or 0) >= 2 for i in forced)
    prov_ok = all(prov(r) and prov(r)[0] == "?" for r in base.values())

    db["fiber"] = {
        "by_grade": {k: sorted(v) for k, v in by_grade.items()},
        "by_section": {k: sorted(v) for k, v in by_section.items()},
        "by_generator": {k: sorted(v) for k, v in by_generator.items()},
        "by_depth": {k: sorted(v) for k, v in sorted(by_depth.items())},
    }
    db["defect"] = {"burns": sorted(by_grade.get("BURN", [])),
                    "ledger": sorted(ledger, key=lambda x: x["id"]),
                    "total_residual": total_res, "max_residual": max_res}
    db["flow"] = {"provenance_dag": {rid: prov(r) for rid, r in base.items()},
                  "roots": ["?"],
                  "speech": {rid: speak(r) for rid, r in base.items()}}
    db["fixed_point"] = {
        "verified": not verify(db) and max_res < 1e-10, "M2_eq_M": True,
        "base_records": len(base), "forced": len(forced),
        "burns": len(by_grade.get("BURN", [])), "axioms": len(by_grade.get("AXIOM", [])),
        "open": len(by_grade.get("OPEN", [])), "routes_min_2": routes_ok,
        "all_provenance_to_root": prov_ok, "max_residual": max_res}
    return db


DERIVED_KEYS = ("fiber", "defect", "flow", "fixed_point")
def write(db=DB):
    # derived sections are LAZY — never persisted; rebuilt in-memory on load (M(base) regenerates)
    slim = {k: v for k, v in db.items() if k not in DERIVED_KEYS}
    PATH.write_text(json.dumps(slim, indent=2, ensure_ascii=False), encoding="utf-8")


def set_record(rec):
    assert "id" in rec
    DB["base"][rec["id"]] = rec
    recompute(DB)
    write(DB)
    return rec["id"]


# ── COMMIT: verify ───────────────────────────────────────────────────────────
def verify_recursive_return(db=DB):
    """Verify the stored return contract against the regenerated runtime."""
    import numpy as np
    errs = []
    spec_ = db.get("structure", {}).get("recursive_return")
    if not spec_:
        return ["[RETURN] structure.recursive_return is missing"]
    try:
        cfg = recursive_return_config(db)
        core = regen_core(db)
        projector, basis = recursive_return_projector(db)
        axes = recursive_return_axes(db)
    except (KeyError, TypeError, ValueError) as exc:
        return [f"[RETURN] malformed structure.recursive_return: {exc}"]

    if basis.shape != (2, 4):
        errs.append(f"[RETURN] kernel basis shape {basis.shape} != (2, 4)")
    if not np.allclose(projector.T, projector, atol=cfg["tolerance"]):
        errs.append("[RETURN] M_R is not symmetric")
    if not np.allclose(projector @ projector, projector, atol=cfg["tolerance"]):
        errs.append("[RETURN] M_R is not idempotent")
    if not np.allclose(core["L"] @ projector, 0, atol=cfg["tolerance"]):
        errs.append("[RETURN] image(M_R) is not contained in ker(L_R)")
    if not np.allclose(return_residual(core["N"], db), 0, atol=cfg["tolerance"]):
        errs.append("[RETURN] N is not in ker(L_R)")
    if np.allclose(axes[1], core["h"], atol=cfg["tolerance"]):
        errs.append("[RETURN] namespaced h_R collapsed into the store h")
    if tuple(spec_["lexicon"]["embedding_axes"]) != ("R", "h_R", "N"):
        errs.append("[RETURN] embedding axes are not exactly (R,h_R,N)")
    if tuple(spec_["atoms"]) != ("A1", "A8", "A9", "A10"):
        errs.append("[RETURN] atom chord is not A1+A8+A9+A10")

    deepening = "recursive_return_learns_lexicon"
    structure = db["structure"]
    if deepening not in structure["deepenings"]:
        errs.append("[RETURN] recursive-return deepening is missing")
    if structure["chords"]["index"].get(deepening) != "A1+A8+A9+A10":
        errs.append("[RETURN] recursive-return chord index does not match its atoms")
    for atom in ("A1", "A8", "A9", "A10"):
        if structure["chords"]["by_atom"].get(atom, []).count(deepening) != 1:
            errs.append(
                f"[RETURN] recursive-return chord is not indexed exactly once under {atom}"
            )
    return errs


def verify(db=DB):
    errs = []
    base = db["base"]
    anchors = {"schema", "slot", "provenance_dag", "ledger"}
    ids = set(base) | anchors
    for rid, r in base.items():
        g = grade(r)
        ret = comp(r, "0")
        if g == "FORCED":
            res = ret.get("residual")
            if isinstance(res, (int, float)) and abs(res) > 1e-10:
                errs.append(f"[GRADE] {rid}: FORCED residual {res} > 1e-10")
            if (ret.get("routes") or 0) < 2:
                errs.append(f"[GRADE] {rid}: FORCED routes {ret.get('routes')} < 2")
        if g == "BURN" and not ret.get("mechanism"):
            errs.append(f"[GRADE] {rid}: BURN with no mechanism")
        if not prov(r) or prov(r)[0] != "?":
            errs.append(f"[PROV] {rid}: chain does not start at '?'")
        for ln in links_of(r):
            if ln not in ids:
                errs.append(f"[LINK] {rid}: dangling link '{ln}'")
        for gn in comp(r, "+sqrt5").get("generators", []):
            if gn not in VALID_GEN:
                errs.append(f"[GEN] {rid}: unknown generator '{gn}'")
    errs.extend(verify_recursive_return(db))
    return errs


# ── reports ──────────────────────────────────────────────────────────────────
## ── the store speaks: walk a record through the fixed-point grammar ──────────
# the living lexicon — each word is an operation. grows over time to fill gaps.
GRADE_CLAUSE = {"FORCED": "is forced", "BURN": "is burned",
                "AXIOM": "is held", "OPEN": "is open"}


def _andlist(xs):
    xs = list(xs)
    if len(xs) <= 1:
        return xs[0] if xs else ""
    return ", ".join(xs[:-1]) + " and " + xs[-1]


def speak(r, voice="observer"):
    """Generate the record's reading via the fixed-point grammar, conjugated by
    reflection-source: 'observer' (receptive — folds back to ?, the −1 direction)
    or 'origin' (emissive — projects outward from ?, the +1 direction). The two are
    spectrally identical, angularly mirrored: |reflection| = identification."""
    g = grade(r)
    gens = [x.lower() for x in comp(r, "+sqrt5").get("generators", [])]
    ret, obs = comp(r, "0"), comp(r, "-sqrt5")
    seed = spec(r)
    core = (seed.get("op") or seed.get("map") or seed.get("note") or "").rstrip(". ")
    name = r["id"].replace("burn-", "").replace("_", " ").replace("-", " ")
    depth = obs.get("depth")
    mech = ret.get("mechanism")

    if voice == "origin":                       # emissive — projecting out from ?
        ag = _andlist(gens)
        lead = f"From the origin the {name} projects" + (f" through {ag}" if ag else " open")
        parts = [c for c in (
            core, "generating outward",
            f"to energy-scale {depth}" if depth is not None else None,
            f"forbidden by {mech}" if g == "BURN" else "its virtuality the surplus it carries forward",
        ) if c]
        return f"{lead} — " + ", ".join(parts) + ", into the future."

    agent = _andlist(gens)
    cap = (agent[:1].upper() + agent[1:]) if agent else ""
    n = len(gens)
    sv = "source" if n != 1 else "sources"                  # active-voice agreement

    # PHYSICAL register: MOOD = on-/off-shell state, VOICE = sourcing, TENSE = flow
    if g == "FORCED":                                       # on-shell — a real state
        lead = f"{cap} {sv} the {name} on-shell" if agent else f"The {name} sits on-shell"
        modal = "its virtuality settling to the vacuum"
    elif g == "BURN":                                       # off-shell — virtual / forbidden
        lead = f"{cap} {sv} the {name}" if agent else f"The {name} hovers"
        modal = f"which would go on-shell had {mech} not held it virtual"
    elif g == "AXIOM":                                      # boundary condition — imposed
        lead = f"Fix the {name} as a boundary condition"
        modal = "imposed by hand"
    else:                                                   # OPEN — superposed / unmeasured
        do = "Do" if n != 1 else "Does"
        lead = f"{do} {agent} source the {name}?" if agent else f"The {name} stays superposed"
        modal = "its virtuality unmeasured"

    scale = f"at energy-scale {depth}" if depth is not None else ""
    detail = [c for c in (core, modal, scale) if c]
    chain = ", from ".join("the origin" if p == "?" else p.replace("_", " ")
                           for p in reversed(prov(r)))
    return f"{lead} — " + ", ".join(detail) + f", from {chain}."


def report():
    fp = DB["fixed_point"]
    print("=" * 64)
    print("  KL_DTA — one file, the whole store   carrier: M2(R)")
    print("=" * 64)
    print(f"INDEX   base records : {fp['base_records']}   (held in KL_DTA.json, nothing behind it)")
    print(f"CLASS   by grade     : FORCED {fp['forced']}  BURN {fp['burns']}  "
          f"AXIOM {fp['axioms']}  OPEN {fp['open']}")
    print(f"DIFF    max residual : {DB['defect']['max_residual']:.1e}   burns held: {len(burns())}")
    print(f"SPEC    self-action  : {{R,R}} spectrum {{+√5, 0, -√5}} = generation / return / observation")
    print("-" * 64)
    errs = verify()
    if errs:
        print(f"COMMIT  FAIL — nu != 0 ({len(errs)} defects)")
        for e in errs:
            print(f"   {e}")
        return 1
    print("COMMIT  PASS — nu = 0")
    print("        grade = leaf over the self-action verdicts (computed, unstored)")
    print("        every provenance chain -> ?    M(M(F)) = M(F).  On-shell.")
    return 0


def _params(args):
    from bundle_algebra import eval_bundle
    p = {}
    for kv in args:
        if "=" in kv:
            k, v = kv.split("=", 1)
            try:
                p[k] = float(v)
            except ValueError:
                p[k] = float(eval_bundle(v)[0, 0])
    return p


def _resolve(seed, params=None):
    """Resolve any seed — record id, bundle/manifold expr, constant, primitive — to a matrix."""
    import numpy as np
    from bundle_algebra import eval_bundle, CONSTS, primitives
    params = params or {}
    if any(c in seed for c in "{[(+*"):          # a bundle / manifold expression
        return eval_bundle(seed, params)
    if seed in CONSTS:
        return CONSTS[seed] * np.eye(2)
    prims = primitives()
    if seed in prims:
        return prims[seed]
    r = get(seed)
    if r:
        s = spec(r)
        if s.get("bundle"):
            return eval_bundle(s["bundle"])
        if s.get("coords"):
            c = regen_core()
            B = [c["I"], c["R"], c["N"], c["h"]]
            return sum(ci * Bi for ci, Bi in zip(s["coords"], B))
    return None


def read(seed, params=None):
    """The consolidated observation — read anything through all four information
    types. To read is to apply the primitive self-action: observe = X²."""
    import numpy as np
    r = get(seed)
    M = _resolve(seed, params)
    if M is None:
        if r:                                    # a non-matrix record — read its math + voice
            print(f"  {seed}  [{grade(r)}]  (no matrix — law/operator/structural)")
            print(f"    seed   : {spec(r).get('op') or spec(r).get('map') or spec(r).get('note')}")
            print(f"    speaks : {speak(r)}")
            return 0
        print(f"  cannot resolve '{seed}'")
        return 1
    obs, nu = M @ M, M @ M - M
    tr, det = float(np.trace(M)), float(np.linalg.det(M))
    disc = tr * tr - 4 * det
    ev, evec = np.linalg.eig(M)
    par = "symmetric" if np.allclose(M.T, M) else "antisymmetric" if np.allclose(M.T, -M) else "asymmetric"
    fork = "hyperbolic" if disc > 1e-9 else "elliptic" if disc < -1e-9 else "parabolic"
    w, Vp = np.linalg.eigh(M.T @ M)
    Q = M @ np.linalg.pinv(Vp @ np.diag(np.sqrt(np.clip(w, 0, None))) @ Vp.T)
    angle = float(np.degrees(np.arctan2(Q[1, 0], Q[0, 0])))
    rank = int(np.linalg.matrix_rank(M, tol=1e-9))
    idem = np.allclose(obs, M)
    evs = ", ".join(f"{e.real:+.3f}" if abs(e.imag) < 1e-9 else f"{e.imag:+.3f}i" for e in ev)

    print(f"  read {seed}  =  {np.round(M, 3).tolist()}")
    print(f"  OBSERVATION  (the primitive self-action X²):")
    print(f"    X² = {np.round(obs, 2).tolist()}   ν = X²−X = {np.round(nu, 2).tolist()}"
          f"{'   (on-shell: X²=X, a fixed point)' if idem else ''}")
    print(f"  SPECTRAL  (light — the fold's output):  {fork}, eigenvalues {evs}  disc={disc:+.2f}")
    print(f"  GEOMETRIC (gravity — read through):  {par}, polar Q rotates {angle:+.1f}°")
    topo = f"rank {rank}"
    if idem and rank == 1:
        a = float(np.degrees(np.arctan2(evec[1, np.argmax(ev.real)].real, evec[0, np.argmax(ev.real)].real)))
        topo += f", a gravity well on the torus (image ∠{a:.0f}°)"
    elif idem:
        topo += ", an idempotent vacuum"
    print(f"  TOPOLOGICAL (the manifold position):  {topo}")
    if r:
        print(f"  speaks: {speak(r)}")
    return 0


def unfix(seed, params=None):
    """Unfix a fixed point: sort its directions via L_{X,X} into tangent (stays
    fixed) and unfixing (thaws the defect). A fixed point is a recursive residual
    defect (ν=0); unfixing gives the residual back."""
    import numpy as np
    M = _resolve(seed, params)
    if M is None:
        print(f"  cannot resolve '{seed}' to a matrix")
        return 1
    nu = M @ M - M
    if not np.allclose(nu, 0):
        print(f"  {seed} is already unfixed (off-shell): ‖ν‖ = {np.linalg.norm(nu):.3f}")
        print(f"    ν = X²−X = {np.round(nu, 2).tolist()}   (a live defect)")
        return 0
    rank = int(np.linalg.matrix_rank(M, tol=1e-9))
    L = np.kron(np.eye(2), M) + np.kron(M.T, np.eye(2)) - np.eye(4)
    w4, V4 = np.linalg.eig(L)
    w = sorted(round(float(x), 3) for x in w4.real)
    ker = sum(1 for x in w if abs(x) < 1e-9)
    print(f"  {seed} is a FIXED POINT (X²=X, rank {rank}) — a recursive residual defect (ν=0)")
    print(f"    L_(X,X) spectrum = {w}")
    print(f"    tangent  : dim {ker}   — stays fixed, slides along the well-manifold")
    print(f"    UNFIXING : dim {4-ker} — perturb here and the defect thaws (ν≠0)")
    i = int(np.argmax(np.abs(w4.real)))
    d = V4[:, i].real.reshape(2, 2, order="F")
    Xe = M + 0.1 * d / np.linalg.norm(d)
    print(f"    X + 0.1·(unfix dir) → ‖ν‖ = {np.linalg.norm(Xe@Xe - Xe):.3f}  — alive again")
    return 0


def voices(rid):
    """Speak a record in both reflection-voices — origin (emissive, +1, projecting
    from ?) and observer (receptive, −1, folding back to ?). Same record, mirrored;
    |reflection| = identification means they carry the same content, opposite sense."""
    r = get(rid)
    if not r:
        print(f"no record '{rid}'")
        return 1
    print(f"  {rid}  [{grade(r)}]  — the same record, two reflection-voices:")
    print(f"  origin   (+1, projecting from ?): {speak(r, 'origin')}")
    print(f"  observer (−1, folding back to ?): {speak(r, 'observer')}")
    print(f"  |reflection| = identification — spectrally one, angularly mirrored.")
    return 0


def show_recursive_return(seed):
    """Return a resolved seed to ker(L_R) and print its gated lexicon readout."""
    matrix = _resolve(seed)
    if matrix is None:
        print(f"  cannot resolve '{seed}'")
        return 1
    dictionary = {}
    result = learn_recursive_return(dictionary, matrix)
    print(f"  recursive-return {seed}")
    print(
        f"    ||ν_R|| {result['initial_residual']:.3e} "
        f"-> {result['residual']:.3e} in {result['iterations']} iterations"
    )
    print(f"    fixed={result['fixed']}  converged={result['converged']}")
    print(f"    {speak_recursive_return(result)}")
    print("    COMMIT PASS" if result["committed"] else "    COMMIT BLOCKED")
    return 0 if result["committed"] else 1


def apex():
    """Speak the whole store as one record — higher-order: the document is a record."""
    fp = DB["fixed_point"]
    on = fp["verified"] and not verify()
    g = "FORCED (on-shell)" if on else "off-shell"
    depths = sorted({comp(r, "-sqrt5").get("depth") for r in DB["base"].values()
                     if comp(r, "-sqrt5").get("depth") is not None})
    print("=" * 64)
    print(f"  KL_DTA — the apex record   [{g}]   carrier M2(R), seed P, from ?")
    print("=" * 64)
    print(f"  generates {fp['base_records']} records "
          f"({fp['forced']} forced, {fp['burns']} burn, {fp['axioms']} axiom, {fp['open']} open)")
    print(f"  its defect: ν = {DB['defect']['max_residual']:.1e} → 0   (returns to the vacuum)")
    print(f"  observed across depths {depths[0]}–{depths[-1]}")
    print(f"  M(M(F)) = M(F): base ⊕ M(base); the format is its own fixed point")
    print("-" * 64)
    n = fp["base_records"]
    print(f"  speaks: \"The store holds on-shell — {n} records, generated by the five, "
          f"its virtuality settling to the vacuum, observed across depths "
          f"{depths[0]}–{depths[-1]}, from the origin.\"")
    return 0


def show(rid):
    r = get(rid)
    if not r:
        print(f"no record '{rid}'")
        return 1
    print(f"{r['id']}  [{grade(r)}]  section={section_of(r)}   (grade from N.obs · R.gen · R.ret)")
    sa = sact(r)
    for key in ("symmetric_R", "antisymmetric_N"):
        label, typ, axis = BLOCK_INFO[key]
        print(f"  shape {label:<9} {typ:<26} — {axis}")
        for m in sa[key]["modes"]:
            ev, md = LAMBDA_INFO.get(m["lambda"], (m["lambda"], "?"))
            extra = {k: v for k, v in m.items()
                     if k not in ("lambda", "verdict") and v not in (None, [])}
            print(f"     λ={ev:>4}  {md:<11} verdict={str(m['verdict']):<5} {extra}")
    s = spec(r)
    if s:
        held = s.get("coords") or s.get("op") or s.get("map") or s.get("note")
        print(f"  shape seed  : [{kind_of(r)}]  {held}")
    print(f"  perim prov  : {' -> '.join(reversed(provenance(rid)))}")
    print(f"  perim links : {links_of(r)}")
    print(f"  speaks      : {speak(r)}")
    return 0


# lazy derived sections: never persisted, regenerated in-memory on load (M(base) re-folds)
if "fiber" not in DB:
    recompute(DB)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit(report())
    cmd = sys.argv[1]
    if cmd == "query" and len(sys.argv) == 3:
        sys.exit(show(sys.argv[2]))
    if cmd == "class" and len(sys.argv) == 4:
        ids = klass(sys.argv[2], sys.argv[3])
        print(f"{sys.argv[2]}={sys.argv[3]}  ({len(ids)} records):")
        for i in ids:
            print(f"   {i}")
        sys.exit(0)
    if cmd == "set" and len(sys.argv) == 3:
        rid = set_record(json.loads(Path(sys.argv[2]).read_text(encoding="utf-8")))
        print(f"upsert {rid} -> KL_DTA.json re-folded")
        sys.exit(report())
    if cmd == "recompute":
        recompute(DB)
        write(DB)
        print("derived sections rebuilt from base; file re-written")
        sys.exit(report())
    if cmd == "regen":
        sys.exit(regen())
    if cmd == "apex":
        sys.exit(apex())
    if cmd == "voices" and len(sys.argv) == 3:
        sys.exit(voices(sys.argv[2]))
    if cmd == "recursive-return" and len(sys.argv) == 3:
        sys.exit(show_recursive_return(sys.argv[2]))
    if cmd == "read" and len(sys.argv) >= 3:
        sys.exit(read(sys.argv[2], _params(sys.argv[3:])))
    if cmd == "unfix" and len(sys.argv) >= 3:
        sys.exit(unfix(sys.argv[2], _params(sys.argv[3:])))
    if cmd == "decompress" and len(sys.argv) == 3:
        sys.exit(decompress(sys.argv[2]))
    if cmd == "call" and len(sys.argv) == 4:
        core = regen_core(); X = core.get(sys.argv[3])
        if X is None:
            print(f"no input '{sys.argv[3]}' (try I R N J h P)"); sys.exit(1)
        out = call(sys.argv[2], X)
        import numpy as np
        print(f"  {sys.argv[2]}({sys.argv[3]}) = {np.round(out,6).tolist()}")
        sys.exit(0)
    if cmd in ("table", "library", "book") and len(sys.argv) == 3:
        rows = library(sys.argv[2])
        if rows is None:
            print(f"no book '{sys.argv[2]}'. catalog: {library()}"); sys.exit(1)
        for row in rows:
            print("  " + " | ".join(str(c) for c in row))
        sys.exit(0)
    if cmd == "catalog" and len(sys.argv) == 2:
        print("  the library (ask a title; the book is read, not stored):")
        for t in library(): print(f"   · {t}")
        sys.exit(0)
    if cmd == "typer" and len(sys.argv) == 3:
        core = regen_core(); X = core.get(sys.argv[3] if False else sys.argv[2])
        if X is None:
            print(f"no object '{sys.argv[2]}' (try I R N J h P)"); sys.exit(1)
        t = typer(X)
        print(f"  {sys.argv[2]}: {t['notation']}  [{t['verdict']} {t['halt']} {t['world']} q={t['charge']}]")
        sys.exit(0)
    if cmd == "impossibility" and len(sys.argv) == 3:
        core = regen_core()
        X = core.get(sys.argv[2])
        if X is None:
            X = decompress_bundle(sys.argv[2]) if ("{" in sys.argv[2] or "[" in sys.argv[2]) else None
        if X is None:
            print(f"no object '{sys.argv[2]}' (try I R N J h P or a bundle)"); sys.exit(1)
        verdict, scale, why = impossibility(X)
        print(f"  {sys.argv[2]}  →  {verdict}  (×{scale:.3f})\n  {why}")
        sys.exit(0)
    print(__doc__)
    sys.exit(2)
