def solve(instructions):
    current = 0
    nsteps = 0
    while current < len(instructions) and current >= 0:
        nincrement = instructions[current]
        instructions[current] += 1
        current += nincrement
        nsteps += 1
    return nsteps


if __name__ == "__main__":
    import fileinput

    instructions = list(map(int, [line.strip() for line in fileinput.input()]))
    nsteps = solve(instructions)
    print(f"Got out in {nsteps} steps")
