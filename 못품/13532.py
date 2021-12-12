# 13532 - 악마의 수열

from decimal import Decimal


def devil(N):
    cache = [Decimal(0) for _ in range(N + 1)]
    cache[1] = Decimal(1)

    for i in range(2, N + 1):
        cache[i] = Decimal(Decimal((cache[i - 1] + cache[i - 2]))/Decimal(2))
    return cache[N]


def solve():
    N = int(input())
    devil_number = devil(N)
    count = 0

    for i in str(devil_number):
        if count != 0 and i != "6":
            break
        if i == "6":
            count += 1
    print(count)


solve()