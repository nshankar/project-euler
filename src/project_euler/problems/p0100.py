# Pell equation x**2 - 2 * y**2 = -1
x1, y1 = 1, 1
D = 2


def next_pell_soln(x: int, y: int):
    A = x1**2 + D * y1**2
    B = 2 * x1 * y1
    return A * x + B * D * y, B * x + A * y


def pell_soln_to_disc_soln(x: int, y: int):
    M, B = (x + 1) / 2, (y + 1) / 2
    if B.is_integer() and M.is_integer():
        return int(B), int(M)
    return -1, -1


x, y = x1, y1
while True:
    x, y = next_pell_soln(x, y)
    B, M = pell_soln_to_disc_soln(x, y)
    if M > 10**12:
        assert 2 * B * (B - 1) == M * (M - 1)
        print(B, M)
        break
