def solve(word_list):
    nvalid = 0
    for line in word_list:
        words = line.strip().split()
        words_unique = set(words)
        if len(words) == len(words_unique):
            nvalid += 1
    return nvalid


if __name__ == "__main__":
    import fileinput

    nvalid = solve([line for line in fileinput.input()])
    print(f"There are {nvalid} password phrases")
