# 1436 - 영화감독 숌

def solve():
    n = int(input())
    count = 0
    six_n = 666

    while True:
        if "666" in str(six_n):
            count += 1
        if count == n:
            break
        six_n += 1

    print(six_n)

solve()
