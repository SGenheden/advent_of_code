import itertools

from partition import find_seat


def calc_id(specification):
    row, col = find_seat(specification)
    return row * 8 + col


if __name__ == "__main__":
    import fileinput

    ids = []
    for line in fileinput.input():
        ids.append(calc_id(line.strip()))

    possible_ids = []
    for row, col in itertools.product(range(128), range(8)):
        possible_ids.append(row * 8 + col)

    for missing in set(possible_ids) - set(ids):
        if missing - 1 in ids and missing + 1 in ids:
            print(missing)
            break
