from parser import parse_content


def has_bag(color, query_color, bag_specs):
    spec = bag_specs[color]
    if not spec:
        return False
    if query_color in spec:
        return True
    else:
        for child_color in spec:
            if has_bag(child_color, query_color, bag_specs):
                return True


def solve(content, query_color="shiny gold"):
    bag_specs = parse_content(content)
    nfound = 0
    for color in bag_specs:
        if has_bag(color, query_color, bag_specs):
            nfound += 1
    return nfound


if __name__ == "__main__":
    import fileinput

    lines = [line.strip() for line in fileinput.input()]
    print(solve("\n".join(lines)))
