from solutions2017.utils.assembly import AssemblyBase


def solve(instructions):
    a = AssemblyBase()
    a.registers["a"] = 1
    for n, registers in enumerate(a.execute(instructions, yield_registers=True)):
        print(",".join(str(registers[r]) for r in "abcdefgh"))
        if n > 100:
            break
    return a.registers["h"]


if __name__ == "__main__":
    import fileinput

    instructions = [line for line in fileinput.input()]
    print(f"The value of register h is {solve(instructions)}")
