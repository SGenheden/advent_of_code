from solutions2020.day10.part1 import solve as solve1
from solutions2020.day10.part2 import solve as solve2

test_input1 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
test_input2 = [
    28,
    33,
    18,
    42,
    31,
    14,
    46,
    20,
    48,
    47,
    24,
    23,
    49,
    45,
    19,
    38,
    39,
    11,
    1,
    32,
    25,
    35,
    8,
    17,
    7,
    9,
    4,
    2,
    34,
    10,
    3,
]


def test_part1():
    assert solve1(test_input1) == 35
    assert solve1(test_input2) == 220


def test_part2():
    assert solve2(test_input1) == 8
    assert solve2(test_input2) == 19208
