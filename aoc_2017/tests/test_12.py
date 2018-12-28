from solutions2017.day12.part1 import solve as solve1
from solutions2017.day12.part2 import solve as solve2

inp = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5""".split(
    "\n"
)


def test_part1():
    assert solve1(inp) == 6


def test_part2():
    assert solve2(inp) == 2
