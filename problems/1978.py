# 1978 - 소수 찾기


def is_prime_number(n):
    if n == 2:
        return True
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def solve():
    N = int(input())
    prime_list = map(int, input().split())
    count = 0
    for i in prime_list:
        if is_prime_number(i):
            count += 1
    print(count)


solve()
