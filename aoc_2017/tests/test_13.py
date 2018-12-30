from solutions2017.day13.part1 import solve as solve1
from solutions2017.day13.part2 import solve as solve2

inp = """0: 3
1: 2
4: 4
6: 4""".split(
    "\n"
)


def test_part1():
    assert solve1(inp) == 24


def test_part2():
    assert solve2(inp) == 10
