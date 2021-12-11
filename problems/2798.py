# 2798 - 블랙잭

from itertools import combinations


def solve():

    n, m = map(int, input().split())
    c = map(int, input().split())
    M = 0
    for i in list(combinations(c, 3)):
        if sum(i) > m:
            continue
        if M == sum(i):
            print(m)
            quit()
        elif M < sum(i):
            M = sum(i)
    print(M)


solve()
