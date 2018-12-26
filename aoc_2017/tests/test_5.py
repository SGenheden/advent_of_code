from solutions2017.day5.part1 import solve as solve1
from solutions2017.day5.part2 import solve as solve2


inp = [0, 3, 0, 1, -3]


def test_part1():
    assert solve1(inp) == 5


def test_part2():
    assert solve2(inp) == 8
