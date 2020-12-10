def solve(numbers):
    sorted_numbers = sorted(numbers)
    differences = {1: 0, 2: 0, 3: 0}

    differences[sorted_numbers[0]] += 1
    differences[3] += 1

    for num1, num2 in zip(sorted_numbers[:-1], sorted_numbers[1:]):
        differences[num2 - num1] += 1

    return differences[3] * differences[1]


if __name__ == "__main__":
    import fileinput

    numbers = [int(line.strip()) for line in fileinput.input()]
    print(solve(numbers))
