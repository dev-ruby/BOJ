# 2164 - 카드2

import collections


def solve():
    N = int(input())
    queue = collections.deque(list(range(1, N + 1)))
    while len(queue) != 1:
        queue.popleft()
        queue.append(queue.popleft())
    print(queue[0])


solve()
