def iter_banks(banks):
    while True:
        maxval = max(banks)
        maxi = banks.index(maxval)
        banks[maxi] = 0
        for i in range(maxi + 1, maxi + maxval + 1):
            banks[i % len(banks)] += 1
        banks_tuple = tuple(banks)
        yield banks_tuple
