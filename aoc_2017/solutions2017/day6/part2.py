

def solve(banks):

    visited = {tuple(banks): 0}
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
            return n - visited[banks_tuple]
        else:
            visited[banks_tuple] = n


if __name__ == "__main__":
    #banks = [0, 2, 7, 0]
    banks = list(map(int, "14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4".strip().split()))
    n = solve(banks)
    print(f"Number of cycles in the infinity loop are {n}")

