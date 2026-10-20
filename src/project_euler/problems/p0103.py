import itertools
import math


def power_set(A: set) -> list[tuple]:
    subsets = [()]
    for x in A:
        subsets += [s + (x,) for s in subsets]
    return subsets


def special_sum(A: set) -> int:
    for B in power_set(A):
        sumB = sum(B)
        lenB = len(B)

        if lenB == 0:
            continue

        complement = A - set(B)
        for C in power_set(complement):
            sumC = sum(C)
            lenC = len(C)

            # TODO: We're guaranteed that lenB >= lenC which could be useful for optimization
            if sumB == sumC:
                return -1
            if lenB > lenC and not (sumB > sumC):
                return -1
    return sum(A)


# We have candidate sets of the form a_1 < a_2 < ... < a_6 < a_7
# Using 255 as an upper bound, ∑a_i <= 255 and also a_7 < a_1 + a_2 implying a_7 <= 255 / 4 = 63.75


def valid_candidate(candidate: tuple, bound: int) -> bool:
    if sum(candidate) > bound:
        return False

    n = len(candidate)
    for i in range(2, bound):
        if sum(candidate[0:i]) < sum(candidate[n - i + 1 : n]):
            return False
    return True


def main(n: int = 7, bound: int = 255):
    candidates = itertools.combinations([i for i in range(1, bound // 4 + 1)], n)
    optimal_special_sum = bound
    optimal_special_sum_set = set()
    for c in candidates:
        if not valid_candidate(c, bound):
            continue
        s = special_sum(set(c))
        if s != -1 and s <= optimal_special_sum:
            optimal_special_sum = s
            optimal_special_sum_set = c

    print(optimal_special_sum_set, optimal_special_sum)


if __name__ == "__main__":
    # ansantz with sum of 255
    print(special_sum({20, 31, 38, 39, 40, 42, 45}))
    main()
