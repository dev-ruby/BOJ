# 1037 - 약수

def solve():
    N = int(input())

    divisor_list = list(map(int, input().split()))
    divisor_list.sort()

    print(divisor_list[0] * divisor_list[-1])

solve()
