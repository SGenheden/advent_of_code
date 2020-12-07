from solutions2020.day7.parser import parse_single
from solutions2020.day7.part1 import solve as solve1
from solutions2020.day7.part2 import solve as solve2

test_str = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

test_str2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""


def test_parse_single():
    str_ = "faded blue bags contain no other bags."
    assert parse_single(str_) == {"faded blue": {}}

    str_ = "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags."
    assert parse_single(str_) == {"muted yellow": {"shiny gold": 2, "faded blue": 9}}

    str_ = "dark olive bags contain 3 faded blue bags, 1 dotted black bag."
    assert parse_single(str_) == {"dark olive": {"faded blue": 3, "dotted black": 1}}


def test_part1():
    assert solve1(test_str) == 4


def test_part2():
    assert solve2(test_str) == 32
    assert solve2(test_str2) == 126
