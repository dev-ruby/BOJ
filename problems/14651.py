# 14651 - 걷다보니 신천역 삼 (Large)


def solve():
    N = int(input())
    M = 10 ** 9 + 9
    count = 0

    if N != 1:
        count = 2
        for i in range(N - 2):
            count *= 3
            count %= M
    print(count)


solve()
