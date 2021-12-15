# 14648 - 쿼리 맛보기

import sys


def solve():
    N, Q = map(int, input().split())
    n_list = list(map(int, input().split()))
    for _ in range(Q):
        query = list(map(int, sys.stdin.readline().split()))
        if query[0] == 1:
            a, b = query[1:]
            print(sum(n_list[a - 1 : b]))
            n_list[a - 1], n_list[b - 1] = n_list[b - 1], n_list[a - 1]

        elif query[0] == 2:
            a, b, c, d = query[1:]
            print(sum(n_list[a - 1 : b]) - sum(n_list[c - 1 : d]))


solve()
