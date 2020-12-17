from utils import cycle


def print_layout(coordinates):
    maxx = max(c[0] for c in coordinates)
    maxy = max(c[1] for c in coordinates)
    maxz = max(c[2] for c in coordinates)
    minx = min(c[0] for c in coordinates)
    miny = min(c[1] for c in coordinates)
    minz = min(c[2] for c in coordinates)

    for z in range(minz, maxz + 1):
        print(f"\nz={z}")
        for y in range(miny, maxy + 1):
            for x in range(minx, maxx + 1):
                if (x, y, z) in coordinates:
                    print("#", end="")
                else:
                    print(".", end="")
            print("")


def solve(initial_setup):
    return cycle(initial_setup)


if __name__ == "__main__":
    import fileinput

    setup = "".join(line for line in fileinput.input())
    print(solve(setup))
