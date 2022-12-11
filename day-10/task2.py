if __name__ == '__main__':
    with open("input.txt") as file:
        instructions = file.readlines()
    clock = 1
    x = 1
    x_pos = range(x-1, x+2)
    image = ""
    for instruction in instructions:
        image += "#" if clock-1 in x_pos else "."
        if clock == 40:
            image += "\n"
            clock = 0
        clock += 1
        if instruction[:4] == "addx":
            image += "#" if clock-1 in x_pos else "."
            if clock == 40:
                image += "\n"
                clock = 0
            clock += 1
            x += int(instruction[5:])
            x_pos = range(x-1, x+2)
    print(image)
