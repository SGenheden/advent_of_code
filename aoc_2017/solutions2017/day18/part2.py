from solutions2017.day18.utils import AssemblyBase


class CommAssembly(AssemblyBase):
    def __init__(self, program_id):
        super(CommAssembly, self).__init__()
        self.registers["p"] = program_id
        self.partner = None
        self.messages = []
        self.sent = 0

    def execute(self, instructions):
        self.sent = 0
        yield from super(CommAssembly, self).execute(instructions)

    def _rcv(self, x):
        if len(self.messages) == 0:
            return self.pos
        self.registers[x] = self.messages.pop(0)
        self.pos += 1

    def _snd(self, x):
        self.partner.messages.append(self._value_of(x))
        self.pos += 1
        self.sent += 1


def solve(instructions):
    a0 = CommAssembly(0)
    a1 = CommAssembly(1)
    a0.partner = a1
    a1.partner = a0
    g0 = a0.execute(instructions)
    g1 = a1.execute(instructions)
    while True:
        try:
            next(g0)
            next(g1)
            if len(a0.messages) == 0 and len(a1.messages) == 0:
                break
        except StopIteration:
            break
    return a1.sent


if __name__ == "__main__":
    import fileinput

    instructions = [line for line in fileinput.input()]
    print(f"The number of times program 1 sent was {solve(instructions)}")
