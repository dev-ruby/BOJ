# 2839 - 설탕 배달


def solve():
    N = int(input())
    c = 0
    for i in range(0, 6):
        if (N - (3 * i)) % 5 == 0:
            c = i
            N = N - (3 * i)
            break
        if N - (3 * i) <= 0:
            c = -1
            break
        c = -1

    if c == -1:
        print(c)
    else:
        c += N // 5
        print(c)


solve()
