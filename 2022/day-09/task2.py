class Knot:
    x: int
    y: int

    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    def __repr__(self) -> str:
        return "({}, {})".format(self.x, self.y)


class Head(Knot):
    def move(self, direction: str) -> None:
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

    def __init__(self, previous: Knot) -> None:
        super().__init__()
        self.previous = previous
    
    def update(self) -> None:
        x_diff = self.previous.x - self.x
        y_diff = self.previous.y - self.y
        x_abs = abs(x_diff)
        y_abs = abs(y_diff)
        if x_abs > 1 or x_abs and y_abs > 1:
            self.x = self.x + x_diff // x_abs
        if y_abs > 1 or y_abs and x_abs > 1:
            self.y = self.y + y_diff // y_abs


class Tail(Body):
    visited: set[tuple[int, int]]
    
    def __init__(self, previous: Knot) -> None:
        self.visited = {(0, 0)}
        super().__init__(previous)

    def __str__(self) -> str:
        min_x = min(pos[0] for pos in self.visited)
        max_x = max(pos[0] for pos in self.visited)
        min_y = min(pos[1] for pos in self.visited)
        max_y = max(pos[1] for pos in self.visited)
        buffer = ""
        for y in range(min_y, max_y+1):
            for x in range(min_x, max_x+1):
                buffer += "#" if (x, y) in self.visited else "."
            buffer += "\n"
        return buffer

    def update(self) -> None:
        super().update()
        self.visited.add((self.x, self.y))


if __name__ == '__main__':
    with open("input.txt") as file:
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
    print(tail)
    print(len(tail.visited))
