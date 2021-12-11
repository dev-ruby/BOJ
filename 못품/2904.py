# 2904 - 수학은 너무 쉬워

import itertools
import math


def get_prime(N):
    primes = list()
    a = [False, False] + [True] * (N - 1)

    for i in range(2, N + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, N + 1, i):
                a[j] = False
    return primes


def solve():
    N = int(input())
    n_list = list(map(int, input().split()))
    count = 1
    M_score = 0
    score = 0
    primes = get_prime(round(math.sqrt(max(n_list))) + 1)

    for ab in set(itertools.permutations(n_list, 2)):
        A, B = ab
        c = 0
        M = 0
        for i in primes[: int(math.sqrt(max(ab)) + 1)]:
            if A % i != 0:
                continue

            A = A // i
            B = B * i
            c += 1

            score = math.gcd(A, B)
            print(f"{A}, {B} : {score}")
            # print(f"score : {score}")
            # print(f"count : {count} / c : {c}")
            M_score = max(score, M_score)

            if score > M_score:
                count = c
            if score == M_score:
                count = min(c, count)

    print(f"{M_score} {count}")


solve()
