from solutions2017.day16.utils import iter_moves


def solve(moves, init_programs=None):
    programs = ""
    for programs in iter_moves(moves, init_programs):
        continue
    return programs


if __name__ == "__main__":
    import fileinput

    inp = ("".join([line.strip() for line in fileinput.input()])).split(",")
    print(f"The final configuration is {solve(inp)}")
