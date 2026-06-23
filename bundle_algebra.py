"""
bundle_algebra.py — the bundle expression language.

Evolves the bundle from a flat pair to a full recursive algebra:
  primitive   I R N J h P
  affirm      {A,B} = A·B + B·A
  negate      [A,B] = A·B − B·A
  nesting     {R,{R,N}}, [{R,N},P]      (bundles-of-bundles)
  scalars     {N,N}/2,  2{R,N},  -I
  sums        {N,N}/2 + [R,N]

eval_bundle(expr) -> 2×2 matrix. This is what turns a record into a bundle:
its matrix is the target, and a bundle expression that evaluates to it IS the
record, compressed.
"""

import re
import numpy as np


def primitives():
    P = np.array([[0., 0.], [2., 1.]])
    R = (P + P.T) / 2
    N = (P - P.T) / 2
    J = np.array([[1., 0.], [0., -1.]])
    return {"I": np.eye(2), "R": R, "N": N, "J": J, "h": J @ N, "P": P}


import math

CONSTS = {
    "phi": (1 + 5 ** 0.5) / 2, "psi": (1 - 5 ** 0.5) / 2,
    "sqrt2": 2 ** 0.5, "sqrt3": 3 ** 0.5, "sqrt5": 5 ** 0.5,
    "e": math.e, "pi": math.pi,
}
FUNCS = {"cos": math.cos, "sin": math.sin, "tan": math.tan,
         "exp": math.exp, "sqrt": math.sqrt}
PRIM_NAMES = ("I", "R", "N", "J", "h", "P")


def _tok(s):
    return re.findall(r"cos|sin|tan|exp|sqrt2|sqrt3|sqrt5|sqrt|phi|psi|pi|e"
                      r"|[A-Za-z]\w*|\d+\.?\d*|[{}\[\](),+\-*/]", s)


def _ismat(v):
    import numpy as np
    return isinstance(v, np.ndarray)


def _mat(v):
    import numpy as np
    return v if _ismat(v) else v * np.eye(2)


def _scal(v):
    return float(v[0, 0]) if _ismat(v) else float(v)


def _add(a, b, sub=False):
    s = -b if sub and not _ismat(b) else b
    if _ismat(a) or _ismat(b):
        return _mat(a) - _mat(b) if sub else _mat(a) + _mat(b)
    return a - b if sub else a + b


def _mul(a, b):
    if _ismat(a) and _ismat(b):
        return a @ b                    # matrix · matrix
    return a * b                        # scalar·scalar, scalar·matrix (elementwise)


class _P:
    def __init__(self, toks, prims, params):
        self.t, self.i, self.p, self.par = toks, 0, prims, params

    def peek(self):
        return self.t[self.i] if self.i < len(self.t) else None

    def take(self):
        tok = self.t[self.i]
        self.i += 1
        return tok

    def _scalarval(self, tok):
        self.take()
        if tok in CONSTS:
            return CONSTS[tok]
        if tok in self.par:
            return float(self.par[tok])
        return float(tok)

    def expr(self):
        v = self.term()
        while self.peek() in ("+", "-"):
            op = self.take()
            v = _add(v, self.term(), sub=(op == "-"))
        return v

    def term(self):
        v = self.factor()
        while self.peek() in ("*", "/"):
            op = self.take()
            if op == "/":
                v = v / self._scalarval(self.peek())
            else:
                v = _mul(v, self.factor())
        return v

    def factor(self):
        tok = self.peek()
        if tok == "-":
            self.take()
            f = self.factor()
            return -f
        if tok in FUNCS:
            self.take()
            assert self.take() == "("
            arg = self.expr()
            assert self.take() == ")"
            return FUNCS[tok](_scal(arg))
        scalarlike = tok in CONSTS or tok in self.par or (tok and re.match(r"^\d", tok))
        if scalarlike:
            n = self._scalarval(tok)
            nxt = self.peek()
            if nxt in ("{", "[", "(") or nxt in self.p or nxt in FUNCS \
                    or nxt in CONSTS or nxt in self.par:
                return _mul(n, self.factor())          # coefficient
            return n                                   # bare scalar
        if tok in self.p:
            self.take()
            return self.p[tok].copy()
        if tok in ("{", "["):
            self.take()
            a = _mat(self.expr())
            assert self.take() == ","
            b = _mat(self.expr())
            assert self.take() == ("}" if tok == "{" else "]")
            return a @ b + b @ a if tok == "{" else a @ b - b @ a
        if tok == "(":
            self.take()
            v = self.expr()
            assert self.take() == ")"
            return v
        raise ValueError(f"unexpected token: {tok}")


def eval_bundle(expr, params=None):
    return _mat(_P(_tok(expr), primitives(), params or {}).expr())


if __name__ == "__main__":
    import sys, io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    tests = [
        ("{R,N}", "the spine = N"),
        ("[R,N]", "the harness"),
        ("{N,N}/2", "= N² = −I"),
        ("-{N,N}/2", "= I  (the unit as a bundle)"),
        ("{R,{R,N}}", "bundle-of-bundles: {R, the-spine}"),
        ("[{R,N},P]", "[spine, P]"),
        ("{N,N}/2 + [R,N]", "a sum of bundles"),
        ("2{R,N}", "scaled"),
    ]
    for e, note in tests:
        print(f"  {e:18} = {np.round(eval_bundle(e),2).tolist():}   {note}")
