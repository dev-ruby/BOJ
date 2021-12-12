# 2293 - 동전 1

import sys


def solve():
    N, K = map(int, sys.stdin.readline().split())
    n_list = list()
    for _ in range(N):
        n_list.append(int(sys.stdin.readline().strip()))

    dp = [0] * (K + 1)
    dp[0] = 1
    for i in n_list:
        for j in range(i, K + 1):
            if j - i >= 0:
                dp[j] += dp[j - i]
    print(dp[K])


solve()
