from collections import defaultdict
from itertools import combinations
from math import ceil, isqrt

from project_euler.utils.parser import get_root, load_data


def sq_nums_of_len_n(n: int) -> list[int]:
    sq_nums = []
    k = ceil(10 ** ((n - 1) / 2))
    while len(str(k**2)) == n:
        sq_nums.append(k**2)
        k += 1
    return sq_nums


def maybe_max_anagramic_square(pair: tuple[str, str], sq_num: int) -> int | None:
    # checks if word pair forms an anagramic square, if yes returns the larger square
    sq_num_str = str(sq_num)
    assert len(pair[0]) == len(pair[1]) == len(sq_num_str)
    mapping = compute_mapping(pair[0], sq_num)

    if mapping is None:
        return None

    sq_candidate_str = pair[1].translate(str.maketrans(mapping))
    if sq_candidate_str[0] == "0":
        return None
    sq_candidate = int(sq_candidate_str)

    if isqrt(sq_candidate) ** 2 == sq_candidate:
        return max(sq_num, sq_candidate)
    else:
        return None


def compute_mapping(word: str, sq_num: int) -> dict[str, str] | None:
    sq_num_str = str(sq_num)
    # need a bijection between letters and digits
    if not len(set(word)) == len(set(sq_num_str)) == len(set(zip(word, sq_num_str))):
        return None

    mapping = {word[i]: sq_num_str[i] for i in range(len(word))}
    return mapping


words = load_data(get_root() / "data" / "p0098.txt")[0][1:-1].split('","')

# keys are sorted letters
# values are lists of words
anagrams: dict[str, list[str]] = defaultdict(list)
for word in words:
    letters = "".join(sorted(word))
    anagrams[letters].append(word)

max_anagramic_square = 0
for anagram_key, anagram_list in anagrams.items():
    if len(anagram_list) < 2:
        continue
    sq_num_candidates = sq_nums_of_len_n(len(anagram_key))

    for pair in combinations(anagram_list, 2):
        if pair[0] == pair[1][::-1]:
            # skip palindromes
            continue
        for sq_num in sq_num_candidates:
            maybe_sq_num = maybe_max_anagramic_square(pair, sq_num)
            if maybe_sq_num is not None:
                max_anagramic_square = max(max_anagramic_square, maybe_sq_num)
print(max_anagramic_square)
