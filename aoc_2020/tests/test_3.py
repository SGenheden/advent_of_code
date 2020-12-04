from solutions2020.day3.part1 import solve as solve1
from solutions2020.day3.part2 import solve as solve2


test_input = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]


def test_part1():
    assert solve1(test_input, 3, 1) == 7


def test_part2():
    assert solve2(test_input) == 336
