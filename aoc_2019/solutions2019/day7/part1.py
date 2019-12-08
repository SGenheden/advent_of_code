import itertools

from solutions2019.utils.intcode import intcode_passthrough


def solve(program_sequence):
    max_output = None
    max_phases = None
    for p1, p2, p3, p4, p5 in itertools.permutations(range(0, 5)):
        signal = 0
        for phase in [p1, p2, p3, p4, p5]:
            signal = intcode_passthrough(list(program_sequence), phase, signal)
        if max_output is None or signal > max_output:
            max_output = signal
            max_phases = [p1, p2, p3, p4, p5]
    return max_output, max_phases


if __name__ == "__main__":
    import fileinput

    sequence = [
        int(number) for number in "".join(line for line in fileinput.input()).split(",")
    ]
    max_output, max_phases = solve(sequence)
    print(f"Max output {max_output}")
