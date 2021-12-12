# 10828 - 스택

import sys


def solve():
    stack = []
    N = int(input())
    for _ in range(N):
        command = sys.stdin.readline().strip().split()

        if command[0] == "push":
            stack.append(int(command[1]))
        elif command[0] == "pop":
            print(stack.pop() if len(stack) != 0 else -1)
        elif command[0] == "size":
            print(len(stack))
        elif command[0] == "empty":
            print(1 if len(stack) == 0 else 0)
        elif command[0] == "top":
            print(stack[-1] if len(stack) != 0 else -1)


solve()
