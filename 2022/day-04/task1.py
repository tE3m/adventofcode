if __name__ == '__main__':
    with open("input.txt") as file:
        pairs = [[[ids for ids in map(int, assignment.split("-"))] for assignment in line.strip().split(",")] for line
                 in file.readlines()]
    counter = 0
    for pair in pairs:
        first, second = pair
        first_range = range(first[0], first[1]+1)
        second_range = range(second[0], second[1]+1)
        if first[0] in second_range and first[1] in second_range or second[0] in first_range and second[1]\
                in first_range:
            counter += 1
    print(counter)
