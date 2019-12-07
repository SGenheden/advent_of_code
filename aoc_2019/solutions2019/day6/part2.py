import networkx as nx


def solve(graph):
    print(nx.shortest_path(graph, "YOU", "SAN"))
    return len(nx.shortest_path(graph, "YOU", "SAN")) - 3


if __name__ == "__main__":
    import fileinput

    graph = nx.Graph()
    for line in fileinput.input():
        first, second = line.strip().split(")")
        graph.add_edge(first, second)
    print(f"The shortest path is: {solve(graph)}")
