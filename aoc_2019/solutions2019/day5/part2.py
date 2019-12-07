from solutions2019.utils.intcode import intcode


def solve(sequence, inp):
    return next(intcode(sequence, input_list=[inp]))[0]


if __name__ == "__main__":
    import fileinput

    sequence = [
        int(number) for number in "".join(line for line in fileinput.input()).split(",")
    ]
    output = solve(sequence, 5)
    print(f"Solution is {output}")
