class Fish:
    def __init__(self, counter=8):
        self.counter = counter

    def __call__(self):
        self.counter -= 1
        if self.counter == -1:
            self.counter = 6
            return True
        return False


def solve(numbers, times):
    fishes = {Fish(number) for number in numbers}
    for _ in range(times):
        count_new = 0
        for fish in fishes:
            if fish():
                count_new += 1
        fishes = fishes.union({Fish() for _ in range(count_new)})
    return len(fishes)


if __name__ == "__main__":
    import sys

    lines = open(sys.argv[1], "r").read().splitlines()
    print(solve([int(number) for number in lines[0].split(",")], 80))
