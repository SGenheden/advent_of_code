from solutions2020.day1.part1 import solve as solve1
from solutions2020.day1.part2 import solve as solve2

test_input = [
    1721,
    979,
    366,
    299,
    675,
    1456,
]


def test_part1():
    assert solve1(test_input) == 514579


def test_part2():
    assert solve2(test_input) == 241861950
