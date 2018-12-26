from solutions2017.day8.utils import iter_registers


def solve(instructions):
    registers = None
    for registers in iter_registers(instructions):
        continue
    return max(registers.values())


if __name__ == "__main__":
    import fileinput

    instructions = [line.strip() for line in fileinput.input()]
    print(f"The maximum value of any register is {solve(instructions)}")
