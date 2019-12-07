from solutions2019.day4.part1 import solve as solve1
from solutions2019.day4.part2 import solve as solve2


def test1():
    assert solve1(111111)
    assert not solve1(223450)
    assert not solve1(123789)


def test2():
    assert solve2(112233)
    assert not solve2(123444)
    assert solve2(111122)
    assert not solve2(156667)
