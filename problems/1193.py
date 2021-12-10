# 1193 - 분수찾기

def solve():
    N = int(input())
    n = 1
    a = 0
    b = 0

    while a < N:
        a = n * (n+1) / 2
        if a >= N: break
        n+=1


    a = 1 + (n * (n+1) / 2 - N)
    b = n - (n * (n+1) / 2 - N)

    if n%2==0:
        a, b = b, a

    a, b = map(int, (a,b))

    print(f"{a}/{b}")

solve()