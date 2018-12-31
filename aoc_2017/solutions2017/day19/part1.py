from solutions2017.day19.utils import iter_letters


def solve(world):
    return "".join(letter for letter, _ in iter_letters(world))


if __name__ == "__main__":
    import fileinput

    world = [line[:-1] for line in fileinput.input()]
    print(f"The letters seen were {solve(world)}")
