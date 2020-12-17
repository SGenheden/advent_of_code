import itertools


def parse_initial(initial_setup, dimensions):
    coordinates = set()
    padding = [0] * (dimensions - 2)
    for y, line in enumerate(initial_setup.split("\n")):
        for x, char in enumerate(line):
            if char == "#":
                coordinates.add(tuple([x, y] + padding))
    return coordinates


def cycle(initial_setup, dimensions=3, iterations=6, print_func=None):
    activate_cubes = parse_initial(initial_setup, dimensions)
    offset_list = list(itertools.product([-1, 0, 1], repeat=dimensions))
    origin = tuple([0] * dimensions)

    if print_func:
        print_func(activate_cubes)

    for _ in range(iterations):
        all_cubes = set()
        for coordinates in activate_cubes:
            for offset in offset_list:
                all_cubes.add(tuple(c + o for c, o in zip(coordinates, offset)))

        next_round = set()
        for coordinates in all_cubes:
            nactive = 0
            for offset in offset_list:
                if offset == origin:
                    continue
                query_coordinates = tuple(c + o for c, o in zip(coordinates, offset))
                if query_coordinates in activate_cubes:
                    nactive += 1
            if coordinates in activate_cubes and nactive in [2, 3]:
                next_round.add(coordinates)
            elif coordinates not in activate_cubes and nactive == 3:
                next_round.add(coordinates)

        activate_cubes = next_round
        if print_func:
            print_func(activate_cubes)

    return len(activate_cubes)
