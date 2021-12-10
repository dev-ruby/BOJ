# 1157 - 단어 공부


def solve():
    word = input().upper()
    alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
    count = 0
    M = ""

    for a in alphabet:
        if count == word.count(a):
            M = "?"
        if count < word.count(a):
            count = word.count(a)
            M = a
    print(M)


solve()
