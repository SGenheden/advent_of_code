def count_trees(rows, slope_x, slope_y):
    ncols = len(rows[0])
    x = 0
    y = 0
    ntrees = 0
    while y < len(rows):
        if rows[y][x % ncols] == "#":
            ntrees += 1
        x += slope_x
        y += slope_y
    return ntrees


def solve(rows):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    solution = 1
    for slope_x, slope_y in slopes:
        solution *= count_trees(rows, slope_x, slope_y)
    return solution


if __name__ == "__main__":
    import fileinput

    rows = [line.strip() for line in fileinput.input()]
    print(solve(rows))
