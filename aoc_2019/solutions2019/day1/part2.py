from solutions2019.day1.part1 import solve as solve1


def solve(number):
    summa = 0
    while True:
        part = solve1(number)
        part = 0 if part <= 0 else part
        summa += part
        if part == 0:
            break
        else:
            number = part
    return summa


if __name__ == "__main__":
    import fileinput

    summa = 0
    for line in fileinput.input():
        summa += solve(line.strip())
    print(f"The sum is {summa}")
