from collections import defaultdict

from solutions2017.utils.knot_hash import knot_hash


def find_region(pos, bitstrs, taken):
    region = {pos}
    if taken[pos]:
        return region

    taken[pos] = True
    for inc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        newx, newy = pos[0] + inc[0], pos[1] + inc[1]
        if 0 <= newx < 128 and 0 <= newy < 128 and bitstrs[newy][newx] == "1":
            region.update(find_region((newx, newy), bitstrs, taken))
    return region


def solve(key):
    bitstrs = []
    for row in range(0, 128):
        bstr = bin(int(knot_hash(f"{key}-{row}"), 16))[2:]
        bitstrs.append("0" * (128 - len(bstr)) + bstr)

    nregions = 0
    taken = defaultdict(lambda: False)
    for x in range(0, 128):
        for y in range(0, 128):
            if bitstrs[y][x] == "0" or taken[(x, y)]:
                continue
            find_region((x, y), bitstrs, taken)
            nregions += 1
    return nregions


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        key = sys.argv[1]
    else:
        key = "hwlqcszp"
    print(f"The number of regions are {solve(key)}")
