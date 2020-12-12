from solutions2020.day12.part1 import solve as solve1
from solutions2020.day12.part2 import solve as solve2

test_input = """F10
N3
F7
R90
F11""".splitlines()


def test_part1():
    assert solve1(test_input) == 25


def test_part2():
    assert solve2(test_input) == 286
