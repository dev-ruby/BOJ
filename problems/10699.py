# 10699 - 오늘 날짜

import datetime


def solve():
    now = datetime.datetime.now()

    print(
        f"{now.year}-{now.month if now.month >= 10 else f'0{now.month}'}-{now.day if now.day >= 10 else f'0{now.day}'}"
    )


solve()
