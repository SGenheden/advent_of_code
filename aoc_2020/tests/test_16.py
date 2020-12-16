from solutions2020.day16.part1 import solve as solve1
from solutions2020.day16.part1 import parser
from solutions2020.day16.part2 import solve as solve2

test_content1 = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

test_content2 = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
22,9,18"""


def test_parse():
    rule_ranges, your_spec, nearby_spec = parser(test_content1)
    assert your_spec == [7, 1, 14]
    assert nearby_spec[0] == [7, 3, 47]
    assert all(key in rule_ranges for key in ["class", "row", "seat"])
    assert rule_ranges["class"] == {1, 2, 3, 5, 6, 7}


def test_part1():
    assert solve1(test_content1) == 71


def test_part2():
    assert solve2(test_content2) == {"row": 11, "class": 12, "seat": 13}
