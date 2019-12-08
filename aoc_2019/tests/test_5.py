from solutions2019.day5.part1 import solve as solve1
from solutions2019.day5.part2 import solve as solve2
from solutions2019.utils.intcode import str2sequence


def test1():
    assert solve1([1002, 4, 3, 4, 33], 1) == None
    assert solve1([3, 0, 4, 0, 99], 5) == 5


def test2():
    seq1 = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    assert solve2(seq1, 8) == 1
    assert solve2(seq1, 7) == 0

    seq2 = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
    assert solve2(seq2, 8) == 0
    assert solve2(seq2, 7) == 1

    seq3 = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
    assert solve2(seq3, 8) == 1
    assert solve2(seq3, 7) == 0

    seq4 = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
    assert solve2(seq4, 8) == 0
    assert solve2(seq4, 7) == 1

    seq5 = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    assert solve2(seq5, 0) == 0
    assert solve2(seq5, 1) == 1

    seq6 = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
    assert solve2(seq6, 1) == 1
    assert solve2(seq6, 0) == 0

    seq7 = str2sequence(
        "3,21,1008,21,8,20,1005,20,22,107,8,21,20,"
        "1006,20,31,1106,0,36,98,0,0,1002,21,"
        "125,20,4,20,1105,1,46,104,999,1105,1,"
        "46,1101,1000,1,20,4,20,1105,1,46,98,99"
    )
    assert solve2(seq7, 7) == 999
    assert solve2(seq7, 8) == 1000
    assert solve2(seq7, 9) == 1001
