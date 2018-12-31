from string import ascii_uppercase


def inside(pos, world):
    return (
        0 <= pos[1] < len(world)
        and 0 <= pos[0] < len(world[pos[1]])
        and world[pos[1]][pos[0]] != " "
    )


def update_inc(pos, inc, world):
    trials = [(0, 1), (0, -1)] if abs(inc[0]) == 1 else [(1, 0), (-1, 0)]
    for trial in trials:
        succ = (pos[0] + trial[0], pos[1] + trial[1])
        if inside(succ, world):
            return trial


def iter_letters(world):
    pos = (world[0].find("|"), 0)
    inc = (0, 1)
    n = 0
    while inside(pos, world):
        curr = world[pos[1]][pos[0]]
        if ascii_uppercase.find(curr) > -1:
            yield curr, n
            n = 0
        elif curr == "+":
            inc = update_inc(pos, inc, world)
        pos = (pos[0] + inc[0], pos[1] + inc[1])
        n += 1
    yield "", n
