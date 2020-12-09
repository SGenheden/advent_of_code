from solutions2020.day9.part1 import create_sum
from solutions2020.day9.part1 import solve as solve1
from solutions2020.day9.part2 import solve as solve2

test_data = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576,
]


def test_sum():
    assert create_sum([0, 10, 20]) == {10, 20, 30}


def test_part1():
    list_ = list(range(1, 26))
    assert solve1(list_ + [26], 25) is None
    assert solve1(list_ + [49], 25) is None
    assert solve1(list_ + [100], 25) == 100
    assert solve1(list_ + [50], 25) == 50
    assert solve1(test_data, 5) == 127


def test_part2():
    assert solve2(test_data, 5) == 62
