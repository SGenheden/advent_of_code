import numpy as np
from scipy.spatial.distance import cdist


from solutions2017.day20.utils import parse_input


def solve(inp, conv=10000):
    p, v, a = parse_input(inp)
    for _ in range(conv):
        v += a
        p += v
        dists = cdist(p, p, "hamming")
        sel = np.sum(dists == 0, axis=1) == 1
        v = v[sel, :]
        a = a[sel, :]
        p = p[sel, :]
    return p.shape[0]


if __name__ == "__main__":
    import fileinput

    inp = [line.strip() for line in fileinput.input()]
    print(f"The number of particles left are {solve(inp)}")
