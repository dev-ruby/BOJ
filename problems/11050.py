# 11050 - 이항 계수 1

import math


def C(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


def solve():
    n, k = map(int, input().split())
    print(C(n, k))


solve()
