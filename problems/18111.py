# 18111 - 마인크래프트

import sys


def solve():
    N, M, B = map(int, sys.stdin.readline().split())
    table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    h = 0
    t = 10 ** 10
    for i in range(257):  # 높이
        _M, _m = 0, 0  # 최대 최소 블록 수
        for j in range(N):  # 가로
            for k in range(M):  # 세로
                if table[j][k] < i:  # 높이가 i 보다 작다면
                    _m += i - table[j][k]  # 최솟값에 높이의 차 추가
                else:
                    _M += table[j][k] - i  # 최댓값에 높이의 차 추가
        inventory = _M + B
        if inventory < _m:
            continue
        time = 2 * _M + _m
        if time <= t:
            t = time
            h = i
    print(f"{t} {h}")


solve()
