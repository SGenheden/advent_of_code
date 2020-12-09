def create_sum(numbers):
    sums = set()
    for i, inum in enumerate(numbers):
        for jnum in numbers[i + 1 :]:
            sums.add(inum + jnum)
    return sums


def solve(numbers, premable_len):
    for idx, number in enumerate(numbers[premable_len:], premable_len):
        if number not in create_sum(numbers[idx - premable_len : idx]):
            return number


if __name__ == "__main__":
    import fileinput

    numbers = [int(line.strip()) for line in fileinput.input()]
    print(solve(numbers, 25))
