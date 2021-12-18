# 8611 - 팰린드롬 숫자


def notation(N, base):
    m = list()
    while N >= base:
        m.append(str(N % base))
        N //= base
    m.append(str(N))
    return m


def solve():
    N = int(input())
    p = False
    for i in range(2, 10):
        n = notation(N, i)
        if n == n[::-1]:
            p = True
            print(i, "".join(n))
    if str(N) == str(N)[::-1]:
        p = True
        print(10, N)
    if not p:
        print("NIE")


solve()
