def solve(content):
    groups = content.split("\n\n")
    counts = [len(set(group.replace("\n", ""))) for group in groups]
    return sum(counts)


if __name__ == "__main__":
    import fileinput

    lines = [line.strip() for line in fileinput.input()]
    print(solve("\n".join(lines)))
