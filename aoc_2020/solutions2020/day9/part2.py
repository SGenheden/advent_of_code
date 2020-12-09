from part1 import solve as find_number


def solve(numbers, premable_len):
    magic_number = find_number(numbers, premable_len)
    for chunk_len in range(2, 100):
        for idx in range(0, len(numbers) - chunk_len + 1):
            selection = numbers[idx : idx + chunk_len]
            if sum(selection) == magic_number:
                return min(selection) + max(selection)


if __name__ == "__main__":
    import fileinput

    numbers = [int(line.strip()) for line in fileinput.input()]
    print(solve(numbers, 25))
