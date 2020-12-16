from collections import defaultdict

from part1 import parser


def solve(content):
    rule_ranges, your_spec, nearby_spec = parser(content)
    invalid = []
    for row in nearby_spec:
        this_invalid = False
        for val in row:
            if not any(val in range_ for range_ in rule_ranges.values()):
                this_invalid = True
        invalid.append(this_invalid)
    nearby_spec = [row for row, invalid in zip(nearby_spec, invalid) if not invalid]

    poss_columns = defaultdict(list)
    for rule_name, rule_range in rule_ranges.items():
        for idx in range(len(rule_ranges)):
            if all(row[idx] in rule_range for row in nearby_spec):
                poss_columns[rule_name].append(idx)

    columns = {}
    while len(poss_columns) > 0:
        min_len = None
        min_key = ""
        for key, list_ in poss_columns.items():
            if min_len is None or len(list_) < min_len:
                min_len = len(list_)
                min_key = key
        take = poss_columns[min_key].pop()
        columns[min_key] = take
        del poss_columns[min_key]
        for key in poss_columns:
            if take in poss_columns[key]:
                poss_columns[key].remove(take)

    retval = {key: your_spec[idx] for key, idx in columns.items()}
    return retval


if __name__ == "__main__":
    import fileinput

    content = "\n".join(line.strip() for line in fileinput.input())
    ret = solve(content)
    product = 1
    for key, val in ret.items():
        if key.startswith("departure"):
            product *= val
    print(product)
