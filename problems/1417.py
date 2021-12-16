# 1417 - 국회의원 선거


def solve():
    N = int(input())

    me = int(input())

    if N == 1:
        print(0)
        return

    count = 0

    n_list = list()

    for _ in range(N - 1):
        n_list.append(int(input()))

    while True:
        n_list.sort()
        if n_list[-1] < me:
            break

        n_list[-1] -= 1
        me += 1
        count += 1

    print(count)


solve()
