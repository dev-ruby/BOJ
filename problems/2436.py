# 2436 - 공약수

import math


def solve():
    GCD, LCM = map(int, input().split())
    answer = (LCM, LCM)
    temp = (0, 0)
    for A in range(math.ceil(math.sqrt(LCM // GCD)), 0, -1):
        if LCM % (GCD * A) == 0:
            B = LCM // (GCD * A)
            temp = (A * GCD, B * GCD)
            if math.gcd(A, B) == 1 and sum(temp) < sum(answer):
                answer = temp
    print(f"{min(answer)} {max(answer)}")


solve()
