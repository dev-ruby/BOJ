# 1259 - 팰린드롬수


def solve():
    while True:
        N = input()
        if N == "0":
            return
        if N[::-1] == N:
            print("yes")
        else:
            print("no")


solve()
