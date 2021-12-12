# 2749 - 피보나치 수 3


def fibo(N):
    dp = [0] * (N + 1)
    dp[1] = 1

    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        dp[i] %= 1000000
    return dp[N]


def solve():
    N = int(input())
    P = 1500000
    N %= P

    print(fibo(N))


solve()
