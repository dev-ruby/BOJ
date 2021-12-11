# 2739 - 구구단


def solve():
    N = int(input())
    for i in range(9):
        print(f"{N} * {i+1} = {N*(i+1)}")


solve()
