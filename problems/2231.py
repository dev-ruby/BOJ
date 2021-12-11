# 2231 - 분해합


def solve():
    N = int(input())
    for i in range(1, N + 1):
        if N == i + sum(map(int, list(str(i)))):
            print(i)
            return
    print(0)


solve()
