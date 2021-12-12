# 15649 - N과 M (1)

import itertools


def solve():
    M, N = map(int, input().split())
    for i in itertools.permutations(range(1, M + 1), N):
        print(" ".join(map(str, i)))


solve()
