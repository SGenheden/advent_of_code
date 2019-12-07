import networkx as nx


from solutions2019.day6.part1 import solve as solve1
from solutions2019.day6.part2 import solve as solve2


def test1():
    assert (
        solve1(
            {
                "B": "COM",
                "C": "B",
                "D": "C",
                "E": "D",
                "F": "E",
                "G": "B",
                "H": "G",
                "I": "D",
                "J": "E",
                "K": "J",
                "L": "K",
            }
        )
        == 42
    )


def test2():
    pairs = [
        ("COM", "B"),
        ("B", "C"),
        ("C", "D"),
        ("D", "E"),
        ("E", "F"),
        ("B", "G"),
        ("G", "H"),
        ("D", "I"),
        ("E", "J"),
        ("J", "K"),
        ("K", "L"),
        ("K", "YOU"),
        ("I", "SAN"),
    ]
    graph = nx.Graph()
    for first, second in pairs:
        graph.add_edge(first, second)
    assert solve2(graph) == 4
