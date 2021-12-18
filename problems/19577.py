# 19577 - 수학은 재밌어


def get_divisor(N):
    N = int(N)
    divisors = []
    divisors_back = []

    for i in range(1, int(N ** 0.5) + 1):
        if not N % i:
            divisors.append(i)
            if i != (N // i):
                divisors_back.append(N // i)

    return divisors + divisors_back[::-1]


def euler_phi(N):
    phi = int(N > 0 and N)
    for i in range(2, int(N ** 0.5) + 1):
        if not N % i:
            phi -= phi // i
            while not N % i:
                N //= i
    if N > 1:
        phi -= phi // N
    return phi


def solve():
    N = int(input())

    if N == 1:
        print(1)
        return

    divisor = get_divisor(N)
    for i in divisor:
        if i * euler_phi(i) == N:
            print(i)
            return
    print(-1)


solve()
