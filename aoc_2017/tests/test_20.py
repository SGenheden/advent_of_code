from solutions2017.day20.part1 import solve as solve1
from solutions2017.day20.part2 import solve as solve2


inp1 = """p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>""".split(
    "\n"
)

inp2 = """p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>""".split(
    "\n"
)


def test_part1():
    assert solve1(inp1, 20) == 0


def test_part2():
    assert solve2(inp2, 20) == 1
