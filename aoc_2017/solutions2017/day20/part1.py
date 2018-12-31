import numpy as np


from solutions2017.day20.utils import parse_input


def solve(inp, conv=10000):
    p, v, a = parse_input(inp)
    closest_id = None
    closest_n = 0
    while True:
        v += a
        p += v
        dists = np.abs(p).sum(axis=1)
        closest = np.argmin(dists)

        if closest != closest_id:
            closest_id = closest
            closest_n = 1
        else:
            closest_n += 1
            if closest_n == conv:
                return closest_id


if __name__ == "__main__":
    import fileinput

    inp = [line.strip() for line in fileinput.input()]
    print(f"The particle closest to (0,0,0) has id {solve(inp)}")
