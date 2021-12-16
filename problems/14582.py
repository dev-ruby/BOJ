# 14582 - 오늘도 졌다


def solve():
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))

    A, B = 0, 0

    for i in range(9):
        A += A_list[i]

        if A > B:
            print("Yes")
            return

        B += B_list[i]
    print("No")


solve()
