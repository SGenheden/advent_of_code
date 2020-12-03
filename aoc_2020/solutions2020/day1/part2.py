import itertools


def solve(numbers):
    for val1, val2, val3 in itertools.product(numbers, repeat=3):
        if val1 + val2 + val3 == 2020:
            return val1 * val2 * val3


if __name__ == "__main__":
    import sys

    numbers = list(map(int, open(sys.argv[1], "r").read().splitlines()))
    print(solve(numbers))
