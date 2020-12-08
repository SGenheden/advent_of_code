from solutions2020.day8.part1 import solve as solve1
from solutions2020.day8.part2 import solve as solve2

test_code = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""".splitlines()


def test_part1():
    assert solve1(test_code) == 5


def test_part2():
    assert solve2(test_code) == 8
