from collections import deque


def solve(n):
    current = (0, 0)
    coordinates = [None] * n
    coordinates[0] = current

    right = [1, 0]
    up = [0, 1]
    left = [-1, 0]
    down = [0, -1]
    operations = deque([right, up, left, down])
    taken = {(0, 0): True}

    for i in range(1, n):
        xy = (current[0] + operations[1][0], current[1] + operations[1][1])
        if xy in taken:
            xy = (current[0] + operations[0][0], current[1] + operations[0][1])
        else:
            operations.rotate(-1)
        coordinates[i] = xy
        taken[xy] = True
        current = xy

    dist = abs(coordinates[0][0] - coordinates[-1][0]) + abs(coordinates[0][1] - coordinates[-1][1])
    return dist


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        n = 347991
    else:
        n = int(sys.argv[1])

    dist = solve(n)
    print(f"Distance from {n} to 1 is {dist}")
