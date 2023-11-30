from string import ascii_letters

if __name__ == '__main__':
    with open("input.txt") as file:
        rucksacks = [line.strip() for line in file.readlines()]
        counter = 0
    for rucksack in rucksacks:
        compartment_length = len(rucksack) // 2
        first = rucksack[compartment_length:]
        second = rucksack[:compartment_length]
        for item in first:
            if item in second:
                counter += ascii_letters.index(item) + 1
                break
    print(counter)

