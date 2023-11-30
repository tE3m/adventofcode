if __name__ == '__main__':
    with open("input.txt") as file:
        instructions = file.readlines()
    clock = 1
    x = 1
    signal_strengths = []
    for instruction in instructions:
        if instruction[:4] == "addx":
            clock += 1
            if clock % 40 == 20:
                signal_strengths.append(clock*x)
            x += int(instruction[5:])
        clock += 1
        if clock % 40 == 20:
            signal_strengths.append(clock * x)
    print(sum(signal_strengths))
