# 1085 - 직사각형에서 탈출

def solve():
    x, y, w, h = map(int, input().split())
    print(min((w-x, x, h-y, y)))

solve()
