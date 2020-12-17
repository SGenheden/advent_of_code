from solutions2020.day17.part1 import solve as solve1


test_setup = """.#.
..#
###"""


def test_part1():
    assert solve1(test_setup) == 112
