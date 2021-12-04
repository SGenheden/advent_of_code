from solutions2021.day2.part1 import solve as solve1
from solutions2021.day2.part2 import solve as solve2

test_commands = [
    ("forward", "5"),
    ("down", "5"),
    ("forward", "8"),
    ("up", "3"),
    ("down", "8"),
    ("forward", "2"),
]


def test_part1():
    assert solve1(test_commands) == 150


def test_part2():
    assert solve2(test_commands) == 900
