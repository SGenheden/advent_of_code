from solutions2017.day24.utils import find_bridges, make_components


def solve(components_spec):
    components = make_components(components_spec)
    bridges = []
    find_bridges([(-1, 0)], components, bridges)
    max_length = 0
    max_strength = 0
    for bridge in bridges:
        max_length = max(max_length, len(bridge))
        if len(bridge) == max_length:
            strength = sum([sum(c) for c in bridge[1:]])
            max_strength = max(max_strength, strength)
    return max_strength


if __name__ == "__main__":
    import fileinput

    spec = [line.strip() for line in fileinput.input()]
    print(f"The strength of the longest bridges is {solve(spec)}")
