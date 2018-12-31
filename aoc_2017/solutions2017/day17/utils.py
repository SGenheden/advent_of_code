from blist import blist


def calc_buffer(step, maxval):
    buffer = blist([0])
    curr = 0
    for value in range(1, maxval + 1):
        if curr > 0:
            curr += step
            curr %= len(buffer)
        buffer.insert(curr + 1, value)
        curr += 1
    return buffer, curr
