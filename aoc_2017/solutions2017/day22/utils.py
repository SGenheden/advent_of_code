from collections import defaultdict
from math import floor

directions = {
    (0, -1): {".": (-1, 0), "#": (1, 0), "W": (0, -1), "F": (0, 1)},
    (0, 1): {".": (1, 0), "#": (-1, 0), "W": (0, 1), "F": (0, -1)},
    (-1, 0): {".": (0, 1), "#": (0, -1), "W": (-1, 0), "F": (1, 0)},
    (1, 0): {".": (0, -1), "#": (0, 1), "W": (1, 0), "F": (-1, 0)},
}


def parse_map(inp):
    nodes = defaultdict(lambda: ".")
    pos = (int(floor(len(inp[0]) / 2)), int(floor(len(inp)) / 2))
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            if inp[y][x] == "#":
                nodes[(x, y)] = "#"
    return nodes, pos


def print_nodes(nodes):
    import sys

    minx = min([k[0] for k in nodes.keys()])
    maxx = max([k[0] for k in nodes.keys()])
    miny = min([k[1] for k in nodes.keys()])
    maxy = max([k[1] for k in nodes.keys()])
    for y in range(miny - 5, maxy + 5):
        for x in range(minx - 5, maxx + 5):
            if (x, y) in nodes:
                sys.stdout.write(nodes[(x, y)])
            else:
                sys.stdout.write(".")
        sys.stdout.write("\n")
    print("\n")


def simulate(nodes, pos, steps, callback):
    direction = (0, -1)
    ninfections = 0
    for _ in range(steps):
        direction = directions[direction][nodes[pos]]
        callback(pos, nodes)
        if pos in nodes and nodes[pos] == "#":
            ninfections += 1
        pos = (pos[0] + direction[0], pos[1] + direction[1])
    return ninfections
