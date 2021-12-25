# 2441 - 별 찍기 - 4


def solve():
    N = int(input())
    for i in range(N):
        print(" " * i + "*" * (N - i))


solve()
