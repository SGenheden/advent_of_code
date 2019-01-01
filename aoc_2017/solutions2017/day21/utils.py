import numpy as np


class Pattern:
    def __init__(self, init):
        if isinstance(init, np.ndarray):
            self.grid = init
            self.size = init.shape[0]
        else:
            rows = init.split("/")
            self.size = len(rows)
            self.grid = np.zeros([self.size, self.size], dtype=str)
            for i, row in enumerate(rows):
                self.grid[i, :] = list(row)

    @property
    def spec(self):
        return "/".join(["".join(row) for row in self.grid])

    def fliph(self):
        return Pattern(self.grid[:, ::-1])

    def flipv(self):
        return Pattern(self.grid[::-1, :])

    def rotate(self):
        return Pattern(self.grid.T)

    @staticmethod
    def parse_patterns(specs):
        new_patterns = [
            lambda p: p.fliph(),
            lambda p: p.fliph().rotate(),
            lambda p: p.fliph().flipv(),
            lambda p: p.flipv(),
            lambda p: p.flipv().rotate(),
            lambda p: p.rotate(),
            lambda p: p.rotate().fliph(),
            lambda p: p.rotate().fliph().flipv(),
            lambda p: p.rotate().flipv(),
            lambda p: p.rotate().flipv().fliph(),
        ]
        rules = {}
        for spec in specs:
            in_spec, out_spec = spec.strip().split(" => ")
            out_pattern = Pattern(out_spec)
            in_pattern = Pattern(in_spec)
            in_specs = {in_pattern.spec}
            for new_pattern in new_patterns:
                in_specs.add(new_pattern(in_pattern).spec)
            for pattern in in_specs:
                rules[pattern] = out_pattern
        return rules


class Image:
    def __init__(self):
        self.grid = Pattern(".#./..#/###").grid
        self.size = 3

    def update(self, rules):
        if self.size % 2 == 0:
            n = self.size // 2
            small_size = 3
        else:
            n = self.size // 3
            small_size = 4
        new_squares = self._iter_squares(n, small_size - 1)
        self.size = small_size * n
        new_grid = np.zeros([self.size, self.size], dtype=str)
        for i in range(n):
            for j in range(n):
                new_square = rules[Pattern(next(new_squares)).spec]
                new_grid[
                    i * small_size : (i + 1) * small_size,
                    j * small_size : (j + 1) * small_size,
                ] = new_square.grid
        self.grid = new_grid

    def _iter_squares(self, n, size):
        for i in range(n):
            for j in range(n):
                yield self.grid[i * size : (i + 1) * size, j * size : (j + 1) * size]
