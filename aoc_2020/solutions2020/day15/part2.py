from part1 import solve as solve1


def solve(seed):
    return solve1(seed, 30000000)


if __name__ == "__main__":
    import fileinput

    numbers = [int(line.strip()) for line in fileinput.input()]
    print(solve(numbers))
