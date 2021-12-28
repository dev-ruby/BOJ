# 3004 - 체스판 조각


def solve():
    N = int(input())
    if N == 1:
        print(2)
    elif N % 2 == 0:
        print(((N // 2) + 1) ** 2)
    else:
        print((N // 2 + 1) * (N // 2 + 2))


solve()
