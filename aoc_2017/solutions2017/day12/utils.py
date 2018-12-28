def find_clique(root, graph, visited):
    programs = {root}
    if graph[root] and root not in visited:
        visited[root] = None
        for child in graph[root]:
            programs.update(find_clique(child, graph, visited))
        return programs
    return programs


def parse_input(lines):
    graph = {}
    for line in lines:
        program, children = line.strip().split(" <-> ")
        program = int(program)
        graph[program] = [int(i) for i in children.split(", ")]
    return graph
