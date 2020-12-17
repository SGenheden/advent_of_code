from utils import cycle


def solve(initial_setup):
    return cycle(initial_setup, dimensions=4)


if __name__ == "__main__":
    import fileinput

    setup = "".join(line for line in fileinput.input())
    print(solve(setup))
