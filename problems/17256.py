# 17256 - 달달함이 넘쳐흘러


def solve():
    ax, ay, az = map(int, input().split())
    cx, cy, cz = map(int, input().split())
    bx = cx - az
    by = cy // ay
    bz = cz - ax
    print(bx, by, bz)


solve()
