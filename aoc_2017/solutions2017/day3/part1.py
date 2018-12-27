from solutions2017.day3.utils import iter_squares


def solve(n):
    xy = (0, 0)
    for xy in iter_squares(n):
        pass
    dist = abs(xy[0]) + abs(xy[1])
    return dist


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        n = 347_991
    else:
        n = int(sys.argv[1])

    dist = solve(n)
    print(f"Distance from {n} to 1 is {dist}")
