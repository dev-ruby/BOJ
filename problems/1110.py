# 1110 - 더하기 사이클

def add(x, y):
    return y + str(int(x) + int(y))[-1]

def solve():
    N = input()
    if len(N) == 1:
        N = "0"+N
    count = 1
    new = add(N[0], N[1])

    while new != N:
        count = count + 1
        new = add(new[0], new[1])

    print(count)

solve()
