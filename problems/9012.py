# 9012 - 괄호

import sys


def solve():
    N = int(input())

    for _ in range(N):
        sentence = sys.stdin.readline().strip()

        if sentence.count("(") != sentence.count(")"):
            print("NO")
            continue
        if sentence[0] == ")" or sentence[-1] == "(":
            print("NO")
            continue

        stack = list()

        for i in range(len(sentence)):
            word = sentence[i]
            if word == "(":
                stack.append(word)
            else:
                if len(stack) != 0:
                    stack.pop()
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")


solve()
