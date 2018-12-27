from solutions2017.day7.utils import parse_program_tree, find_root


def solve(lines):
    programs = parse_program_tree(lines)
    return find_root(programs)


if __name__ == "__main__":
    import fileinput

    name = solve([line for line in fileinput.input()])
    print(f"The bottom program is {name}")
