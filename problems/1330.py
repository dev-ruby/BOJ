# 1330 - 두 수 비교하기


def solve():
    a, b = map(int, input().split())
    if a == b:
        print("==")
    elif a < b:
        print("<")
    elif a > b:
        print(">")


solve()
