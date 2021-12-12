# 11866 - 요세푸스 문제 0

import collections


def solve():
    N, K = map(int, input().split())
    queue = collections.deque(list(range(1, N + 1)))
    perm = list()
    while queue:
        queue.rotate(-K + 1)
        perm.append(str(queue.popleft()))
    print(f"<{', '.join(perm)}>")


solve()
