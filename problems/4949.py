# 4949 - 균형잡힌 세상

import collections
import sys


def is_symmetry(sentence):
    stack = collections.deque()
    for i in sentence:
        if i == "[" or i == "(":
            stack.append(i)
        elif i == "]":
            if not stack:
                return "no"
            if stack.pop() != "[":
                return "no"
        elif i == ")":
            if not stack:
                return "no"
            if stack.pop() != "(":
                return "no"
    if stack:
        return "no"
    return "yes"


def solve():
    while True:
        sentence = sys.stdin.readline()

        if sentence == ".\n":
            break

        print(is_symmetry(sentence))


solve()
