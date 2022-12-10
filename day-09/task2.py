class Knot:
    x: int
    y: int

    def __init__(self):
        self.x = 0
        self.y = 0


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
    previous: Knot

    def __init__(self, previous: Knot):
        super().__init__()
        self.previous = previous
    
    def update(self):
        x_diff = self.previous.x - self.x
        y_diff = self.previous.y - self.y
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
    
    def __init__(self, previous: Knot):
        self._x = 0
        self._y = 0
        self.visited = set()
        super().__init__(previous)

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
    with open("test_input.txt") as file:
        moves = [(line[0], int(line[2:])) for line in file.readlines()]
    head = Head()
    knots = [head]
    for _ in range(8):
        knots.append(Body(knots[-1]))
    tail = Tail(knots[8])
    knots.append(tail)
    completed_moves = 0
    for move_index, (direction_, amount) in enumerate(moves):
        for move in range(amount):
            head.move(direction_)
            for knot in knots[1:completed_moves+1]:
                knot.update()
            completed_moves += 1
    print(tail.visited)
