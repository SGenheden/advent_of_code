def solve(numbers):
    count = 0
    for val1, val2 in zip(numbers[:-1], numbers[1:]):
        if val2 > val1:
            count += 1
    return count


if __name__ == "__main__":
    import sys

    numbers = list(map(int, open(sys.argv[1], "r").read().splitlines()))
    print(solve(numbers))
