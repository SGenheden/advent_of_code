from solutions2017.day24.utils import find_bridges, make_components


def solve(components_spec):
    components = make_components(components_spec)
    bridges = []
    find_bridges([(-1, 0)], components, bridges)
    scores = []
    for bridge in bridges:
        scores.append(sum([sum(c) for c in bridge[1:]]))
    return max(scores)


if __name__ == "__main__":
    import fileinput

    spec = [line.strip() for line in fileinput.input()]
    print(f"The strongest bridges has a strength of {solve(spec)}")
