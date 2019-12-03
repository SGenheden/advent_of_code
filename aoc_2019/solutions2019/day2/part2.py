from solutions2019.day2.part1 import solve


if __name__ == "__main__":
    import fileinput

    sequence0 = [
        int(number) for number in "".join(line for line in fileinput.input()).split(",")
    ]
    for noun in range(0, 100):
        for verb in range(0, 100):
            solution = solve(list(sequence0), noun, verb)
            if solution[0] == 19690720:
                print(f"{noun}, {verb}, {100 * noun + verb}")
                quit()
