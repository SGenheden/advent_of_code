import itertools


def no_anagrams(words):
    for word1, word2 in itertools.product(words, words):
        if word1 == word2 or len(word1) != len(word2):
            continue
        sorted1 = "".join(sorted(list(word1)))
        sorted2 = "".join(sorted(list(word2)))
        if sorted1 == sorted2:
            return False
    return True


def solve(word_list):
    nvalid = 0
    for line in word_list:
        words = line.strip().split()
        words_unique = set(words)
        if len(words) == len(words_unique) and no_anagrams(words):
            nvalid += 1
    return nvalid


if __name__ == "__main__":
    import fileinput

    nvalid = solve([line for line in fileinput.input()])
    print(f"There are {nvalid} password phrases")
