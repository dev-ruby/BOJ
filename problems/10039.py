# 10039 - 평균 점수


def solve():
    def check(x):
        return x if x > 40 else 40

    n_list = []

    for _ in range(5):
        n_list.append(int(input()))

    print(sum(map(check, n_list)) // 5)


solve()
