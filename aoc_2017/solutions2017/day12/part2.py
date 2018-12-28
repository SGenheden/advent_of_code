from solutions2017.day12.utils import parse_input, find_clique


def solve(lines):
    graph = parse_input(lines)
    ncliques = 0
    taken = {k: False for k in graph.keys()}
    for program in graph.keys():
        if taken[program]:
            continue
        clique = find_clique(program, graph, {})
        for id in clique:
            taken[id] = True
        ncliques += 1
    return ncliques


if __name__ == "__main__":
    import fileinput

    lines = [line.strip() for line in fileinput.input()]
    print(f"There are {solve(lines)} groups")
