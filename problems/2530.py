# 2530 - 인공지능 시계


def solve():
    a, b, c = map(int, input().split())
    d = int(input())

    time = c + 60 * b + 60 * 60 * a + d
    c = time % 60
    b = time // 60 % 60
    a = time // 3600 % 24

    print(a, b, c)


solve()
