from solutions2017.day23.part1 import solve as solve1

# from solutions2017.day22.part2 import solve as solve2


instructions = """set e 2
set g d
mul g e
sub g b
mul g e""".split(
    "\n"
)


def test_part1():
    assert solve1(instructions) == 2
