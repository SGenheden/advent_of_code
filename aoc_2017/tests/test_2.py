
from solutions2017.day2.part1 import solve as solve1
from solutions2017.day2.part2 import solve as solve2


inp1="""5 1 9 5
7 5 3
2 4 6 8""".split("\n")


inp2="""5 9 2 8
9 4 7 3
3 8 6 5""".split("\n")


def test_part1():
    assert solve1(inp1) == 18


def test_part2():
    assert solve2(inp2) == 9
