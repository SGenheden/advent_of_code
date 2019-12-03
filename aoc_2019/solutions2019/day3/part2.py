def find_points(path):
    x, y = 0, 0
    points = {}
    total_steps = 0
    for move in path:
        dir = move[0]
        steps = int(move[1:])
        for _ in range(1, steps + 1):
            if dir == "L":
                x -= 1
            elif dir == "R":
                x += 1
            elif dir == "D":
                y += 1
            elif dir == "U":
                y -= 1
            total_steps += 1
            if (x, y) not in points:
                points[(x, y)] = total_steps
    return points


def solve(path1, path2):
    points1 = find_points(path1)
    points2 = find_points(path2)

    steps = [
        points1[point] + points2[point]
        for point in set(points1.keys()) & set(points2.keys())
    ]
    return min(steps)


if __name__ == "__main__":
    import fileinput

    paths = [line.split(",") for line in fileinput.input()]
    print(f"The minimum is {solve(paths[0], paths[1])}")
