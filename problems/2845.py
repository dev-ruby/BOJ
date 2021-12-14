# 2845 - 파티가 끝나고 난 뒤


def solve():
    L, P = map(int, input().split())
    n = L * P
    for i in map(int, input().split()):
        print(i - n, end=" ")


solve()
