from solutions2017.day9.part1 import solve as solve1
from solutions2017.day9.part2 import solve as solve2


def test_part1():
    assert solve1("{}") == 1
    assert solve1("{{{}}}") == 6
    assert solve1("{{},{}}") == 5
    assert solve1("{{{},{},{{}}}}") == 16
    assert solve1("{<a>,<a>,<a>,<a>}") == 1
    assert solve1("{{<ab>},{<ab>},{<ab>},{<ab>}}") == 9
    assert solve1("{{<!!>},{<!!>},{<!!>},{<!!>}}") == 9
    assert solve1("{{<a!>},{<a!>},{<a!>},{<ab>}}") == 3


def test_part2():
    assert solve2("{<>}") == 0
    assert solve2("{<random characters>}") == 17
    assert solve2("{<<<<>}") == 3
    assert solve2("{<{!>}>}") == 2
    assert solve2("{<!!>}") == 0
    assert solve2("{<!!!>>}") == 0
    assert solve2('{<{o"i!a,<{i<a>}') == 10
