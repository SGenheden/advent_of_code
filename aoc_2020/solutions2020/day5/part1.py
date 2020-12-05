from partition import find_seat


def solve(specification):
    row, col = find_seat(specification)
    return row * 8 + col


if __name__ == "__main__":
    import fileinput

    ids = []
    for line in fileinput.input():
        ids.append(solve(line.strip()))
    print(max(ids))
