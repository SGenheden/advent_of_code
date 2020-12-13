from solutions2020.day13.part1 import solve as solve1
from solutions2020.day13.part2 import solve as solve2


def test_part1():
    assert solve1(939, "7,13,x,x,59,x,31,19") == 295


def test_part2():
    assert solve2("7,13,x,x,59,x,31,19") == 1068781
