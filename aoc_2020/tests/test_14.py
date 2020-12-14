from solutions2020.day14.part1 import solve as solve1
from solutions2020.day14.part2 import solve as solve2

mask_str = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
memory_slots = """mem[8] = 11
mem[7] = 101
mem[8] = 0""".splitlines()


def test_part1():
    assert sum(solve1(mask_str, memory_slots).values()) == 165


def test_part2():
    mask1 = "000000000000000000000000000000X1001X"
    memory_slots1 = ["mem[42] = 100"]
    mask2 = "00000000000000000000000000000000X0XX"
    memory_slots2 = ["mem[26] = 1"]

    memory = solve2(mask1, memory_slots1)
    assert all(key in memory for key in [26, 27, 58, 59])
    assert len(memory) == 4
    assert sum(memory.values()) == 400

    memory = solve2(mask2, memory_slots2)
    assert all(key in memory for key in [16, 17, 18, 19, 24, 25, 26, 27])
    assert len(memory) == 8
    assert sum(memory.values()) == 8

    memory = solve2(mask1, memory_slots1)
    memory = solve2(mask2, memory_slots2, memory)
    assert sum(memory.values()) == 208
