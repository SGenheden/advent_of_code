from solutions2017.day4.part1 import solve as solve1
from solutions2017.day4.part2 import solve as solve2


inp1 = """aa bb cc dd ee
aa bb cc dd aa
aa bb cc dd aaa""".split(
    "\n"
)


inp2 = """abcde fghij
abcde xyz ecdab
a ab abc abd abf abj
iiii oiii ooii oooi oooo
oiii ioii iioi iiio""".split(
    "\n"
)


def test_part1():
    assert solve1(inp1) == 2


def test_part2():
    assert solve2(inp2) == 3
