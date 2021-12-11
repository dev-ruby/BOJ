# 2292 - 벌집


def solve():
    N = int(input())

    r = 1
    c = 1
    while N > r:
        r += 6 * c
        c += 1
    print(c)


solve()
