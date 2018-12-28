from solutions2017.day11.utils import dist_from_zero, iter_positions


def solve(steps):
    last = (0, 0)
    for last in iter_positions(steps):
        continue
    return dist_from_zero(last)


if __name__ == "__main__":
    import fileinput

    step_str = "".join(line.strip() for line in fileinput.input())
    steps = step_str.split(",")
    print(f"The fewest number of steps is {solve(steps)}")
