def solve(digits):
    digits = list(digits) + [digits[0]]
    return sum([int(a) for a, b in zip(digits[0:-1], digits[1:]) if a == b])


if __name__ == "__main__":
    import fileinput

    digits = "".join([line.strip() for line in fileinput.input()])
    summa = solve(digits)
    print(f"The sum is {summa}")
