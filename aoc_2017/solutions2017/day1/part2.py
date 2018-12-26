def solve(digits):
    digits = list(digits)
    n = len(digits)
    digits += digits[: n // 2]
    return sum([int(a) for a, b in zip(digits[0:n], digits[n // 2 :]) if a == b])


if __name__ == "__main__":
    import fileinput

    digits = "".join([line.strip() for line in fileinput.input()])
    summa = solve(digits)
    print(f"The sum is {summa}")
