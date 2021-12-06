from collections import defaultdict


def solve(numbers, times):
    nfishes = defaultdict(int)
    for number in numbers:
        nfishes[number] += 1

    for _ in range(times):
        new_nfishes = defaultdict(int)
        for x in range(8):
            new_nfishes[7 - x] = nfishes[8 - x]
        new_nfishes[6] += nfishes[0]
        new_nfishes[8] = nfishes[0]
        nfishes = new_nfishes
    return sum(new_nfishes.values())


if __name__ == "__main__":
    import sys

    lines = open(sys.argv[1], "r").read().splitlines()
    print(solve([int(number) for number in lines[0].split(",")], 256))
