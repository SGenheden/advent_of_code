from solutions2017.day24.part1 import solve as solve1
from solutions2017.day24.part2 import solve as solve2


inp = """0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10""".split(
    "\n"
)


def test_part1():
    assert solve1(inp) == 31


def test_part2():
    assert solve2(inp) == 19
