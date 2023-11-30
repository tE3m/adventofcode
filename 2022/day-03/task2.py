from string import ascii_letters

if __name__ == '__main__':
    with open("input.txt") as file:
        rucksacks = [line.strip() for line in file.readlines()]
        counter = 0
    for index in range(0, len(rucksacks), 3):
        for item in rucksacks[index]:
            if item in rucksacks[index+1] and item in rucksacks[index+2]:
                counter += ascii_letters.index(item) + 1
                break
    print(counter)
