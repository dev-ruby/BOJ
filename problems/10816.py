# 10816 - 숫자 카드 2

import sys
import collections


def solve():
    N = int(sys.stdin.readline().strip())
    n_list = list(map(int, sys.stdin.readline().strip().split()))
    M = int(sys.stdin.readline().strip())
    m_list = list(map(int, sys.stdin.readline().strip().split()))

    C = collections.Counter(n_list)
    for i in m_list:
        print(C[i] if i in C else 0, end=" ")


solve()
