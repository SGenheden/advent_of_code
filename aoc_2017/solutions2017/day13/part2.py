from solutions2017.day13.utils import Firewall


def is_caught(firewall, delay):
    firewall.reset()
    for _ in range(delay):
        firewall.move()
    for layer, scanner in firewall.iter_steps():
        if scanner is not None and scanner["pos"] == 0:
            return True
    return False


def solve(spec):
    firewall = Firewall(spec)
    delay = 1
    while True:
        if not is_caught(firewall, delay):
            return delay
        delay += 1


if __name__ == "__main__":
    import fileinput

    spec = [line.strip() for line in fileinput.input()]
    print(f"If we delay {solve(spec)} ps we won't get caught")
