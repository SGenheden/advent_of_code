from solutions2017.day16.utils import iter_dance


def solve(moves, init_programs=None):
    return next(iter_dance(moves, init_programs))


if __name__ == "__main__":
    import fileinput

    inp = ("".join([line.strip() for line in fileinput.input()])).split(",")
    print(f"The final configuration is {solve(inp)}")
