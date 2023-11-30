if __name__ == '__main__':
    with open("input.txt") as file:
        moves = [(line[0], int(line[2:])) for line in file.readlines()]
    tail_position, head_position = [(0, 0)]*2
    visited: set[tuple[int, int]] = set()
    for index, (direction, amount) in enumerate(moves):
        for move in range(amount):
            visited.add(tail_position)
            match direction:
                case "L":
                    head_position = (head_position[0]-1, head_position[1])
                case "R":
                    head_position = (head_position[0]+1, head_position[1])
                case "U":
                    head_position = (head_position[0], head_position[1]+1)
                case "D":
                    head_position = (head_position[0], head_position[1]-1)
            if not index and not move:
                continue
            x_diff = head_position[0] - tail_position[0]
            y_diff = head_position[1] - tail_position[1]
            x_abs = abs(x_diff)
            y_abs = abs(y_diff)
            x_new, y_new = tail_position
            if x_abs > 1 or x_abs and y_abs > 1:
                x_new = tail_position[0] + x_diff // x_abs
            if y_abs > 1 or y_abs and x_abs > 1:
                y_new = tail_position[1] + y_diff // y_abs
            tail_position = (x_new, y_new)
        visited.add(tail_position)
    print(len(visited))
