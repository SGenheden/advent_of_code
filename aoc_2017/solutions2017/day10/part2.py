from solutions2017.utils.knot_hash import knot_hash


def solve(inp):
    return knot_hash(inp)


if __name__ == "__main__":
    import fileinput

    inp = "".join(line.strip() for line in fileinput.input())
    print(f"The knot hash is {solve(inp)}")
