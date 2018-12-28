from solutions2017.day9.utils import parse_group


def score_group(group, level):
    score = level
    if group["children"]:
        score += sum(score_group(child, level + 1) for child in group["children"])
    return score


def solve(stream):
    _, tree = parse_group(stream)
    return score_group(tree, 1)


if __name__ == "__main__":
    import fileinput

    stream = "".join(line.strip() for line in fileinput.input())
    print(f"The total score is {solve(stream)}")
