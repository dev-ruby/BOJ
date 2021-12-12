# 10866 - 덱

import sys
import collections


def solve():
    deque = collections.deque()
    N = int(input())
    for _ in range(N):
        command = sys.stdin.readline().strip().split()

        if command[0] == "push_front":
            deque.appendleft(int(command[1]))
        elif command[0] == "push_back":
            deque.append(int(command[1]))
        elif command[0] == "pop_front":
            print(deque.popleft() if deque else -1)
        elif command[0] == "pop_back":
            print(deque.pop() if deque else -1)
        elif command[0] == "size":
            print(len(deque))
        elif command[0] == "empty":
            print(1 if len(deque) == 0 else 0)
        elif command[0] == "front":
            print(deque[0] if deque else -1)
        elif command[0] == "back":
            print(deque[-1] if deque else -1)


solve()
