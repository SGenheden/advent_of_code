def iter_a(number):
    mask = (1 << 16) - 1
    while True:
        number = (number * 16807) % 2_147_483_647
        yield number & mask


def iter_b(number):
    mask = (1 << 16) - 1
    while True:
        number = (number * 48271) % 2_147_483_647
        yield number & mask


def solve(init_a, init_b):
    counter = 0
    for n, (val_a, val_b) in enumerate(zip(iter_a(init_a), iter_b(init_b))):
        if val_a == val_b:
            counter += 1
        if n > 40e6:
            break
    return counter


if __name__ == "__main__":
    import fileinput

    init_a, init_b = (int(line.strip().split()[-1]) for line in fileinput.input())
    print(
        f"The number of times the generators were equal with starting "
        f"values {init_a} and {init_b} where {solve(init_a, init_b)}"
    )
