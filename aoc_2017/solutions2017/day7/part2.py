
from collections import Counter


def balance_weights(parent, programs):
    weights = [children_weight(child, programs) for child in programs[parent]["children"]]
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
    programs = {}

    for line in lines:
        cols = line.strip().split(" -> ")
        program, nr = cols[0].split()
        if program not in programs:
            programs[program] = {"children": [], "weight": None, "ischild": False}
        programs[program]["weight"] = int(nr[1:-1])
        if len(cols) > 1:
            for subprog in cols[1].split(", "):
                programs[program]["children"].append(subprog)
                if subprog not in programs:
                    programs[subprog] = {"children": [], "weight": None, "ischild": False}
                programs[subprog]["ischild"] = True

    parent = None
    for program, spec in programs.items():
        if not spec["ischild"]:
            parent = program
            break
    balance_weights(parent, programs)

    for program, specs in programs.items():
        if "old_weight" in specs:
            return specs['weight']

test = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)""".split("\n")


if __name__ == "__main__":
    import fileinput
    n = solve([line for line in fileinput.input()])
    #n = solve(test)
    print(f"The new weight would be {n}")
