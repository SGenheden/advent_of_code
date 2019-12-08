from solutions2019.utils.intcode import intcode_passthrough


def solve(sequence, inp):
    return intcode_passthrough(sequence, inp)


if __name__ == "__main__":
    import fileinput

    sequence = [
        int(number) for number in "".join(line for line in fileinput.input()).split(",")
    ]
    output = solve(sequence, 5)
    print(f"Solution is {output}")
