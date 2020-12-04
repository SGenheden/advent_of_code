from parser import parse


def _check_byr(password):
    byr = password["byr"]
    try:
        return len(byr) == 4 and int(byr) >= 1920 and int(byr) <= 2002
    except Exception:
        return False


def _check_iyr(password):
    iyr = password["iyr"]
    try:
        return len(iyr) == 4 and int(iyr) >= 2010 and int(iyr) <= 2020
    except Exception:
        return False


def _check_eyr(password):
    eyr = password["eyr"]
    try:
        return len(eyr) == 4 and int(eyr) >= 2020 and int(eyr) <= 2030
    except Exception:
        return False


def _check_hgt(password):
    hgt = password["hgt"]
    if not (hgt.endswith("in") or hgt.endswith("cm")):
        return False

    try:
        number = int(hgt[:-2])
        unit = hgt[-2:]
        if unit == "cm":
            return number >= 150 and number <= 193
        return number >= 59 and number <= 76
    except Exception:
        return False


def _check_hcl(password):
    hcl = password["hcl"]
    if not hcl.startswith("#"):
        return False
    if not len(hcl) == 7:
        return False
    valid = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
    ]
    return all(char for char in valid)


def _check_ecl(password):
    ecl = password["ecl"]
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def _check_pid(password):
    pid = password["pid"]
    if not len(pid) == 9:
        return False
    try:
        _ = int(pid)
    except Exception:
        return False
    return True


def solve(content):
    passwords = parse(content)
    nok = 0
    for password in passwords:
        if not all(
            key in password for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        ):
            continue
        if (
            _check_byr(password)
            and _check_iyr(password)
            and _check_eyr(password)
            and _check_hgt(password)
            and _check_hcl(password)
            and _check_ecl(password)
            and _check_pid(password)
        ):
            nok += 1
    return nok


if __name__ == "__main__":
    import fileinput

    rows = [line.strip() for line in fileinput.input()]
    print(solve("\n".join(rows)))
