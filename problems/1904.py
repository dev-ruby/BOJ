# 1904 - 01타일


def get_way(N):
    MOD = 15746

    dp = [0] * 1000001
    dp[1] = 1
    dp[2] = 2

    if N < 3:
        return dp[N]

    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        dp[i] %= MOD

    return dp[N]


def solve():
    N = int(input())
    print(get_way(N))


solve()
