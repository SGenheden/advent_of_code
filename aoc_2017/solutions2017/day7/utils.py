def find_root(programs):
    for program, spec in programs.items():
        if not spec["ischild"]:
            return program


def parse_program_tree(lines):
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
                    programs[subprog] = {
                        "children": [],
                        "weight": None,
                        "ischild": False,
                    }
                programs[subprog]["ischild"] = True
    return programs
