class Tree:
    height: int
    visible: bool

    def __init__(self, height: int) -> None:
        self.height = height
        self.visible = False

    def __lt__(self, other) -> bool:
        assert type(other) == Tree
        return self.height < other.height

    def __repr__(self) -> str:
        return "Tree({}, {})".format(self.height, self.visible)


if __name__ == '__main__':
    with open("input.txt") as file:
        grid: list[list[Tree]] = [[Tree(int(tree)) for tree in line.strip()] for line in file.readlines()]
    counter = 0
    for orientation in (grid, zip(*reversed(grid))):
        for row in orientation:
            highest = max(row)
            for direction in (row, row[::-1]):
                current_height = -1
                for tree in direction:
                    if tree.height > current_height:
                        if not tree.visible:
                            counter += 1
                        current_height = tree.height
                        tree.visible = True
                    if tree.height == highest:
                        break
    print(counter)
