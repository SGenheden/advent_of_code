from solutions2017.day7.part1 import solve as solve1
from solutions2017.day7.part2 import solve as solve2

inp = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)""".split(
    "\n"
)


def test_part1():
    assert solve1(inp) == "tknk"


def test_part2():
    assert solve2(inp) == 60
