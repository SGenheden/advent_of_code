from collections import Counter

from solutions2017.day7.utils import parse_program_tree, find_root


def balance_weights(parent, programs):
    weights = [
        children_weight(child, programs) for child in programs[parent]["children"]
    ]
    counts = Counter(weights)

    if len(counts) == 1:
        return sum(weights)
    elif len(counts) != 2:
        raise ValueError("Algorithm failed!")

    maxcount = max(counts.values())
    common_weight = None
    uncommon_weight = None
    for weight, count in counts.items():
        if count == maxcount:
            common_weight = weight
        else:
            uncommon_weight = weight
    delta = common_weight - uncommon_weight
    idx = weights.index(uncommon_weight)
    child = programs[parent]["children"][idx]
    programs[child]["old_weight"] = programs[child]["weight"]
    programs[child]["weight"] += delta
    weights[idx] += delta
    return sum(weights)


def children_weight(parent, programs):
    weight = programs[parent]["weight"]
    if programs[parent]["children"]:
        weight += balance_weights(parent, programs)
    return weight


def solve(lines):
    programs = parse_program_tree(lines)
    parent = find_root(programs)
    balance_weights(parent, programs)

    for program, specs in programs.items():
        if "old_weight" in specs:
            return specs["weight"]


if __name__ == "__main__":
    import fileinput

    n = solve([line for line in fileinput.input()])
    print(f"The new weight would be {n}")
