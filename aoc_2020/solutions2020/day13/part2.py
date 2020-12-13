from sympy.ntheory.modular import crt


def solve(busses):
    busses = busses.split(",")
    m = [int(bus_idx) for bus_idx in busses if bus_idx != "x"]
    v = [int(bus_idx) - rank for rank, bus_idx in enumerate(busses) if bus_idx != "x"]
    return crt(m, v)[0]


if __name__ == "__main__":
    import fileinput

    lines = [line.strip() for line in fileinput.input()]
    busses = lines[1]
    print(solve(busses))
