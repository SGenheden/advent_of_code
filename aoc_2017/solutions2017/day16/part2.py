from solutions2017.day16.utils import iter_dance


def solve(moves, init_programs=None, n_limit=1_000_000_000):
    visited = {}
    for n, programs in enumerate(iter_dance(moves, init_programs)):
        if programs in visited:
            period = n - visited[programs]
            if (n_limit - 1) % period == visited[programs]:
                return programs
        else:
            visited[programs] = n
        if n == n_limit:
            break


if __name__ == "__main__":
    import fileinput

    inp = ("".join([line.strip() for line in fileinput.input()])).split(",")
    print(f"The final configuration is {solve(inp)}")
