from .parser import parse


def solve(content):
    passwords = parse(content)
    nok = 0
    for password in passwords:
        if all(
            key in password for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        ):
            nok += 1
    return nok


if __name__ == "__main__":
    import fileinput

    rows = [line.strip() for line in fileinput.input()]
    print(solve("\n".join(rows)))
