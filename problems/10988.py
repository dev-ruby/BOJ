# 10988 - 팰린드롬인지 확인하기


def solve():
    word = input()
    print(1 if word == word[::-1] else 0)


solve()
