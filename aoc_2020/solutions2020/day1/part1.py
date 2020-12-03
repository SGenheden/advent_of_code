import itertools


def solve(numbers):
    for val1, val2 in itertools.product(numbers, repeat=2):
        if val1 + val2 == 2020:
            return val1 * val2


if __name__ == "__main__":
    import sys

    numbers = list(map(int, open(sys.argv[1], "r").read().splitlines()))
    print(solve(numbers))
