# 2579 - 계단 오르기

import sys


def solve():
    N = int(input())

    stair = []
    dp = []

    for _ in range(N):
        stair.append(int(sys.stdin.readline()))

    dp.append(stair[0])
    dp.append(max(stair[0] + stair[1], stair[1]))
    dp.append(max(stair[0] + stair[2], stair[1] + stair[2]))
    for i in range(3, N):
        dp.append(max(dp[i - 2] + stair[i], dp[i - 3] + stair[i] + stair[i - 1]))

    print(dp[N - 1])


solve()
