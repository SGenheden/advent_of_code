from solutions2017.day16.utils import iter_moves


def solve(moves, init_programs=None, n_limit=1_000_000_000):
    visited = {}
    n = 0
    while n < n_limit:
        programs = ""
        for programs in iter_moves(moves, init_programs):
            continue
        if programs in visited:
            period = n - visited[programs]
            if (n_limit - 1) % period == visited[programs]:
                return programs
        else:
            visited[programs] = n
        init_programs = list(programs)
        n += 1


if __name__ == "__main__":
    import fileinput

    inp = ("".join([line.strip() for line in fileinput.input()])).split(",")
    print(f"The final configuration is {solve(inp)}")
