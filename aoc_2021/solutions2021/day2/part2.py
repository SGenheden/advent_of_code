def solve(commands):
    def down(pos, value):
        return pos[0], pos[1], pos[2] + value

    def up(pos, value):
        return pos[0], pos[1], pos[2] - value

    def forward(pos, value):
        return pos[0] + value, pos[1] + pos[2] * value, pos[2]

    actions = {
        "forward": forward,
        "down": down,
        "up": up,
    }

    pos = (0, 0, 0)
    for action, value in commands:
        pos = actions[action](pos, int(value))
    return pos[0] * pos[1]


if __name__ == "__main__":
    import sys

    lines = open(sys.argv[1], "r").read().splitlines()
    print(solve([line.split() for line in lines]))
