# 14654 - 스테판 쿼리


def solve():
    N = int(input())
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))

    count = ["", 0]
    current = ["", 0]
    for i in range(N):
        A, B = A_list[i], B_list[i]
        if A == B:
            if current[0] == "A":
                current = ["B", 1]
            else:
                current = ["A", 1]
        elif A == 1 and B == 3:
            if current[0] == "A":
                current[1] += 1
            else:
                current = ["A", 1]
        elif A == 2 and B == 1:
            if current[0] == "A":
                current[1] += 1
            else:
                current = ["A", 1]
        elif A == 3 and B == 2:
            if current[0] == "A":
                current[1] += 1
            else:
                current = ["A", 1]
        else:
            if current[0] == "B":
                current[1] += 1
            else:
                current = ["B", 1]
        if count[1] < current[1]:
            count = current.copy()
    print(count[1])


solve()
