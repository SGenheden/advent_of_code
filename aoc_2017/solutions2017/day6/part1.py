def solve(banks):

    visited = {tuple(banks): None}
    n = 0
    while True:
        maxval = max(banks)
        maxi = banks.index(maxval)
        banks[maxi] = 0
        for i in range(maxi + 1, maxi + maxval + 1):
            banks[i % len(banks)] += 1
        n += 1
        banks_tuple = tuple(banks)
        if banks_tuple in visited:
            break
        else:
            visited[banks_tuple] = None
    return n


if __name__ == "__main__":
    banks = list(map(int, "14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4".strip().split()))
    n = solve(banks)
    print(f"Repeated banks found after {n} cycles")
