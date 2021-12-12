# 9093 - 단어 뒤집기

import sys


def solve():
    N = int(input())
    for _ in range(N):
        sentence = sys.stdin.readline().strip().split()
        for i in range(len(sentence)):
            sentence[i] = sentence[i][::-1]
        print(" ".join(sentence))


solve()
