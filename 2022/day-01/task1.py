if __name__ == '__main__':
    with open("input.txt") as file:
        lines = [int(line.strip()) if line != "\n" else -1 for line in file.readlines()]
    elves = [0]
    for line in lines:
        if line == -1:
            elves.append(0)
        else:
            elves[-1] += line
    print(max(elves))
