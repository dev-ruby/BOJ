# 5554 - 심부름 가는 길


def solve():
    print(
        "\n".join(
            map(str, divmod(sum(map(int, (input(), input(), input(), input()))), 60))
        )
    )


solve()
