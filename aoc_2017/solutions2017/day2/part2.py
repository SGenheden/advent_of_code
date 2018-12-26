import itertools


def solve(rows):
    checksum = 0
    for line in rows:
        row = list(map(int, line.strip().split()))
        for i, j in itertools.product(row, row):
            if i == j:
                continue
            elif i % j == 0:
                checksum += i // j
                break
            elif j % i == 0:
                checksum += j // i
                break
    return checksum


if __name__ == "__main__":
    import fileinput

    rows = [line for line in fileinput.input()]
    checksum = solve(rows)
    print(f"Checksum is {checksum}")
