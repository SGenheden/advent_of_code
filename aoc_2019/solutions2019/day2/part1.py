from solutions2019.utils.intcode import intcode


def solve(sequence, val1, val2):
    sequence[1] = val1
    sequence[2] = val2
    return next(intcode(sequence))[0]


if __name__ == "__main__":
    import fileinput

    sequence = [
        int(number) for number in "".join(line for line in fileinput.input()).split(",")
    ]
    output = solve(sequence, 12, 2)
    print(f"Solution is {output}")
