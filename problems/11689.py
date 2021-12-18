# 11689 - GCD(n, k) = 1

# 오일러 피 함수 활용, ϕ(N) = K의 개수


def euler_phi(N):
    phi = int(N > 0 and N)
    for p in range(2, int(N ** 0.5) + 1):
        if not N % p:
            phi -= phi // p
            while not N % p:
                N //= p
    if N > 1:
        phi -= phi // N
    return phi


def solve():
    N = int(input())
    print(euler_phi(N))


solve()
