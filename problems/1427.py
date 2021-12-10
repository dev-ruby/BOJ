# 1427 - 소트인사이드


def solve():
    N = list(map(int, list(input())))

    N.sort()

    N = list(map(str, N))

    print("".join(N[::-1]))


solve()
