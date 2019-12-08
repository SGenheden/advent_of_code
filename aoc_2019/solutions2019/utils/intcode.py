def intcode(sequence):
    i = 0
    output = None
    while True:
        instr = ("000000" + str(sequence[i]))[::-1]
        optcode = int(instr[:2][::-1])
        modes = instr[2:]
        if optcode == 99:  # halt
            return output
        elif optcode == 1:  # addition
            val1 = sequence[sequence[i + 1]] if modes[0] == "0" else sequence[i + 1]
            val2 = sequence[sequence[i + 2]] if modes[1] == "0" else sequence[i + 2]
            if modes[2] == "0":
                sequence[sequence[i + 3]] = val1 + val2
            i += 4
        elif optcode == 2:  # multiplication
            val1 = sequence[sequence[i + 1]] if modes[0] == "0" else sequence[i + 1]
            val2 = sequence[sequence[i + 2]] if modes[1] == "0" else sequence[i + 2]
            if modes[2] == "0":
                sequence[sequence[i + 3]] = val1 * val2
            i += 4
        elif optcode == 3:  # input
            inp = yield output
            if modes[0] == "0":
                sequence[sequence[i + 1]] = inp
            i += 2
        elif optcode == 4:  # output
            if modes[0] == "0":
                output = sequence[sequence[i + 1]]
            else:
                output = sequence[i + 1]
            i += 2
        elif optcode == 5:  # jump-if-true
            val1 = sequence[sequence[i + 1]] if modes[0] == "0" else sequence[i + 1]
            val2 = sequence[sequence[i + 2]] if modes[1] == "0" else sequence[i + 2]
            if val1 != 0:
                i = val2
            else:
                i += 3
        elif optcode == 6:  # jump-if-false
            val1 = sequence[sequence[i + 1]] if modes[0] == "0" else sequence[i + 1]
            val2 = sequence[sequence[i + 2]] if modes[1] == "0" else sequence[i + 2]
            if val1 == 0:
                i = val2
            else:
                i += 3
        elif optcode == 7:  # less than
            val1 = sequence[sequence[i + 1]] if modes[0] == "0" else sequence[i + 1]
            val2 = sequence[sequence[i + 2]] if modes[1] == "0" else sequence[i + 2]
            if modes[2] == "0":
                sequence[sequence[i + 3]] = 1 if val1 < val2 else 0
            i += 4
        elif optcode == 8:  # equal
            val1 = sequence[sequence[i + 1]] if modes[0] == "0" else sequence[i + 1]
            val2 = sequence[sequence[i + 2]] if modes[1] == "0" else sequence[i + 2]
            if modes[2] == "0":
                sequence[sequence[i + 3]] = 1 if val1 == val2 else 0
            i += 4


def intcode_passthrough(sequence, *input_signals):
    program = intcode(sequence)
    try:
        next(program)
        for signal in input_signals:
            program.send(signal)
    except StopIteration as stop:
        return stop.value


def str2sequence(str_):
    return list(map(int, str_.split(",")))
