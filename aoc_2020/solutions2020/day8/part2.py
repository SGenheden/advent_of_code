def run_instructions(instructions):
    used = set()
    cursor = 0
    accumulator = 0
    while True:
        if cursor in used:
            return None
        if cursor >= len(instructions):
            return accumulator

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


def solve(instructions):
    indices = [
        idx for idx, instr in enumerate(instructions) if instr[:3] in ["nop", "jmp"]
    ]
    for idx in indices:
        new_instructions = list(instructions)
        if new_instructions[idx][:3] == "jmp":
            new_instructions[idx] = "nop" + new_instructions[idx][3:]
        else:
            new_instructions[idx] = "jmp" + new_instructions[idx][3:]
        ret_val = run_instructions(new_instructions)
        if ret_val is not None:
            return ret_val


if __name__ == "__main__":
    import fileinput

    lines = [line for line in fileinput.input()]
    print(solve(lines))
