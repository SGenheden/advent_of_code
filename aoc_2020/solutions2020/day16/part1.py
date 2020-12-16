def parser(content):
    rules, your_ticket, nearby_tickets = content.split("\n\n")

    rule_ranges = {}
    for rule in rules.split("\n"):
        name, ranges = rule.split(": ")
        valid_ints = []
        for range_ in ranges.split(" or "):
            first, last = range_.split("-")
            valid_ints.extend(range(int(first), int(last) + 1))
        rule_ranges[name] = set(valid_ints)

    _, your_ints = your_ticket.split("\n")
    your_spec = [int(val) for val in your_ints.split(",")]

    _, *nearby_ints = nearby_tickets.split("\n")
    nearby_spec = []
    for nearby_ints_row in nearby_ints:
        nearby_spec.append([int(val) for val in nearby_ints_row.split(",")])

    return rule_ranges, your_spec, nearby_spec


def solve(content):
    rule_ranges, _, nearby_spec = parser(content)
    invalid = []
    for row in nearby_spec:
        for val in row:
            if not any(val in range_ for range_ in rule_ranges.values()):
                invalid.append(val)
    return sum(invalid)


if __name__ == "__main__":
    import fileinput

    content = "\n".join(line.strip() for line in fileinput.input())
    print(solve(content))
