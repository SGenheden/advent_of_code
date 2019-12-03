from solutions2019.day1.part1 import solve as solve1
from solutions2019.day1.part2 import solve as solve2


def test_part1():
    assert solve1(12) == 2
    assert solve1(14) == 2
    assert solve1(1969) == 654
    assert solve1(100756) == 33583


def test_part2():
    assert solve2(14) == 2
    assert solve2(1969) == 966
    assert solve2(100756) == 50346
