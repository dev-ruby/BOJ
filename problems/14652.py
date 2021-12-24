# 14652 - 나는 행복합니다~


def solve():
    N, M, K = map(int, input().split())
    n = K // M
    m = K % M

    print(n, m)


solve()
