# 2607 - 비슷한 단어
import string


def solve():
    N = int(input())

    word = list(sorted(input()))

    count = 0

    for _ in range(N - 1):
        w = list(sorted(input()))
        if w == word:
            count += 1
            continue

        for i in string.ascii_uppercase:
            _w = w.copy()
            _w.append(i)
            if sorted(_w) == word:
                count += 1
                continue
        for i in string.ascii_uppercase:
            _w = w.copy()
            if not i in _w:
                continue
            _w.remove(i)
            if sorted(_w) == word:
                count += 1
                continue
        for i in string.ascii_uppercase:
            for j in string.ascii_uppercase:
                _w = w.copy()
                if not i in _w:
                    continue
                _w.remove(i)
                _w.append(j)
                if sorted(_w) == word:
                    count += 1
                    continue

    print(count)


solve()
