# 2562 - 최댓값


def solve():
    n_list = list()
    for _ in range(9):
        n_list.append(int(input()))
    print(max(n_list))
    print(n_list.index(max(n_list))+1)

solve()
