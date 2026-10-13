import warnings

import numpy as np
from numpy import poly1d
from scipy.interpolate import lagrange

warnings.filterwarnings("ignore", category=DeprecationWarning)
np.set_printoptions(suppress=True)

u = poly1d([(-1) ** k for k in range(10, -1, -1)])
sequence = [u(j) for j in range(1, 13)]

# test case
# sequence = [1, 8, 27, 64, 125, 216]


class IntegerPolynomial:
    def __init__(self, coefs: list[int]):
        self.coefs = coefs

    def __call__(self, x: int):
        return sum([c * x**k for k, c in enumerate(self.coefs)])


def op(k) -> IntegerPolynomial:
    if k <= 0:
        raise ValueError()
    # create integer poly
    float_coefs = lagrange([i for i in range(1, k + 1)], sequence[: k + 1]).coef
    int_coefs = np.round(float_coefs)
    int_poly = IntegerPolynomial([int(c) for c in int_coefs[::-1]])
    for i in range(k):
        assert int_poly(i + 1) == sequence[i]

    return int_poly


def bop(k) -> int:
    if not np.isclose(op(k)(k + 1), sequence[k]):
        return int(op(k)(k + 1))
    return 0


s = 0
for k in range(1, len(sequence)):
    s += bop(k)
print(s)
