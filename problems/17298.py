# 17298 - 오큰수

import collections


def solve():
    N = int(input())
    n_list = list(map(int, input().split()))
    big_list = [-1] * N
    stack = collections.deque()
    for i in range(N):
        while stack and stack[-1][0] < n_list[i]:
            index = stack.pop()[1]
            big_list[index] = n_list[i]
        stack.append([n_list[i], i])
    print(" ".join(map(str, big_list)))


solve()
