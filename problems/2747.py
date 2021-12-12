# 2747 - 피보나치 수


def fibo(N):
    dp = [0] * (N + 1)
    dp[1] = 1

    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[N]


def solve():
    N = int(input())
    print(fibo(N))


solve()
