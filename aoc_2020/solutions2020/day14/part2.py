import functools
import re
import itertools


def set_bit(bit, value):
    return value | (1 << bit)


def unset_bit(bit, value):
    return value & ~(1 << bit)


def solve(bitmask, memory_slots, memory=None):
    mask_op = []
    floatings = []
    for idx, value in enumerate(reversed(bitmask)):
        if value == "1":
            mask_op.append(functools.partial(set_bit, idx))
        elif value == "X":
            floatings.append(idx)

    memory = memory or {}
    for slot in memory_slots:
        match = re.match(r"mem\[(\d+)\] \= (\d+)", slot)
        if not match:
            raise ValueError(f"Unknown memory row: {slot}")
        address = int(match.groups()[0])
        for op in mask_op:
            address = op(address)
        new_address = address
        for value_vector in itertools.product([0, 1], repeat=len(floatings)):
            for val, bit in zip(value_vector, floatings):
                if val == 0:
                    new_address = unset_bit(bit, new_address)
                else:
                    new_address = set_bit(bit, new_address)
            memory[new_address] = int(match.groups()[1])

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
