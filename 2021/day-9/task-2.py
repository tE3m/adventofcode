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


def get_basin(heightmap: list[list[int]], y_index: int, x_index: int, basin: dict = {}):
    if basin == {}:
        basin = {y_position: [] for y_position in range(len(heightmap))}
    if x_index not in basin[y_index]:
        basin[y_index].append(x_index)
    newCoordinates = []
    if 0 < y_index and x_index not in basin[y_index - 1] and heightmap[y_index - 1][x_index] != 9:
        basin[y_index - 1].append(x_index)
        newCoordinates.append([y_index - 1, x_index])
    if y_index < len(heightmap) - 1 and x_index not in basin[y_index + 1] and heightmap[y_index + 1][x_index] != 9:
        basin[y_index + 1].append(x_index)
        newCoordinates.append([y_index + 1, x_index])
    if 0 < x_index and x_index - 1 not in basin[y_index] and heightmap[y_index][x_index - 1] != 9:
        basin[y_index].append(x_index - 1)
        newCoordinates.append([y_index, x_index - 1])
    if x_index < len(heightmap[y_index]) - 1 and x_index + 1 not in basin[y_index] and heightmap[y_index][x_index + 1] != 9:
        basin[y_index].append(x_index + 1)
        newCoordinates.append([y_index, x_index + 1])
    for coordinate in newCoordinates:
        basin = get_basin(heightmap, coordinate[0], coordinate[1], basin)
    return basin


def main():
    with open("input.txt") as file:
        heightmap = [[int(digit) for digit in line.strip()] for line in file.readlines()]
    basins = []
    for y_index, y in enumerate(heightmap):
        for x_index, x in enumerate(y):
            adjacent = get_adjacent(heightmap, y_index, x_index)
            if all(True if point > x else False for point in adjacent):
                basins.append(sum(len(basin) for basin in get_basin(heightmap, y_index, x_index).values()))
    largest, second_largest, third_largest = sorted(basins, reverse=True)[:3]
    print(largest*second_largest*third_largest)


if __name__ == '__main__':
    main()
