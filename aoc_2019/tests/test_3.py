from solutions2019.day3.part1 import solve as solve1
from solutions2019.day3.part2 import solve as solve2


def pest1():
    assert solve1(["R8", "U5", "L5", "D3"], ["U7", "R6", "D4", "L4"]) == 6

    path1 = ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"]
    path2 = ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]
    assert solve1(path1, path2) == 159

    path1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(",")
    path2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(",")
    assert solve1(path1, path2) == 135


def test2():
    assert solve2(["R8", "U5", "L5", "D3"], ["U7", "R6", "D4", "L4"]) == 30

    path1 = ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"]
    path2 = ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]
    assert solve2(path1, path2) == 610

    path1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(",")
    path2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(",")
    assert solve2(path1, path2) == 410
