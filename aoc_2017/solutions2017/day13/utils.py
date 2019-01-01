class Firewall:
    def __init__(self, spec):
        self.scanners = {}
        self.max_range = 0
        for line in spec:
            depth, range = [int(i) for i in line.strip().split(": ")]
            self.max_range = max(self.max_range, range)
            self.scanners[depth] = {"range": range, "pos": 0, "dir": 1}
        self.max_depth = max(self.scanners.keys())

    def iter_steps(self):
        for layer in range(self.max_depth + 1):
            yield layer, self.scanners.get(layer, None)
            self.move()

    def move(self):
        for _, spec in self.scanners.items():
            if spec["pos"] == spec["range"] - 1:
                spec["dir"] = -1
            elif spec["pos"] == 0:
                spec["dir"] = 1
            spec["pos"] += spec["dir"]

    def move_many(self, n):
        for _, spec in self.scanners.items():
            n_to_round_trip = (spec["range"]-2)*2+2
            n_extra = n % n_to_round_trip
            for _ in range(n_extra):
                if spec["pos"] == spec["range"] - 1:
                    spec["dir"] = -1
                elif spec["pos"] == 0:
                    spec["dir"] = 1
                spec["pos"] += spec["dir"]

    def reset(self):
        for _, spec in self.scanners.items():
            spec["pos"] = 0
            spec["dir"] = 1

    def __repr__(self):
        reprs = "".join(str(i) for i in range(self.max_depth + 1))
        for row in range(self.max_range):
            layer_strs = []
            for layer in range(self.max_depth + 1):
                if layer not in self.scanners:
                    layer_strs.append("." if row == 0 else " ")
                else:
                    if (
                        row < self.scanners[layer]["range"]
                        and self.scanners[layer]["pos"] == row
                    ):
                        layer_strs.append("S")
                    elif row < self.scanners[layer]["range"]:
                        layer_strs.append("-")
                    else:
                        layer_strs.append(" ")
            reprs += "\n" + "".join(layer_strs)
        return reprs
