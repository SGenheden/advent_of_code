def iter_knot_rounds(n, lengths):
    numbers = list(range(n))
    pos = 0
    skip = 0
    while True:
        for length in lengths:
            if length > 1:
                sel = [numbers[i % n] for i in range(pos, pos + length)]
                sel.reverse()
                for i, seli in enumerate(sel, pos):
                    numbers[i % n] = seli
            pos += length + skip
            skip += 1
        yield numbers


def knot_hash(inp):
    n = 256
    lengths = [ord(i) for i in inp]
    lengths += [17, 31, 73, 47, 23]
    numbers = []
    for k, numbers in enumerate(iter_knot_rounds(n, lengths), 1):
        if k == 64:
            break
    dense_hash = ["%0.2x" % _xor_list(numbers[i : i + 16]) for i in range(0, n, 16)]
    return "".join(dense_hash)


def _xor_list(lst):
    accum = lst[0]
    for i in lst[1:]:
        accum ^= i
    return accum
