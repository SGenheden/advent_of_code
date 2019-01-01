import numpy as np

from solutions2017.day21.utils import Pattern, Image


def solve(rule_spec):
    rules = Pattern.parse_patterns(rule_spec)
    image = Image()
    for _ in range(18):
        image.update(rules)
    return np.sum(image.grid == "#")


if __name__ == "__main__":
    import fileinput

    rule_spec = [line.strip() for line in fileinput.input()]
    print(
        f"The number of square that is on is after 18 iterations is {solve(rule_spec)}"
    )
