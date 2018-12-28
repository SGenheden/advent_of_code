from solutions2017.day11.part1 import solve as solve1
from solutions2017.day11.part2 import solve as solve2


def test_part1():
    assert solve1(["ne", "ne", "ne"]) == 3
    assert solve1(["ne", "ne", "sw", "sw"]) == 0
    assert solve1(["ne", "ne", "s", "s"]) == 2
    assert solve1(["se", "sw", "se", "sw", "sw"]) == 3


def test_part2():
    assert solve2(["ne", "ne", "ne"]) == 3
    assert solve2(["ne", "ne", "sw", "sw"]) == 2
    assert solve2(["ne", "ne", "s", "s"]) == 2
    assert solve2(["se", "sw", "se", "sw", "sw"]) == 3
