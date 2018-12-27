from solutions2017.day6.utils import iter_banks


def solve(banks):
    visited = {tuple(banks): None}
    n = 0
    for n, banks_tuple in enumerate(iter_banks(banks), 1):
        if banks_tuple in visited:
            break
        else:
            visited[banks_tuple] = None
    return n


if __name__ == "__main__":
    import fileinput

    banks = list(
        map(int, "".join(line.strip() for line in fileinput.input()).strip().split())
    )
    n = solve(banks)
    print(f"Repeated banks found after {n} cycles")
