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
