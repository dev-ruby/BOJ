# 13140 - Hello World!

import itertools


def solve():
    N = int(input())
    A, B = 0, 0
    if N > 185000:
        print("No Answer")
        return
    for i in itertools.permutations(list(range(0, 10)), 7):
        d, e, h, l, o, r, w = i
        if w == 0 or h == 0:
            continue
        _a = 10000 * h + 1000 * e + 100 * l + 10 * l + o
        _b = 10000 * w + 1000 * o + 100 * r + 10 * l + d

        if _a + _b == N:
            A = _a
            B = _b
            break
    if A == 0 and B == 0:
        print("No Answer")
    else:
        print(f"  {A}\n+ {B}\n-------")
        print(f" {N}" if n >= 100000 else f"  {N}")


solve()
