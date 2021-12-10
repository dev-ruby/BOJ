# 1316 - 그룹 단어 체커


def solve():
    N = int(input())
    count = 0

    for i in range(N):
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        word = input()
        cur = 1
        for w in range(len(word)):
            if w == 0:
                alphabet.remove(word[w])
                continue
            else:
                if word[w] in alphabet:
                    alphabet.remove(word[w])
                    continue
                else:
                    if word[w - 1] == word[w]:
                        continue
                    else:
                        cur = 0
        count += cur
    print(count)


solve()
