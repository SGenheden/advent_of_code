from solutions2017.day8.utils import iter_registers


def solve(instructions):
    maxval = 0
    for registers in iter_registers(instructions):
        maxval = max(maxval, max(registers.values()))
    return maxval


if __name__ == "__main__":
    import fileinput

    instructions = [line.strip() for line in fileinput.input()]
    print(f"The maximum value of any register is at any point is {solve(instructions)}")
