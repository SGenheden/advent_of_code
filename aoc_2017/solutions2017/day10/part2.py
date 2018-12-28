from solutions2017.day10.utils import iter_knot_rounds


def xor_list(lst):
    accum = lst[0]
    for i in lst[1:]:
        accum ^= i
    return accum


def solve(inp):
    n = 256
    lengths = [ord(i) for i in inp]
    lengths += [17, 31, 73, 47, 23]
    numbers = []
    for k, numbers in enumerate(iter_knot_rounds(n, lengths), 1):
        if k == 64:
            break
    dense_hash = ["%0.2x" % xor_list(numbers[i : i + 16]) for i in range(0, n, 16)]
    return "".join(dense_hash)


if __name__ == "__main__":
    import fileinput

    inp = "".join(line.strip() for line in fileinput.input())
    print(f"The knot hash is {solve(inp)}")
