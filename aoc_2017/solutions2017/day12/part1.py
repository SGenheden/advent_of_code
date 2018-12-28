from solutions2017.day12.utils import parse_input, find_clique


def solve(lines):
    graph = parse_input(lines)
    return len(find_clique(0, graph, {}))


if __name__ == "__main__":
    import fileinput

    lines = [line.strip() for line in fileinput.input()]
    print(f"There are {solve(lines)} programs in the group of program 0")
