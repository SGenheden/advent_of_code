from solutions2017.day6.utils import iter_banks


def solve(banks):

    visited = {tuple(banks): 0}
    for n, banks_tuple in enumerate(iter_banks(banks), 1):
        if banks_tuple in visited:
            return n - visited[banks_tuple]
        else:
            visited[banks_tuple] = n


if __name__ == "__main__":
    import fileinput

    banks = list(
        map(int, "".join(line.strip() for line in fileinput.input()).strip().split())
    )
    n = solve(banks)
    print(f"Number of cycles in the infinity loop are {n}")
