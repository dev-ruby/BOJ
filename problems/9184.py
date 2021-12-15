# 9184 - 신나는 함수 실행


dp = [[[0] * (21) for _ in range(21)] for _ in range(21)]


def w(a, b, c):
    global dp

    if min(a, b, c) <= 0:
        return 1
    elif max(a, b, c) > 20:
        return w(20, 20, 20)
    elif not dp[a][b][c] == 0:
        return dp[a][b][c]
    elif a < b and b < c:
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = (
            w(a - 1, b, c)
            + w(a - 1, b - 1, c)
            + w(a - 1, b, c - 1)
            - w(a - 1, b - 1, c - 1)
        )
        return dp[a][b][c]


def solve():
    while True:
        a, b, c = map(int, input().split())
        if a == b == c == -1:
            break
        print(f"w({a}, {b}, {c}) = {w(a, b, c)}")


solve()
