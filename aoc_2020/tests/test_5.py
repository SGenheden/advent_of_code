from solutions2020.day5.partition import find_seat
from solutions2020.day5.part1 import solve as solve1


def test_partition():
    assert find_seat("FBFBBFFRLR") == (44, 5)
    assert find_seat("BFFFBBFRRR") == (70, 7)
    assert find_seat("FFFBBBFRRR") == (14, 7)
    assert find_seat("BBFFBBFRLL") == (102, 4)


def test_part1():
    assert solve1("FBFBBFFRLR") == 357
    assert solve1("BFFFBBFRRR") == 567
    assert solve1("FFFBBBFRRR") == 119
    assert solve1("BBFFBBFRLL") == 820
