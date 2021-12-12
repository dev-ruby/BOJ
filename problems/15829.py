# 15829 - Hashing


def hash(d):
    h = 0
    M = 1234567891
    for i in range(len(d)):
        x = ord(d[i]) - 96
        h += x * (31 ** i)
    return h % M


def solve():
    L = int(input())
    sentence = input()
    print(hash(sentence))


solve()
