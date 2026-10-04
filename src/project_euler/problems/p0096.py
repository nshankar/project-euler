from copy import deepcopy

from project_euler.utils.parser import get_root, load_data


def puzzles():
    data = load_data(get_root() / "data" / "p0096.txt")
    for k in range(0, len(data), 10):
        puzzle_arr = [[0 for _ in range(9)] for _ in range(9)]
        puzzle_strs = data[k + 1 : k + 10]  # skip puzzle title line
        for i in range(9):
            for j in range(9):
                puzzle_arr[i][j] = int(puzzle_strs[i][j])
        yield puzzle_arr


def get_candidates(puzzle: list[list[int]], i: int, j: int) -> set[int]:
    assert puzzle[i][j] == 0

    candidates = {i for i in range(1, 10)}
    row_vals = set(puzzle[i])
    col_vals = {puzzle[m][j] for m in range(9)}
    box_vals = get_box_vals(puzzle, i, j)

    candidates = candidates - (row_vals | col_vals | box_vals)

    return candidates


def get_box_vals(puzzle: list[list[int]], i: int, j: int) -> set:
    uli = (i // 3) * 3
    ulj = (j // 3) * 3
    box_vals = set()
    for m in range(uli, uli + 3):
        box_vals.update(puzzle[m][ulj : ulj + 3])
    return box_vals


def solve_puzzle(puzzle: list[list[int]]) -> list[list[int]] | None:
    best_i = -1
    best_j = -1
    best_candidates = {i for i in range(1, 10)}

    for i in range(9):
        for j in range(9):
            if puzzle[i][j] != 0:
                continue
            candidates = get_candidates(puzzle, i, j)
            if len(candidates) == 0:
                return None
            elif len(candidates) < len(best_candidates):
                best_candidates = candidates
                best_i, best_j = i, j

    if best_i == -1 or best_j == -1:
        return puzzle

    for candidate in best_candidates:
        candidate_puzzle = deepcopy(puzzle)
        candidate_puzzle[best_i][best_j] = candidate

        soln = solve_puzzle(candidate_puzzle)
        if soln is not None:
            return soln


s = 0
for i, puzzle in enumerate(puzzles()):
    soln = solve_puzzle(puzzle)
    assert soln is not None
    s += 100 * soln[0][0] + 10 * soln[0][1] + soln[0][2]
print(s)
