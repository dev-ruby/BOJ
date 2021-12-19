# 17425 - 약수의 합

import sys


def solve():
    N = int(sys.stdin.readline())
    n_list = []

    for _ in range(N):
        n_list.append(int(sys.stdin.readline()))

    M = max(n_list)

    sum_list = [0 for _ in range(M + 1)]
    dp = [1 for _ in range(M + 1)]

    for i in range(2, M + 1):
        j = 1
        while i * j <= M:
            dp[i * j] += i
            j += 1
    for i in range(1, M + 1):
        sum_list[i] = sum_list[i - 1] + dp[i]

    for i in n_list:
        print(sum_list[i])


solve()
