# 2824 - 최대공약수


def get_gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def solve():
    _ = input()
    A = eval(" * ".join(input().split()))
    _ = input()
    B = eval(" * ".join(input().split()))

    print(str(get_gcd(A, B))[-9:])


solve()
