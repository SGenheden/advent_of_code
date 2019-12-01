import math

def solve(number):
    result = float(number) / 3
    result = math.floor(result)
    return result - 2


if __name__ == "__main__":
    import fileinput

    summa = 0
    for line in fileinput.input():
        summa += solve(line.strip())
    print(f"The sum is {summa}")