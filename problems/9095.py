# 9095 - 1, 2, 3 더하기

import sys


def solve():
    N = int(input())
    n_list = []

    for _ in range(N):
        n_list.append(int(sys.stdin.readline()))

    dp = [0 for _ in range(sum(n_list) + 1)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, sum(n_list) + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    for i in n_list:
        print(dp[i])


solve()
