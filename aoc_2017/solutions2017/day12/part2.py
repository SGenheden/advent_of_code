from solutions2017.day12.utils import parse_input, find_clique


def solve(lines):
    graph = parse_input(lines)
    ncliques = 0
    taken = {}
    for program in graph.keys():
        if program in taken:
            continue
        find_clique(program, graph, taken)
        ncliques += 1
    return ncliques


if __name__ == "__main__":
    import fileinput

    lines = [line.strip() for line in fileinput.input()]
    print(f"There are {solve(lines)} groups")
