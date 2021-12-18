# 8892 - 팰린드롬

import itertools
import sys


def solve():
    N = int(sys.stdin.readline())
    for _ in range(N):
        k = int(sys.stdin.readline())
        w_list = list()
        p = False
        for _ in range(k):
            w_list.append(sys.stdin.readline().strip())
        for i in itertools.permutations(w_list, 2):
            w = "".join(i)
            if w == w[::-1]:
                p = True
                print(w)
                break
        if not p:
            print(0)


solve()
