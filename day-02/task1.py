outcomes = {
    "X": ["B", "A", "C", 1],
    "Y": ["C", "B", "A", 2],
    "Z": ["A", "C", "B", 3]
}

if __name__ == '__main__':
    with open("input.txt") as file:
        lines = [line.strip().strip().split(" ") for line in file.readlines()]
    print(sum(map(lambda line: outcomes[line[1]][3] + outcomes[line[1]].index(line[0])*3, lines)))

