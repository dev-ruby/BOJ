# 4299 - AFC 윔블던


def solve():
    p, m = map(int, input().split())

    if p - m < 0:
        print(-1)
        return

    if (p + m) % 2 == 1:
        print(-1)
        return

    a = (p + m) // 2
    b = p - a

    print(max(a, b), min(a, b))


solve()
