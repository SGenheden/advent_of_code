from solutions2020.day11.part1 import solve as solve1
from solutions2020.day11.part2 import solve as solve2
from solutions2020.day11.part2 import count_occupied
from solutions2020.day11.utils import parse_input

test_input = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""".splitlines()


def test_part1():
    assert solve1(test_input) == 37


def test_count_occupied():
    layout = parse_input(
        """.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....""".splitlines()
    )
    assert count_occupied(3, 4, layout) == 8

    layout = parse_input(
        """.............
.L.L.#.#.#.#.
.............""".splitlines()
    )
    assert count_occupied(1, 1, layout) == 0
    assert count_occupied(3, 1, layout) == 1

    layout = parse_input(
        """.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.""".splitlines()
    )
    assert count_occupied(3, 3, layout) == 0


def test_part2():
    assert solve2(test_input) == 26
