from solutions2017.day22.utils import parse_map, simulate


def advanced_callback(pos, nodes):
    if nodes[pos] == "F":
        del nodes[pos]
    elif nodes[pos] == "W":
        nodes[pos] = "#"
    elif nodes[pos] == "#":
        nodes[pos] = "F"
    else:
        nodes[pos] = "W"


def solve(inp, steps=10_000_000):
    nodes, pos = parse_map(inp)
    return simulate(nodes, pos, steps, advanced_callback)


if __name__ == "__main__":
    import fileinput

    inp = [line.strip() for line in fileinput.input()]
    print(f"The number of infections after 10000000 bursts are {solve(inp)}")
