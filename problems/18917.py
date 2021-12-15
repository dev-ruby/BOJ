# 18917 - 수열과 쿼리 38

import sys


def solve():
    Q = int(input())

    s = 0

    xor = 0

    for _ in range(Q):
        query = sys.stdin.readline().split()
        command = query[0]
        N = int(query[1]) if len(query) == 2 else 0
        if command == "1":
            s += N
            xor ^= N

        elif command == "2":
            s -= N
            xor ^= N

        elif command == "3":
            print(s)

        elif command == "4":
            print(xor)


solve()
