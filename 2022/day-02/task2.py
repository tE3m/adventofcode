outcomes = ["X", "Y", "Z"]
combinations = {
    "X": ["B", "A", "C", 1],
    "Y": ["C", "B", "A", 2],
    "Z": ["A", "C", "B", 3]
}

if __name__ == '__main__':
    with open("input.txt") as file:
        lines = [line.strip().strip().split(" ") for line in file.readlines()]
    score = 0
    for line in lines:
        outcome_index = outcomes.index(line[1])
        for key, value in combinations.items():
            if value.index(line[0]) == outcome_index:
                score += outcome_index*3 + value[3]
    print(score)

