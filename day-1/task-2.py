def main():
    input_lines = open("input.txt").readlines()
    counter = 0
    previous_window = None
    for index in range(len(input_lines)):
        window = sum(int(x) for x in input_lines[index: index + 3])
        if previous_window is not None and window > previous_window:
            counter += 1
        previous_window = window
    print(counter)


if __name__ == '__main__':
    main()
