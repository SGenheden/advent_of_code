from solutions2017.day8.part1 import solve as solve1
from solutions2017.day8.part2 import solve as solve2

inp = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10""".split(
    "\n"
)


def test_part1():
    assert solve1(inp) == 1


def test_part2():
    assert solve2(inp) == 10
