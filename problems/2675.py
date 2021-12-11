# 2675 - 문자열 반복


def solve():
    N = int(input())
    for _ in range(N):
        line = input().split()
        word = ""
        for l in line[1]:
            word += l * int(line[0])
        print(word)


solve()
