from collections import deque
from itertools import product


def solve(n):
    current = (0, 0)
    coordinates = [None] * n
    coordinates[0] = current

    right = [1, 0]
    up = [0, 1]
    left = [-1, 0]
    down = [0, -1]
    operations = deque([right, up, left, down])
    all_operations = list(product([-1, 1, 0], [-1, 1, 0]))
    values = {(0, 0): 1}

    for i in range(1, n):

        xy = (current[0] + operations[1][0], current[1] + operations[1][1])
        if xy in values:
            xy = (current[0] + operations[0][0], current[1] + operations[0][1])
        else:
            operations.rotate(-1)
        neigh_sum = 0
        for operation in all_operations:
            new_xy = (xy[0] + operation[0], xy[1] + operation[1])
            if new_xy in values:
                neigh_sum += values[new_xy]
        coordinates[i] = xy
        values[xy] = neigh_sum
        current = xy
        if neigh_sum > n:
            return neigh_sum


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        n = 347_991
    else:
        n = int(sys.argv[1])

    neigh_sum = solve(n)
    print(f"Value written that is larger than {n} is {neigh_sum}")
