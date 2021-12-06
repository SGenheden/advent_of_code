from solutions2021.day5.part1 import solve as solve1
from solutions2021.day5.part2 import solve as solve2

test_rows = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".split(
    "\n"
)


def test_part1():
    assert solve1(test_rows) == 5


def test_part2():
    assert solve2(test_rows) == 12
