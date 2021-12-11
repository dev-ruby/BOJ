# 2439 - 별 찍기 - 2


def solve():
    N = int(input())

    for i in range(1, N + 1):
        print(" " * (N - i) + "*" * i)


solve()
