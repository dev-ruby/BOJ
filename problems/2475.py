# 2475 - 검증수


def solve():
    n = list(map(int, input().split()))
    print(sum(list(map(lambda x: x**2, n)))%10)

solve()
