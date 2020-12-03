from solutions2020.day2.part1 import solve as solve1
from solutions2020.day2.part2 import solve as solve2


test_input = [
    [(1, 3), "a", "abcde"],
    [(1, 3), "b", "cdefg"],
    [(2, 9), "c", "ccccccccc"],
]

def test_part1():
    assert solve1(test_input) == 2

def test_part2():
    assert solve2(test_input) == 1
