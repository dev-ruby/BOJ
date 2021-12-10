# 1181 - 단어 정렬

import sys

def solve():
    N = int(input())

    word_list = list()

    for _ in range(N):
        word_list.append(sys.stdin.readline().rstrip("\n"))

    word_list = list(set(word_list)) # 중복 제거

    word_list.sort() # 사전순 정렬
    word_list.sort(key = lambda x: len(x)) # 길이별 정렬

    for i in word_list:
        print(i)

solve()