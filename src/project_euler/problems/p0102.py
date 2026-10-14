import numpy as np

from project_euler.utils.parser import get_root, load_data

data = load_data(get_root() / "data/p0102.txt")
points = []
for line in data:
    vals = list(map(int, line.split(",")))
    a = np.array(vals[0:2])
    b = np.array(vals[2:4])
    c = np.array(vals[4:6])

    points.append([a, b, c])


def cross(x: np.ndarray, y: np.ndarray):
    return x[0] * y[1] - x[1] * y[0]


def inside(x: np.ndarray, triangle: list[np.ndarray]):
    # checks if a 2D point x is inside the triangle ABC using cross products
    crosses = [
        cross(triangle[(i + 1) % 3] - triangle[i], x - triangle[i]) for i in range(3)
    ]
    return all(c > 0 for c in crosses) or all(c < 0 for c in crosses)


s = 0
origin = np.array((0, 0))
for triangle in points:
    if inside(origin, triangle):
        s += 1
print(s)
