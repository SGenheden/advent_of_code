def oxygen_generator_rating(rows):
    bit_position = 0
    while len(rows) > 1:
        counts = {"0": 0, "1": 0}
        for row in rows:
            counts[row[bit_position]] += 1
        keep_bit = "1" if counts["1"] >= counts["0"] else "0"
        rows = [row for row in rows if row[bit_position] == keep_bit]
        bit_position += 1
    return rows[0]


def co2_scrubbing_rating(rows):
    bit_position = 0
    while len(rows) > 1:
        counts = {"0": 0, "1": 0}
        for row in rows:
            counts[row[bit_position]] += 1
        keep_bit = "0" if counts["0"] <= counts["1"] else "1"
        rows = [row for row in rows if row[bit_position] == keep_bit]
        bit_position += 1
    return rows[0]


def solve(rows):
    rating1 = oxygen_generator_rating(list(rows))
    rating2 = co2_scrubbing_rating(list(rows))
    return int(rating1, 2) * int(rating2, 2)


if __name__ == "__main__":
    import sys

    lines = open(sys.argv[1], "r").read().splitlines()
    print(solve(lines))
