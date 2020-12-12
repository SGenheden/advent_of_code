from utils import parse_input, find_equilibrium


def count_occupied(x, y, layout):
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
        new_x = x + delta_x
        new_y = y + delta_y
        while (new_x, new_y) in layout and layout[(new_x, new_y)] == ".":
            new_x += delta_x
            new_y += delta_y
        noccupied += layout.get((new_x, new_y), "L") == "#"
    return noccupied


def apply_rules(x, y, layout):
    if layout[(x, y)] == ".":
        return "."

    noccupied = count_occupied(x, y, layout)
    if layout[(x, y)] == "L" and noccupied == 0:
        return "#"
    if layout[(x, y)] == "#" and noccupied >= 5:
        return "L"
    return layout[(x, y)]


def solve(lines):
    layout = parse_input(lines)
    return find_equilibrium(layout, apply_rules)


if __name__ == "__main__":
    import fileinput

    lines = [line.strip() for line in fileinput.input()]
    print(solve(lines))
