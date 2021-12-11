# 2577 - 숫자의 개수


def solve():
    a = int(input())
    b = int(input())
    c = int(input())
    abc = list(str(a * b * c))
    for i in range(0, 10):
        print(abc.count(str(i)))


solve()
