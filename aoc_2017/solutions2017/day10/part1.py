from solutions2017.utils.knot_hash import iter_knot_rounds


def solve(n, lengths):
    numbers = next(iter_knot_rounds(n, lengths))
    return numbers[0] * numbers[1]


if __name__ == "__main__":
    import fileinput

    lengths_str = "".join(line.strip() for line in fileinput.input())
    lengths = [int(nr) for nr in lengths_str.split(",")]
    print(
        f"The product of the first two numbers in the final list is {solve(256, lengths)}"
    )
