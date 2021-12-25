# 1924 - 2007년

import datetime


def solve():
    m, d = map(int, input().split())
    today = datetime.datetime(2007, m, d)
    print(["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"][today.weekday()])


solve()
