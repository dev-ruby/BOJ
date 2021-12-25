# 11399 - ATM


def solve():
    N = int(input())
    P = list(map(int, input().split()))
    count = 0
    P.sort()
    for i in range(N):
        count += sum(P[: i + 1])
    print(count)


solve()
