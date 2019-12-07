def solve(pairs):
    return sum(traverse(pairs, pairs[node], 0) for node in pairs.keys())


def traverse(pairs, node, n):
    n += 1
    if node not in pairs.keys():
        return n
    else:
        return traverse(pairs, pairs[node], n)


if __name__ == "__main__":
    import fileinput

    pairs = {}
    for line in fileinput.input():
        first, second = line.strip().split(")")
        if second not in pairs:
            pairs[second] = first
        else:
            raise ValueError("Already taken")
    print(f"Number of orbitals: {solve(pairs)}")
