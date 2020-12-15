from solutions2020.day15.part1 import solve as solve1


def test_part1():
    assert solve1([0, 3, 6], 2020) == 436
    assert solve1([1, 3, 2]) == 1
    assert solve1([2, 1, 3]) == 10
