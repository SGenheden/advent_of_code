from solutions2019.day8.part1 import solve as solve1
from solutions2019.day8.part2 import solve as solve2


def test1():
    assert solve1("123456789012", 3, 2) == 1


def test2():
    assert solve2("0222112222120000", 2, 2) == "01\n10"
