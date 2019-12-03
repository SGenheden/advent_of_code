def find_points(path):
    x, y = 0, 0
    points = []
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
            points.append((x, y))
    print(points)
    return set(points)


def solve(path1, path2):
    points1 = find_points(path1)
    points2 = find_points(path2)
    distances = [abs(point[0]) + abs(point[1]) for point in points1 & points2]
    return min(distances)


if __name__ == "__main__":
    import fileinput

    paths = [line.split(",") for line in fileinput.input()]
    print(f"The distance is {solve(paths[0], paths[1])}")
