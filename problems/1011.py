# 1011 - Fly me to the Alpha Centauri

def solve():
    N = int(input())

    for _ in range(N):
        x,y = map(int, input().split())

        distance = y-x
        n = 0
        
        while True:
            if distance <= n*(n+1):
                break
            n+=1
        if distance <= n**2:
            print(n*2-1)
        else:
            print(n*2)

solve()
