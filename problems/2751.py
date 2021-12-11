# 2751 - 수 정렬하기 2


def solve():
    N = int(input())
    n_list = list()

    for _ in range(N):
        n_list.append(int(input()))

    print("\n".join(map(str, sorted(n_list))))


solve()
