import re

import numpy as np


def parse_input(inp):
    p = np.zeros([len(inp), 3])
    v = np.zeros([len(inp), 3])
    a = np.zeros([len(inp), 3])
    for i, line in enumerate(inp):
        m = re.match("p=<(.+)>, v=<(.+)>, a=<(.+)>", line)
        p[i, :] = [int(c.strip()) for c in m.group(1).split(",")]
        v[i, :] = [int(c.strip()) for c in m.group(2).split(",")]
        a[i, :] = [int(c.strip()) for c in m.group(3).split(",")]
    return p, v, a
