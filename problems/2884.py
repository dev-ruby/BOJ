# 2884 - 알람 시계


def solve():
    hour, minute = map(int, input().split())
    minute = minute + hour * 60
    minute = (minute - 45) if minute >= 45 else (minute + 1395)
    hour = minute // 60
    minute = minute % 60
    print(str(hour) + " " + str(minute))


solve()
