# 9461 - 파도반 수열

import sys


def P(N):

    if N < 6:
        return "21112"[N % 5]

    dp = [0] * (N + 1)
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2

    for i in range(6, N + 1):
        dp[i] = dp[i - 5] + dp[i - 1]

    return dp[N]


def solve():
    N = int(input())
    for _ in range(N):
        print(P(int(sys.stdin.readline())))


solve()
