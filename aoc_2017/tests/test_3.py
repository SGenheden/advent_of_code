
from solutions2017.day3.part1 import solve as solve1
from solutions2017.day3.part2 import solve as solve2


def test_part1():
    assert solve1(1) == 0
    assert solve1(12) == 3
    assert solve1(23) == 2
    assert solve1(1024) == 31


def test_part2():
    assert solve2(20) == 23
    assert solve2(30) == 54
