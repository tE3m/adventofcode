class Tree:
    height: int
    score: int | None

    def __init__(self, height: int) -> None:
        self.height = height
        self.score = None

    def __lt__(self, other) -> bool:
        assert type(other) == Tree
        return self.score < other.score

    def __repr__(self) -> str:
        return "Tree({}, {})".format(self.height, self.score)


if __name__ == '__main__':
    with open("input.txt") as file:
        rows: list[list[Tree]] = [[Tree(int(tree)) for tree in line.strip()] for line in file.readlines()]
    columns = list(zip(*rows))
    for y, row in enumerate(rows):
        for x, tree in enumerate(row):
            distances = []
            for view in (reversed(row[:x]), row[x + 1:], reversed(columns[x][:y]), columns[x][y + 1:]):
                distance = 0
                for other_tree in view:
                    distance += 1
                    if other_tree.height >= tree.height:
                        break
                if not distance:
                    tree.score = 0
                    break
                distances.append(distance)
            if len(distances) == 4:
                tree.score = distances[0] * distances[1] * distances[2] * distances[3]
    print(max(tree for row in rows for tree in row).score)

