from solutions2017.day21.part1 import solve as solve1


rules = """../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#""".split(
    "\n"
)


def test_part12():
    assert solve1(rules, 2) == 12
