from solutions2017.utils.assembly import AssemblyBase


class SoundAssembly(AssemblyBase):
    def __init__(self):
        super(SoundAssembly, self).__init__()
        self.sound = None

    def _rcv(self, x):
        self.pos += 1
        if self._value_of(x) != 0:
            return self.sound

    def _snd(self, x):
        self.sound = self._value_of(x)
        self.pos += 1


def solve(instructions):
    a = SoundAssembly()
    return next(a.execute(instructions))


if __name__ == "__main__":
    import fileinput

    instructions = [line for line in fileinput.input()]
    print(f"The last value played is {solve(instructions)}")
