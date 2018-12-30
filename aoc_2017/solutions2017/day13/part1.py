from solutions2017.day13.utils import Firewall


def solve(spec):
    firewall = Firewall(spec)
    severity = 0
    for layer, scanner in firewall.iter_steps():
        if scanner is not None and scanner["pos"] == 0:
            severity += layer * scanner["range"]
    return severity


if __name__ == "__main__":
    import fileinput

    spec = [line.strip() for line in fileinput.input()]
    print(f"The overall severity is {solve(spec)}")
