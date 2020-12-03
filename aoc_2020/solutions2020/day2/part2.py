from collections import Counter

def solve(rows):
    ncorrect = 0
    for indices, key, password in rows:
        first, second = indices
        ok1 = password[first-1] == key
        ok2 = password[second-1] == key
        if (ok1 and not ok2) or (ok2 and not ok1):
            ncorrect += 1
    return ncorrect


if __name__ == "__main__":
    import fileinput

    rows = []
    for line in fileinput.input():
        indices_str, key_str, password = line.split()
        indices = [int(n) for n in indices_str.split("-")]
        rows.append([indices, key_str[:-1], password])
        if len(rows) == 1:
            print(rows)
    print(solve(rows))
