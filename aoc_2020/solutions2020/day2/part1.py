from collections import Counter

def solve(rows):
    ncorrect = 0
    for limit, key, password in rows:
        lower, upper = limit
        n = Counter(password)[key]
        if lower <= n and n <= upper:
            ncorrect += 1
    return ncorrect


if __name__ == "__main__":
    import fileinput

    rows = []
    for line in fileinput.input():
        limit_str, key_str, password = line.split()
        limit = [int(n) for n in limit_str.split("-")]
        rows.append([limit, key_str[:-1], password])
        if len(rows) == 1:
            print(rows)
    print(solve(rows))
