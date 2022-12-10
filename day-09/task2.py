class Knot:
    x: int
    y: int


class Head(Knot):
    def move(self, direction: str):
        match direction:
            case "L":
                self.x -= 1
            case "R":
                self.x += 1
            case "U":
                self.y += 1
            case "D":
                self.y -= 1


class Body(Knot):
    def follow(self, other):
        assert type(other) == Knot
        x_diff = other.x - self.x
        y_diff = other.y - self.y
        x_abs = abs(x_diff)
        y_abs = abs(y_diff)
        if x_abs > 1 or x_abs and y_abs > 1:
            self.x = self.x + x_diff // x_abs
        if y_abs > 1 or y_abs and x_abs > 1:
            self.y = self.y + y_diff // y_abs


class Tail(Body):
    visited: set
    _x: int
    _y: int
    
    def __init__(self):
        self.visited = set()
        self._x = 0
        self._y = 0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_value: int):
        self.visited.add((self._x, self._y))
        self._x = new_value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_value: int):
        self.visited.add((self._x, self._y))
        self._y = new_value


if __name__ == '__main__':
    with open("input.txt") as file:
        moves = [(line[0], int(line[2:])) for line in file.readlines()]
    tail_position, head_position = [(0, 0)]*2
    visited: set[tuple[int, int]] = set()
    for index, (direction, amount) in enumerate(moves):
        for move in range(amount):
            visited.add(tail_position)

            if not index and not move:
                continue

        visited.add(tail_position)
    print(len(visited))
