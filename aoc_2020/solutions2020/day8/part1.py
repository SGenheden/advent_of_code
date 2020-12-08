def solve(instructions):
    used = set()
    cursor = 0
    accumulator = 0
    while True:
        if cursor in used:
            break
        instr, value_str = instructions[cursor].split(" ")
        value = int(value_str)

        used.add(cursor)
        if instr == "nop":
            cursor += 1
        elif instr == "acc":
            accumulator += value
            cursor += 1
        elif instr == "jmp":
            cursor += value

    return accumulator


if __name__ == "__main__":
    import fileinput

    lines = [line for line in fileinput.input()]
    print(solve(lines))
