# 18870 - 좌표 압축

import sys


def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def solve():
    N = input()

    pos_list = list(map(int, sys.stdin.readline().strip().split()))

    pos_rank = list(set(pos_list))
    pos_rank.sort()

    for i in pos_list:
        print(binary_search(pos_rank, i), end=" ")


solve()
