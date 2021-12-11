# 2108 - 통계학

import sys
from collections import Counter


def solve():
    N = int(sys.stdin.readline())
    n_list = list()

    for _ in range(N):
        n_list.append(int(sys.stdin.readline()))

    n_list.sort()
    avg = round(sum(n_list) / N)

    M = n_list[-1]
    m = n_list[0]
    rg = M - m
    med = n_list[N // 2] if N % 2 == 1 else (n_list[N // 2] + n_list[N // 2 + 1]) / 2

    cm_list = Counter(n_list).most_common()
    cm_1 = list(x[0] for x in cm_list)
    cm_2 = list(x[1] for x in cm_list)

    if cm_2.count(cm_2[0]) > 1:
        cm = cm_1[1]
    else:
        cm = cm_1[0]

    print(avg)
    print(med)
    print(cm)
    print(rg)


solve()
