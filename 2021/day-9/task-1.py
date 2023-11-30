def get_adjacent(heightmap: list[list[int]], y_index: int, x_index: int):
    adjacent = []
    if 0 < y_index:
        adjacent.append(heightmap[y_index-1][x_index])
    if y_index < len(heightmap)-1:
        adjacent.append(heightmap[y_index+1][x_index])
    if 0 < x_index:
        adjacent.append(heightmap[y_index][x_index-1])
    if x_index < len(heightmap[y_index])-1:
        adjacent.append(heightmap[y_index][x_index+1])
    return adjacent


def main():
    with open("input.txt") as file:
        heightmap = [[int(digit) for digit in line.strip()] for line in file.readlines()]
    risk_levels = []
    for y_index, y in enumerate(heightmap):
        for x_index, x in enumerate(y):
            adjacent = get_adjacent(heightmap, y_index, x_index)
            if all(True if point > x else False for point in adjacent):
                risk_levels.append(x+1)
    print(sum(risk_levels))


if __name__ == '__main__':
    main()
    