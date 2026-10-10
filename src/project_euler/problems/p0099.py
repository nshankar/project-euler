from math import log

from project_euler.utils.parser import get_root, load_data

data = load_data(get_root() / "data/p0099.txt")
parsed_data = []
for l in data:
    base, exp = map(int, l.split(","))
    parsed_data.append((base, exp))

# log is monotonic
largest_line = parsed_data.index(max(parsed_data, key=lambda x: x[1] * log(x[0])))
print(largest_line)
