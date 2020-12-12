import math


def solve(instructions):
    pos_x, pos_y = 0, 0
    angle = 360
    for instruction in instructions:
        code = instruction[0]
        value = int(instruction[1:])
        if code == "F":
            radians = math.pi / 180.0 * angle
            pos_x += int(math.cos(radians)) * value
            pos_y -= int(math.sin(radians)) * value
        elif code == "N":
            pos_y += value
        elif code == "S":
            pos_y -= value
        elif code == "E":
            pos_x += value
        elif code == "W":
            pos_x -= value
        elif code == "L":
            angle -= value
        elif code == "R":
            angle += value
    return abs(pos_x) + abs(pos_y)


if __name__ == "__main__":
    import fileinput

    lines = [line.strip() for line in fileinput.input()]
    print(solve(lines))
