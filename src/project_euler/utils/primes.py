import numba
import numpy as np
from numba import njit, types
from numba.typed import Dict


# TODO: benchmark if these matter
@njit(nogil=True, parallel=True, fastmath=True)
def build_sieve(n: int) -> np.ndarray:
    primes = np.full(n, True)
    primes[0], primes[1] = False, False
    for i in numba.prange(2, int(np.sqrt(n) + 1)):
        if primes[i]:
            primes[i * i :: i] = False
    return np.flatnonzero(primes)


@njit(nogil=True)
def build_spf_sieve(n: int) -> np.ndarray:
    spf = np.arange(n + 1)
    for i in range(2, int(n**0.5) + 1):
        if spf[i] == i:  # if prime
            for j in range(i * i, n + 1, i):
                spf[j] = i
    return spf


@njit
def factor_spf(n: int, spf: np.ndarray) -> dict[int, int]:
    factors = Dict.empty(types.int64, types.int64)
    while n > 1:
        p = spf[n]
        if p not in factors:
            factors[p] = 1
        else:
            factors[p] += 1
        n //= p
    return factors
