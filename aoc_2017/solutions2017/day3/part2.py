from itertools import product

from solutions2017.day3.utils import iter_squares


def solve(n):
    all_operations = list(product([-1, 1, 0], [-1, 1, 0]))
    values = {(0, 0): 1}

    for xy in iter_squares(n):
        neigh_sum = 0
        for operation in all_operations:
            new_xy = (xy[0] + operation[0], xy[1] + operation[1])
            if new_xy in values:
                neigh_sum += values[new_xy]
        values[xy] = neigh_sum
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
