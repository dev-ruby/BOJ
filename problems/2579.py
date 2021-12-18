# 2579 - 계단 오르기

import sys


def solve():
    N = int(input())

    stair = []
    dp = []
    for _ in range(N):
        stair.append(int(sys.stdin.readline()))

    if N == 1:
        print(stair[0])
        return
    if N == 2:
        print(stair[0] + stair[1])
        return

    dp.append(stair[0])
    for i in range(1, 3):
        if i == 1:
            dp.append(max(dp[i - 1] + stair[i], stair[i]))
        else:
            dp.append(max(dp[i - 2] + stair[i], stair[i - 1] + stair[i]))

    for i in range(3, N):
        dp.append(max(stair[i] + stair[i - 1] + dp[i - 3], stair[i] + dp[i - 2]))

    print(dp[-1])


solve()
