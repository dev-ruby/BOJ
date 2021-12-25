# 16170 - 오늘의 날짜는?

import datetime


def solve():
    now = datetime.datetime.now()

    print(now.year)
    print(now.month if not now.month < 10 else f"0{now.month}")
    print(now.day if not now.day < 10 else f"0{now.day}")


solve()
