def solve(depart_time, busses):
    bus_ids = [int(idx) for idx in busses.split(",") if idx != "x"]
    min_diff = 1e6
    min_id = []
    for bus_id in bus_ids:
        bus_time = bus_id * (depart_time // bus_id + 1)
        delta = bus_time - depart_time
        if min_diff > delta:
            min_diff = delta
            min_id = bus_id
    return min_diff * min_id


if __name__ == "__main__":
    import fileinput

    lines = [line.strip() for line in fileinput.input()]
    depart_time = int(lines[0])
    busses = lines[1]
    print(solve(depart_time, busses))
