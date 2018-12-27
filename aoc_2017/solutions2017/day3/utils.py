from collections import deque


def iter_squares(n):
    right = [1, 0]
    up = [0, 1]
    left = [-1, 0]
    down = [0, -1]
    operations = deque([right, up, left, down])

    current = (0, 0)
    taken = {(0, 0): True}
    for i in range(1, n):
        xy = (current[0] + operations[1][0], current[1] + operations[1][1])
        if xy in taken:
            xy = (current[0] + operations[0][0], current[1] + operations[0][1])
        else:
            operations.rotate(-1)
        taken[xy] = True
        yield xy
        current = xy
