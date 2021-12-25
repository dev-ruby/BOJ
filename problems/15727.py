# 15727 - 조별과제를 하려는데 조장이 사라졌다


def solve():
    N = int(input())
    print(N // 5 + (0 if N % 5 == 0 else 1))


solve()
