# 10773 - 제로

import collections
import sys


def solve():
    N = int(input())
    stack = collections.deque()
    for _ in range(N):
        n = int(sys.stdin.readline().strip())
        if n != 0:
            stack.append(n)
        else:
            stack.pop()
    print(sum(stack))


solve()
