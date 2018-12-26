from solutions2017.day6.part1 import solve as solve1
from solutions2017.day6.part2 import solve as solve2


inp = [0, 2, 7, 0]


def test_part1():
    assert solve1(inp) == 5


def test_part2():
    assert solve2(inp) == 4
