def solve(lines):
    programs = {}

    for line in lines:
        cols = line.strip().split(" -> ")
        program, nr = cols[0].split()
        if program not in programs:
            programs[program] = {"children": [], "nr": None, "ischild": False}
        programs[program]["nr"] = int(nr[1:-1])
        if len(cols) > 1:
            for subprog in cols[1].split(", "):
                programs[program]["children"].append(subprog)
                if subprog not in programs:
                    programs[subprog] = {"children": [], "nr": None, "ischild": False}
                programs[subprog]["ischild"] = True

    for program, spec in programs.items():
        if not spec["ischild"]:
            return program


if __name__ == "__main__":
    import fileinput

    name = solve([line for line in fileinput.input()])
    print(f"The bottom program is {name}")
