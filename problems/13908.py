# 13908 - 비밀번호

import math


def C(n, r):
    return int(math.factorial(n) / (math.factorial(n - r) * math.factorial(r)))


def solve():
    N, M = map(int, input().split())
    n_list = map(int, input().split())
    count = 10
    n = 0
    for i in range(M + 1):
        n += ((-1) ** i) * (count ** N) * C(M, i)
        count += -1
    print(n)


solve()
