from string import ascii_lowercase


def spin_move(move, programs):
    n = int(move[1:])
    return programs[-n:] + programs[:-n]


def exchange_move(move, programs):
    i, j = [int(val) for val in move[1:].split("/")]
    a = programs[i]
    programs[i] = programs[j]
    programs[j] = a
    return programs


def partner_move(move, programs):
    a = move[1]
    b = move[3]
    i = programs.index(a)
    j = programs.index(b)
    programs[i] = b
    programs[j] = a
    return programs


moves_lookup = {"s": spin_move, "x": exchange_move, "p": partner_move}


def iter_moves(moves, programs=None):
    if programs is None:
        programs = list(ascii_lowercase[:16])
    for move in moves:
        programs = moves_lookup[move[0]](move, programs)
        yield "".join(programs)
