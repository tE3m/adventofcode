def main():
    input_lines = open("input.txt").readlines()
    x = 0
    y = 0
    for line in input_lines:
        direction, value = line.split(" ")
        value = int(value)
        if direction == "forward":
            x += value
        elif direction == "down":
            y += value
        else:
            y -= value
    print(x*y)


if __name__ == '__main__':
    main()
