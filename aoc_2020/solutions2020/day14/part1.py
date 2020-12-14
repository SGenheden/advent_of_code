import functools
import re


def set_bit(bit, value):
    return value | (1 << bit)


def unset_bit(bit, value):
    return value & ~(1 << bit)


def solve(bitmask, memory_slots, memory=None):
    mask_op = []
    for idx, value in enumerate(reversed(bitmask)):
        if value == "1":
            mask_op.append(functools.partial(set_bit, idx))
        elif value == "0":
            mask_op.append(functools.partial(unset_bit, idx))

    memory = memory or {}
    for slot in memory_slots:
        match = re.match(r"mem\[(\d+)\] \= (\d+)", slot)
        if not match:
            raise ValueError(f"Unknown memory row: {slot}")
        value = int(match.groups()[1])
        for op in mask_op:
            value = op(value)
        memory[match.groups()[0]] = value

    return memory


if __name__ == "__main__":
    import fileinput

    lines = [line.strip() for line in fileinput.input()]
    _, bit_mask = lines[0].split(" = ")
    memory = {}
    memory_slots = []
    for line in lines[1:]:
        if line.startswith("mask"):
            memory = solve(bit_mask, memory_slots, memory)
            _, bit_mask = line.split(" = ")
            memory_slots = []
        else:
            memory_slots.append(line)
    memory = solve(bit_mask, memory_slots, memory)
    print(sum(memory.values()))
