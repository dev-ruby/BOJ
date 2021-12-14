# 16480 - 외심과 내심은 사랑입니다


def solve():
    R, r = map(int, input().split())
    distance = R * (R - (2 * r))
    print(distance)


solve()
