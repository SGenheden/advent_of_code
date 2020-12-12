def parse_input(lines):
    layout = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            layout[(x, y)] = char
    return layout


def print_layout(layout):
    prev_y = 0
    print("")
    for (x, y), char in layout.items():
        if y != prev_y:
            print("")
        print(char, end="")
        prev_y = y


def find_equilibrium(layout, rules_func):
    while True:
        new_layout = {}
        for x, y in layout:
            new_layout[(x, y)] = rules_func(x, y, layout)

        if layout == new_layout:
            return sum(val == "#" for val in new_layout.values())

        layout = new_layout
