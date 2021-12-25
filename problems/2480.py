# 2480 - 주사위 세개


def solve():
    a, b, c = map(int, input().split())

    money = 0

    if a == b == c:
        money = 10000 + a * 1000
    elif a == b or b == c or c == a:
        if a == b or a == c:
            money = 1000 + 100 * a
        elif b == c:
            money = 1000 + 100 * b
    else:
        money = max(a, b, c) * 100

    print(money)


solve()
