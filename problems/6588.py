# 6588 - 골드바흐의 추측

import sys


def get_prime_list():
    prime = [True for _ in range(10000 + 1)]
    prime[0] = False
    prime[1] = False

    for i in range(1, 10000 + 1):
        if prime[i]:
            p = 2
            while i * p <= 10000:
                prime[i * p] = False
                p += 1
    return prime


def solve():
    prime = get_prime_list()
    while True:
        N = int(sys.stdin.readline())
        if N == 0:
            break

        for i in range(3, N + 1):
            if prime[i] and prime[N - i]:
                print(f"{N} = {i} + {N-i}")
                break


solve()
