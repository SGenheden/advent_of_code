import math


def new_vec(x, y, delta_theta):
    r = math.sqrt(x ** 2 + y ** 2)
    theta = math.atan2(y, x) + delta_theta
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return int(round(x)), int(round(y))


def solve(instructions):
    ship_x, ship_y = 0, 0
    way_x, way_y = 10.0, 1.0
    for instruction in instructions:
        code = instruction[0]
        value = int(instruction[1:])
        if code == "F":
            ship_x += way_x * value
            ship_y += way_y * value
        elif code == "N":
            way_y += value
        elif code == "S":
            way_y -= value
        elif code == "E":
            way_x += value
        elif code == "W":
            way_x -= value
        elif code == "L":
            delta = value / 180.0 * math.pi
            way_x, way_y = new_vec(way_x, way_y, delta)
        elif code == "R":
            delta = -value / 180.0 * math.pi
            way_x, way_y = new_vec(way_x, way_y, delta)
    return abs(ship_x) + abs(ship_y)


if __name__ == "__main__":
    import fileinput

    lines = [line.strip() for line in fileinput.input()]
    print(solve(lines))
