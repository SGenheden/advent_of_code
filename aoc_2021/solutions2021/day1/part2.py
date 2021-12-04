def solve(numbers):
    count = 0
    for offset in range(len(numbers) - 3):
        val1 = sum(numbers[offset + idx] for idx in range(3))
        val2 = sum(numbers[offset + idx + 1] for idx in range(3))
        print(val1, val2)
        if val2 > val1:
            count += 1
    return count


if __name__ == "__main__":
    import sys

    numbers = list(map(int, open(sys.argv[1], "r").read().splitlines()))
    print(solve(numbers))
