from solutions2020.day6.part1 import solve as solve1
from solutions2020.day6.part2 import solve as solve2

test_content = """abc

a
b
c

ab
ac

a
a
a
a

b"""


def test_1():
    assert solve1(test_content) == 11


def test_2():
    assert solve2(test_content) == 6
