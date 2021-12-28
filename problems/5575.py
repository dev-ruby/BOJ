# 5575 - 타임 카드


def solve():
    print(
        "\n".join(
            map(
                lambda x: f"{x[0]} {x[1]} {x[2]}",
                map(
                    lambda x: (x // 3600, x // 60 % 60, x % 60),
                    map(
                        lambda x: (x[3] * 3600 + x[4] * 60 + x[5])
                        - (x[0] * 3600 + x[1] * 60 + x[2]),
                        (list(map(int, input().split())) for _ in range(3)),
                    ),
                ),
            )
        )
    )


solve()
