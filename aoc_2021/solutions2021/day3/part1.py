def solve(rows):
    counts = [{"0": 0, "1": 0} for _ in range(len(rows[0]))]
    for row in rows:
        for idx, digit in enumerate(row):
            counts[idx][digit] += 1
    gamma_row = "".join("1" if count["1"] > count["0"] else "0" for count in counts)
    epsilon_row = "".join("0" if count["0"] < count["1"] else "1" for count in counts)
    return int(gamma_row, 2) * int(epsilon_row, 2)


if __name__ == "__main__":
    import sys

    lines = open(sys.argv[1], "r").read().splitlines()
    print(solve(lines))
