# 1929 - 소수 구하기


def solve():
    M, N = map(int, input().split())

    prime = [True] * (N + 1)
    prime[1] = False

    for i in range(1, N + 1):
        if prime[i]:
            p = 2
            while i * p <= N:
                prime[i * p] = False
                p += 1

    for i in range(M, N + 1):
        if prime[i]:
            print(i)


solve()
