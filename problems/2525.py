# 2525 - 오븐 시계


def solve():
    h, m = map(int, input().split())
    c = int(input())

    m += 60 * h
    m += c

    h, m = divmod(m, 60)

    h %= 24

    print(h, m)


solve()
