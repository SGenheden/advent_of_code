def solve(rows):
    checksum = 0
    for line in rows:
        row = list(map(int, line.strip().split()))
        checksum += max(row) - min(row)
    return checksum


if __name__ == "__main__":
    import fileinput

    rows = [line for line in fileinput.input()]
    checksum = solve(rows)
    print(f"Checksum is {checksum}")
