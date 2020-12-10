def solve(numbers):
    sorted_numbers = sorted(numbers)
    sorted_numbers = [0] + sorted_numbers

    def count_paths(sequence, cache):
        if len(sequence) == 1:
            return 1

        if sequence[0] in cache:
            return cache[sequence[0]]

        count = 0
        if sequence[1] - sequence[0] in [1, 2, 3]:
            count += count_paths(sequence[1:], cache)
        if len(sequence) > 2 and sequence[2] - sequence[0] in [1, 2, 3]:
            count += count_paths(sequence[2:], cache)
        if len(sequence) > 3 and sequence[3] - sequence[0] in [1, 2, 3]:
            count += count_paths(sequence[3:], cache)

        cache[sequence[0]] = count
        return count

    cache = {}
    return count_paths(sorted_numbers, cache)


if __name__ == "__main__":
    import fileinput

    numbers = [int(line.strip()) for line in fileinput.input()]
    print(solve(numbers))
