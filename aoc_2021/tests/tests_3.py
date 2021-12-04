from solutions2021.day3.part1 import solve as solve1
from solutions2021.day3.part2 import solve as solve2

test_rows = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".split(
    "\n"
)


def test_part1():
    assert solve1(test_rows) == 198


def test_part2():
    assert solve2(test_rows) == 230
