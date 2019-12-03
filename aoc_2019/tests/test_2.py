from solutions2019.day2.part1 import solve as solve1


def test1():
    assert solve1([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], 9, 10) == [
        3500,
        9,
        10,
        70,
        2,
        3,
        11,
        0,
        99,
        30,
        40,
        50,
    ]
