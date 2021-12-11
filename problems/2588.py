# 2588 - 곱셈


def solve():
    a = int(input())
    b = int(input())

    bl = list(str(b))

    print(int(bl[-1]) * a)
    print(int(bl[-2]) * a)
    print(int(bl[-3]) * a)
    print(a * b)


solve()
