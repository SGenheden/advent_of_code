from collections import Counter

from solutions2017.utils.knot_hash import knot_hash


def solve(key):
    bitstr = bin(int(knot_hash(key + "-0"), 16))[2:]
    counts = Counter(bitstr)
    for row in range(1, 128):
        bitstr = bin(int(knot_hash(f"{key}-{row}"), 16))[2:]
        counts.update(bitstr)
    return counts["1"]


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        key = sys.argv[1]
    else:
        key = "hwlqcszp"
    print(f"The number of occupied squares are {solve(key)}")
