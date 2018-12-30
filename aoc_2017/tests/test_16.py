from solutions2017.day16.part1 import solve as solve1
from solutions2017.day16.part2 import solve as solve2

inp = """s1
x3/4
pe/b""".split(
    "\n"
)


def test_part1():
    assert solve1(inp, list("abcde")) == "baedc"


def test_part2():
    assert solve2(inp, list("abcde"), 9) == "baedc"
    assert solve2(inp, list("abcde"), 10) == "ceadb"
    assert solve2(inp, list("abcde"), 11) == "ecbda"
