from solutions2017.day15.part1 import solve as solve1
from solutions2017.day15.part2 import solve as solve2


def test_part1():
    assert solve1(65, 8921) == 588


def test_part2():
    assert solve2(65, 8921) == 309
