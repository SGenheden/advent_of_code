from solutions2021.day6.part1 import solve as solve1
from solutions2021.day6.part2 import solve as solve2

test_numbers = [3, 4, 3, 1, 2]


def test_part1():
    assert solve1(test_numbers, 80) == 5934


def test_part2():
    assert solve2(test_numbers, 256) == 26984457539
