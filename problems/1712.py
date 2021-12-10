# 1712 - 손익분기점


def solve():
    a, b, c = tuple(map(int, input().split()))

    if b >= c:
        print(-1)
    else:
        print(a // (c - b) + 1)


solve()
