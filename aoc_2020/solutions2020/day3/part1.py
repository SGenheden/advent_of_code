def solve(rows, slope_x, slope_y):
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


if __name__ == "__main__":
    import fileinput

    rows = [line.strip() for line in fileinput.input()]
    print(solve(rows, 3, 1))
