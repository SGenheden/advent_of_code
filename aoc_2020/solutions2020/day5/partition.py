def find_seat(specification):
    rows = list(range(128))
    for spec in specification[:7]:
        n = len(rows)
        if spec == "F":
            rows = rows[: n // 2]
        else:
            rows = rows[n // 2 :]

    columns = list(range(8))
    for spec in specification[7:]:
        n = len(columns)
        if spec == "L":
            columns = columns[: n // 2]
        else:
            columns = columns[n // 2 :]

    return rows[0], columns[0]
