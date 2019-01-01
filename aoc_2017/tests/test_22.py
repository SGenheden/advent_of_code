from solutions2017.day22.part1 import solve as solve1
from solutions2017.day22.part2 import solve as solve2


inp = """..#
#..
...""".split(
    "\n"
)


def test_part1():
    assert solve1(inp, 7) == 5
    assert solve1(inp, 70) == 41
    assert solve1(inp, 10000) == 5587


def test_part2():
    assert solve2(inp, 100) == 26
    assert solve2(inp, 10000000) == 2511944
