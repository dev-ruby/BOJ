# 1002 - 터렛

import math

def solve():
    N = int(input())

    for _ in range(N):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())

        distance = math.sqrt((x1-x2)**2 + (y1-y2)**2) # 두 원 사이의 거리

        if distance == 0 and r1 == r2: # 두 원이 같을 때
            print(-1)
            continue
        
        if abs(r1 - r2) == distance or r1 + r2 == distance: # 내접하거나 외접할 때
            print(1)
            continue
        
        if abs(r1 - r2) < distance < (r1+r2): #두 원이 서로다른 두 점에서 만날때
            print(2)
            continue
        
        print(0)
        continue

solve()
