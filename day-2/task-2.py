def main():
    input_lines = open("input.txt").readlines()
    x = 0
    y = 0
    aim = 0
    for line in input_lines:
        direction, value = line.split(" ")
        value = int(value)
        if direction == "forward":
            x += value
            y += value*aim
        elif direction == "down":
            aim += value
        else:
            aim -= value
    print(x*y)


if __name__ == '__main__':
    main()
