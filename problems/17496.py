# 17496 - 스타후르츠


def solve():
    N, T, C, P = map(int, input().split())
    print((N - 1) // T * C * P)


solve()
