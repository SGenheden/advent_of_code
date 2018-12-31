from solutions2017.day17.utils import calc_buffer


def solve(step):
    buffer, curr = calc_buffer(step, 2017)
    return buffer[(curr + 1) % len(buffer)]


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        key = int(sys.argv[1])
    else:
        key = 314
    print(f"The buffer value after 2017 is {solve(key)}")
