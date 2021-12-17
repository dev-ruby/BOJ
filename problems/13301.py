# 13301 - 타일 장식물


def F(N):
    if N < 3:
        return "046"[N]

    dp = [0 for _ in range(N + 1)]
    dp[1] = 4
    dp[2] = 6

    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[N]


def solve():
    N = int(input())
    print(F(N))


solve()
