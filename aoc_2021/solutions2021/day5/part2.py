from collections import defaultdict


def solve(rows):
    counts = defaultdict(int)
    for row in rows:
        start, end = row.split(" -> ")
        x1, y1 = [int(v) for v in start.split(",")]
        x2, y2 = [int(v) for v in end.split(",")]

        if x1 == x2 or y1 == y2:
            x1, x2 = min([x1, x2]), max([x1, x2])
            y1, y2 = min([y1, y2]), max([y1, y2])
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    counts[(x, y)] += 1
        else:
            x_change = 1 if x1 < x2 else -1
            y_change = 1 if y1 < y2 else -1
            x, y = x1, y1
            while True:
                counts[(x, y)] += 1
                if (x, y) == (x2, y2):
                    break
                x += x_change
                y += y_change
    return sum(1 for count in counts.values() if count >= 2)


if __name__ == "__main__":
    import sys

    lines = open(sys.argv[1], "r").read().splitlines()
    print(solve(lines))
