# 2447 - 별 찍기 - 10


def rect_star(x, y, n, ls):
    if n == 3:
        ls[x + 1][y + 1] = " "

    else:
        temp = n // 3
        for i in range(x + temp, x + 2 * temp):
            for j in range(y + temp, y + 2 * temp):
                ls[i][j] = " "

        for i in range(0, n, temp):
            for j in range(0, n, temp):
                rect_star(x + i, y + j, temp, ls)


def solve():
    N = int(input())
    ls = [["*" for i in range(N)] for i in range(N)]

    rect_star(0, 0, N, ls)
    for i in range(0, N):
        for j in range(0, N):
            print(ls[i][j], end="")
        print()


solve()
