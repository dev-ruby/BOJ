# 14650 - 걷다보니 신천역 삼 (Small)

import itertools


def solve():
    N = int(input())
    if N == 1:
        print(0)
    else:
        print(2 * (3 ** (N - 2)))


solve()
