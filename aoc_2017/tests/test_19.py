from solutions2017.day19.part1 import solve as solve1
from solutions2017.day19.part2 import solve as solve2

inp = """     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 
"""
world = [line[:-1] for line in inp.split("\n")]


def test_part1():
    assert solve1(world) == "ABCDEF"


def test_part2():
    assert solve2(world) == 38
