from solutions2021.day1.part1 import solve as solve1
from solutions2021.day1.part2 import solve as solve2

test_input = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]


def test_part1():
    assert solve1(test_input) == 7


def test_part2():
    assert solve2(test_input) == 5
