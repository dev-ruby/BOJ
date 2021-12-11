# 2581 - 소수


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def solve():
    M, N = map(int, (input(), input()))
    m = 0
    c = 0

    for i in range(M, N + 1):
        if is_prime(i):
            c += i
            if m == 0:
                m = i
    if c == 0:
        print(-1)
    else:
        print(c)
        print(m)


solve()
