class Slot:
    __slots__ = ["prev", "succ", "value"]

    def __init__(self):
        self.prev = None
        self.succ = None
        self.value = 0


class Slots:
    def __init__(self):
        self.curr = Slot()

    def __repr__(self):

        slot = self.curr
        while True:
            if slot.prev is None:
                break
            else:
                slot = slot.prev
        valstr = ""
        while slot is not None:
            valstr += str(slot.value)
            slot = slot.succ
        return valstr

    def checksum(self):
        val = self.curr.value
        slot = self.curr.prev
        while slot is not None:
            val += slot.value
            slot = slot.prev
        slot = self.curr.succ
        while slot is not None:
            val += slot.value
            slot = slot.succ
        return val

    def move(self, direction):
        if direction == -1:
            self.move_left()
        else:
            self.move_right()

    def move_left(self):
        if self.curr.prev is None:
            new = Slot()
            new.succ = self.curr
            self.curr.prev = new
        self.curr = self.curr.prev

    def move_right(self):
        if self.curr.succ is None:
            new = Slot()
            new.prev = self.curr
            self.curr.succ = new
        self.curr = self.curr.succ


class State:
    def __init__(self, spec):
        spec = spec.split("\n")
        directions = {"right": 1, "left": -1}
        self.name = self.parse_spec_line(spec[0])
        val0 = int(self.parse_spec_line(spec[1]))
        val1 = int(self.parse_spec_line(spec[5]))
        self.jobs = {
            val0: {
                "val": int(self.parse_spec_line(spec[2])),
                "dir": directions[self.parse_spec_line(spec[3])],
                "next": self.parse_spec_line(spec[4]),
            },
            val1: {
                "val": int(self.parse_spec_line(spec[6])),
                "dir": directions[self.parse_spec_line(spec[7])],
                "next": self.parse_spec_line(spec[8]),
            },
        }

    def execute(self, slots):
        val = slots.curr.value
        job = self.jobs[val]
        slots.curr.value = job["val"]
        slots.move(job["dir"])
        return job["next"]

    @staticmethod
    def parse_spec_line(spec):
        return spec.strip().split()[-1][:-1]


class Blueprint:
    def __init__(self, spec):
        specs = spec.split("\n\n")
        gen_spec = specs[0].split("\n")
        self.state0 = State.parse_spec_line(gen_spec[0])
        self.nsteps = int(gen_spec[1].strip().split()[-2])
        self.states = {}
        for state_spec in specs[1:]:
            state = State(state_spec)
            self.states[state.name] = state

    def execute(self):
        curr = self.state0
        slots = Slots()
        for _ in range(self.nsteps):
            curr = self.states[curr].execute(slots)
        return slots.checksum()


def solve(specs):
    b = Blueprint(specs)
    return b.execute()


if __name__ == "__main__":
    import fileinput

    specs = "".join([line for line in fileinput.input()])
    print(f"The checksum is {solve(specs)}")
