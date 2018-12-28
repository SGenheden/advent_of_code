from solutions2017.day11.utils import dist_from_zero, iter_positions


def solve(steps):
    maxdist = 0
    for pos in iter_positions(steps):
        maxdist = max(maxdist, dist_from_zero(pos))
    return maxdist


if __name__ == "__main__":
    import fileinput

    step_str = "".join(line.strip() for line in fileinput.input())
    steps = step_str.split(",")
    print(f"The fewest number of steps is {solve(steps)}")
