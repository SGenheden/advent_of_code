movements = {
    "n": (0, 2),
    "ne": (1, 1),
    "se": (1, -1),
    "s": (0, -2),
    "sw": (-1, -1),
    "nw": (-1, 1),
}


def dist_from_zero(pos):
    pos = (abs(pos[0]), abs(pos[1]))
    return pos[0] + (pos[1] - pos[0]) // 2


def iter_positions(steps):
    current = (0, 0)
    for step in steps:
        movement = movements[step]
        new = (current[0] + movement[0], current[1] + movement[1])
        yield new
        current = new
