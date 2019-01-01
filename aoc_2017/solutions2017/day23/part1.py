from solutions2017.utils.assembly import AssemblyBase


def solve(instructions):
    a = AssemblyBase()
    list(a.execute(instructions))
    return a.counts["mul"]


if __name__ == "__main__":
    import fileinput

    instructions = [line for line in fileinput.input()]
    print(f"The number of times mul was called is {solve(instructions)}")
