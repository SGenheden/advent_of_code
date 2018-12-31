from collections import defaultdict


class AssemblyBase:
    def __init__(self):
        self.registers = defaultdict(lambda: 0)
        self.pos = None

    def execute(self, instructions):
        instructions = [i.strip().split() for i in instructions]
        self.pos = 0
        while 0 <= self.pos < len(instructions):
            method = getattr(self, "_" + instructions[self.pos][0])
            ret = method(*instructions[self.pos][1:])
            if ret is not None:
                yield ret

    def _add(self, x, y):
        self.registers[x] += self._value_of(y)
        self.pos += 1

    def _mod(self, x, y):
        self.registers[x] %= self._value_of(y)
        self.pos += 1

    def _mul(self, x, y):
        self.registers[x] *= self._value_of(y)
        self.pos += 1

    def _jgz(self, x, y):
        if self._value_of(x) > 0:
            self.pos += self._value_of(y)
        else:
            self.pos += 1

    def _rcv(self, x):
        raise NotImplementedError

    def _set(self, x, y):
        self.registers[x] = self._value_of(y)
        self.pos += 1

    def _snd(self, x):
        raise NotImplementedError

    def _value_of(self, x):
        try:
            return int(x)
        except ValueError:
            return self.registers[x]
