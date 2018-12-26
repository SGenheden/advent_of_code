
from solutions2017.day1.part1 import solve as solve1
from solutions2017.day1.part2 import solve as solve2


def test_part1():
    assert solve1("1122") == 3
    assert solve1("1111") == 4
    assert solve1("1234") == 0
    assert solve1("91212129") == 9


def test_part2():
    assert solve2("1212") == 6
    assert solve2("1221") == 0
    assert solve2("123425") == 4
    assert solve2("123123") == 12
    assert solve2("12131415") == 4
