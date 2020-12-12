from utils import parse_input, find_equilibrium


def apply_rules(x, y, layout):
    if layout[(x, y)] == ".":
        return "."

    noccupied = 0
    for delta_x, delta_y in [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
    ]:
        noccupied += layout.get((x + delta_x, y + delta_y), "L") == "#"
    if layout[(x, y)] == "L" and noccupied == 0:
        return "#"
    if layout[(x, y)] == "#" and noccupied >= 4:
        return "L"
    return layout[(x, y)]


def solve(lines):
    layout = parse_input(lines)
    return find_equilibrium(layout, apply_rules)


if __name__ == "__main__":
    import fileinput

    lines = [line.strip() for line in fileinput.input()]
    print(solve(lines))
