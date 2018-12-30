from solutions2017.day14.part1 import solve as solve1
from solutions2017.day14.part2 import solve as solve2

inp = """flqrgnkx"""


def test_part1():
    assert solve1(inp) == 8108


def test_part2():
    assert solve2(inp) == 1242
