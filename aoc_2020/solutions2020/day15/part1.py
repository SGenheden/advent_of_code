def solve(seed, nturns=2020):
    spoken = {number: [turn] for turn, number in enumerate(seed, 1)}
    prev = seed[-1]
    for turn in range(len(seed) + 1, nturns + 1):
        if len(spoken[prev]) > 1:
            now = spoken[prev][-1] - spoken[prev][-2]
        else:
            now = 0
        if now in spoken:
            spoken[now].append(turn)
            if len(spoken[now]) == 3:
                spoken[now] = spoken[now][1:]
        else:
            spoken[now] = [turn]
        prev = now
    return prev


if __name__ == "__main__":
    import fileinput

    numbers = [int(line.strip()) for line in fileinput.input()]
    print(solve(numbers))
