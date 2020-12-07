from collections import Counter


def solve(content):
    groups = content.split("\n\n")
    counts = []
    for group in groups:
        group_counts = Counter()
        npeople = 0
        for answer in group.split("\n"):
            group_counts.update(answer)
            npeople += 1
        nall = sum(1 for _, count in group_counts.items() if count == npeople)
        counts.append(nall)
    return sum(counts)


if __name__ == "__main__":
    import fileinput

    lines = [line.strip() for line in fileinput.input()]
    print(solve("\n".join(lines)))
