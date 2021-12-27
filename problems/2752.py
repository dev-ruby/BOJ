# 2752 - 세수정렬


def solve():
    number = list(map(int, input().split()))
    number.sort()

    print(*number)


solve()
