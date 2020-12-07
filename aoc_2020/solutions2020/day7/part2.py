from parser import parse_content


def count_bags(color, bag_specs):
    spec = bag_specs[color]
    if not spec:
        return 0
    else:
        return sum(
            spec[child_color] * (1 + count_bags(child_color, bag_specs))
            for child_color in spec
        )


def solve(content, query_color="shiny gold"):
    bag_specs = parse_content(content)
    nbags = 0
    for color in bag_specs[query_color]:
        child_count = count_bags(color, bag_specs)
        nbags += bag_specs[query_color][color] * (1 + child_count)
    return nbags


if __name__ == "__main__":
    import fileinput

    lines = [line.strip() for line in fileinput.input()]
    print(solve("\n".join(lines)))
