class OctopusMap:
    _map: list[list[int]] = []
    flashes: int = 0

    def __init__(self, filename: str):
        with open(filename) as file:
            self._map = [[int(octopus) for octopus in list(line.strip())] for line in file.readlines()]

    def __str__(self):
        return "".join("".join(str(octopus) + " " for octopus in y) + "\n" for y in self._map)

    def __repr__(self):
        return str(self._map)

    def simulate(self, steps: int):
        for _ in range(steps):
            self._step()

    def _step(self):
        self._map = [[octopus + 1 for octopus in y] for y in self._map]
        already_flashed = []
        for y_index, y in enumerate(self._map):
            for x_index, x in enumerate(y):
                if x > 9:
                    already_flashed = self._flash(y_index, x_index, already_flashed)

    def _flash(self, y_index: int, x_index: int, already_flashed: list[list[int, int]]):
        self._map[y_index][x_index] = 0
        self.flashes += 1
        already_flashed.append([y_index, x_index])
        for square_y in range(y_index - 1, y_index + 2):
            for square_x in range(x_index - 1, x_index + 2):
                if square_y in range(10) and square_x in range(10) and [square_y, square_x] not in already_flashed:
                    self._map[square_y][square_x] += 1
                    if self._map[square_y][square_x] > 9:
                        self._flash(square_y, square_x, already_flashed)
        return already_flashed


if __name__ == '__main__':
    octopusmap = OctopusMap("input.txt")
    octopusmap.simulate(100)
    print(octopusmap.flashes)
