def main():
    input_lines = open("input.txt").readlines()
    counter = 0
    previous_line = None
    for line in input_lines:
        line = int(line)
        if previous_line is not None and line > previous_line:
            counter += 1
        previous_line = line
    print(counter)


if __name__ == '__main__':
    main()
