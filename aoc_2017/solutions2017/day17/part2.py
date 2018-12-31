from solutions2017.day17.utils import calc_buffer


def solve(step, maxval=50_000_000):
    buffer, _ = calc_buffer(step, maxval)
    zeroi = buffer.index(0)
    return buffer[(zeroi + 1) % len(buffer)]


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        key = int(sys.argv[1])
    else:
        key = 314
    print(f"The value after 0 is {solve(key)}")
