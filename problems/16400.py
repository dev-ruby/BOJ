# 16400 - 소수 화폐


def get_prime_list(N):
    prime_list = [True] * (N + 1)
    prime_list[0] = False
    prime_list[1] = False
    prime = list()

    for i in range(2, N + 1):
        if prime_list[i]:
            prime.append(i)
            for j in range(2 * i, N + 1, i):
                prime_list[j] = False
        else:
            continue
    return prime


def solve():
    N = int(input())
    prime_list = get_prime_list(N)

    dp = [0] * (N + 1)
    dp[0] = 1

    for i in prime_list:
        for j in range(i, N + 1):
            dp[j] = (dp[j] + dp[j - i]) % 123456789

    print(dp[N])


solve()
