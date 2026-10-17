import sys

sys.set_int_max_str_digits(0)


def fibonacci():
    f_prev, f_prev_prev = 1, 1
    yield f_prev_prev
    yield f_prev

    while True:
        f = f_prev + f_prev_prev
        f_prev_prev = f_prev
        f_prev = f
        yield f


def is_pandigital(n: str):
    digits = set(n)
    return len(digits) == 9 and "0" not in digits


for i, f in enumerate(fibonacci(), start=1):
    lagging_digits = str(f % 10**9)
    if is_pandigital(lagging_digits):
        leading_digits = str(f)[:9]
        if is_pandigital(leading_digits):
            print(f"F_{i} has pandigital ends")
            break
