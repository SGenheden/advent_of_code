from solutions2017.day9.utils import parse_group


def count_garbage(group):
    count = sum(len(g) for g in group["garbage"])
    if group["children"]:
        count += sum(count_garbage(child) for child in group["children"])
    return count


def solve(stream):
    _, tree = parse_group(stream)
    return count_garbage(tree)


if __name__ == "__main__":
    import fileinput

    stream = "".join(line.strip() for line in fileinput.input())
    print(f"The total number of garbage is {solve(stream)}")
