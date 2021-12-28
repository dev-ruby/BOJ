# 5532 - 방학 숙제


def solve():
    L, A, B, C, D = (int(input()) for _ in range(5))
    korean = A // C + (0 if A % C == 0 else 1)
    math = B // D + (0 if B % D == 0 else 1)
    print(L - max(korean, math))


solve()
