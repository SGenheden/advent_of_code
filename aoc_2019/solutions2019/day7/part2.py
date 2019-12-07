import itertools

from solutions2019.utils.intcode import intcode


def create_amps(program_sequence, *phases):
    amps = []
    for phase in phases:
        amp = {"phase": phase, "prog": None, "final": None}
        amp["prog"] = intcode(list(program_sequence))
        next(amp["prog"])
        amp["prog"].send(phase)
        amps.append(amp)
    return amps


def solve(program_sequence):
    max_output = None
    max_phases = None
    for p1, p2, p3, p4, p5 in itertools.permutations(range(5, 10)):
        signal = 0
        amps = create_amps(program_sequence, p1, p2, p3, p4, p5)
        nfinished = 0
        for amp in itertools.cycle(amps):
            signal = amp["prog"].send(signal)
            if isinstance(signal, tuple):
                signal = signal[0]
                nfinished += 1
                if nfinished == 5:
                    break
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
