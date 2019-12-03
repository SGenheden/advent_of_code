def solve(sequence, val1, val2):
    i = 0
    sequence[1] = val1
    sequence[2] = val2
    while True:
        if sequence[i] == 99:
            return sequence
        elif sequence[i] == 1:
            sequence[sequence[i + 3]] = (
                sequence[sequence[i + 1]] + sequence[sequence[i + 2]]
            )
        elif sequence[i] == 2:
            sequence[sequence[i + 3]] = (
                sequence[sequence[i + 1]] * sequence[sequence[i + 2]]
            )
        i += 4


if __name__ == "__main__":
    import fileinput

    sequence = [
        int(number) for number in "".join(line for line in fileinput.input()).split(",")
    ]
    solution = solve(sequence, 12, 2)
    print(f"Solution is {solution[0]}")
