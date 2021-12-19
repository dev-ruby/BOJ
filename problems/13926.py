# 13926 - gcd(n, k) = 1

import random
import sys

sys.setrecursionlimit(10 ** 6)


def pow(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res


def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def miller_rabin(N, a):
    r = 0
    d = N - 1
    while d % 2 == 0:
        r += 1
        d = d // 2

    x = pow(a, d, N)
    if x == 1 or x == N - 1:
        return True

    for i in range(r - 1):
        x = pow(x, 2, N)
        if x == N - 1:
            return True
    return False


def is_prime(N):
    prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    if N == 1:
        return False
    if N == 2 or N == 3:
        return True
    if N % 2 == 0:
        return False
    for a in prime_list:
        if N == a:
            return True
        if not miller_rabin(N, a):
            return False
    return True


def pollard_rho(N):

    if is_prime(N):
        return N
    if N == 1:
        return 1
    if N % 2 == 0:
        return 2

    g = lambda x, y: ((x ** 2 % N) + y + N) % N

    x = random.randrange(2, N)
    y = x
    c = random.randrange(1, N)
    d = 1
    while d == 1:
        x = g(x, c)
        y = g(g(y, c), c)
        d = gcd(abs(x - y), N)
        if d == N:
            return pollard_rho(N)
    if is_prime(d):
        return d
    else:
        return pollard_rho(d)


def fast_euler_phi(N, d):
    for i in d:
        N = N // i * (i - 1)
    return N


def solve():
    N = int(input())

    divisor = list()

    n = N
    while n > 1:
        d = pollard_rho(n)
        divisor.append(d)
        n //= d

    divisor = list(set(divisor))

    print(fast_euler_phi(N, divisor))


solve()
