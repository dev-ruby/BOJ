# 1758 - 알바생 강호

import sys


def solve():
    N = int(input())

    n_list = list()
    money = 0

    for _ in range(N):
        n_list.append(int(sys.stdin.readline()))

    n_list.sort(key=lambda x: -x)

    for i in range(N):
        current = n_list[i] - i
        if current > 0:
            money += current

    print(money)


solve()
