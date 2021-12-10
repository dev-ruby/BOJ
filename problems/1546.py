# 1546 - 평균


def solve():
    N = int(input())

    scores = list(map(int, input().split()))
    M = max(scores)

    for i in range(N):
        scores[i] = scores[i] / M * 100

    avg = sum(scores) / N

    print(avg)


solve()
