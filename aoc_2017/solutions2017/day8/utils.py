import collections
import operator

op_map = {
    ">": operator.gt,
    "<": operator.lt,
    ">=": operator.ge,
    "<=": operator.le,
    "==": operator.eq,
    "!=": operator.ne,
}


def iter_registers(instructions):
    registers = collections.defaultdict(lambda: 0)
    for inst in instructions:
        register, incflag, val, _, cond_a, op, cond_b = inst.strip().split()
        try:
            val_a = int(cond_a)
        except ValueError:
            val_a = registers[cond_a]
        try:
            val_b = int(cond_b)
        except ValueError:
            val_b = registers[cond_b]
        if op_map[op](val_a, val_b):
            factor = 1 if incflag == "inc" else -1
            registers[register] += factor * int(val)
        yield registers
