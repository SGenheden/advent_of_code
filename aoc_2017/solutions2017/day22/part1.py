from solutions2017.day22.utils import parse_map, simulate


def simple_callback(pos, nodes):
    if nodes[pos] == "#":
        del nodes[pos]
    else:
        nodes[pos] = "#"


def solve(inp, steps=10000):
    nodes, pos = parse_map(inp)
    return simulate(nodes, pos, steps, simple_callback)


if __name__ == "__main__":
    import fileinput

    inp = [line.strip() for line in fileinput.input()]
    print(f"The number of infections after 10000 bursts are {solve(inp)}")
