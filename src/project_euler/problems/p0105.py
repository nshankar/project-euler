from project_euler.problems.p0103 import special_sum
from project_euler.utils.parser import get_root, load_data

data = load_data(get_root() / "data/p0105.txt")
sets = [set(map(int, row.split(","))) for row in data]

s = 0
for A in sets:
    ss = special_sum(A)
    if ss != -1:
        s += ss
print(s)
