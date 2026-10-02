import numpy as np


def sums_of_divisors(n) -> np.ndarray:
    sods = np.full(n + 1, 1)
    for i in range(2, n + 1):
        for j in range(2 * i, n + 1, i):
            sods[j] += i
    return sods


def amicable_chain(m: int, sods: np.ndarray, max_allowed: int | None) -> set[int]:
    chain = {m}
    chain_member = sods[m]
    while chain_member != m:
        if (
            max_allowed is not None
            and chain_member > max_allowed
            or chain_member in chain
        ):  # invalid amicable chains
            return set()
        chain.add(int(chain_member))
        chain_member = sods[chain_member]
    return chain


def p0095(n: int = 1_000_000) -> int:
    sods = sums_of_divisors(n)
    max_chain = []

    for i in range(2, n + 1):
        chain = amicable_chain(i, sods, n)
        if len(chain) > len(max_chain):
            max_chain = chain

    print(max_chain)
    return min(max_chain)


print(p0095())
