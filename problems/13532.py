# 13532 - 악마의 수열

import math


def solve():

    N = int(input())
    count = 0

    if N < 4:
        print(0)
        return

    if N % 2 == 0:
        count = math.floor(math.log10(2 ** N))
    else:
        count = math.floor(math.log10(2 ** (N - 1)))
    print(count)


solve()
