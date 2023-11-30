def main():
    input_lines = open("input.txt").readlines()
    gamma = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    epsilon = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for line in input_lines:
        for index, bit in enumerate(line.strip()):
            if int(bit):
                gamma[index] += 1
    for index in range(len(gamma)):
        if gamma[index] > len(input_lines)/2:
            gamma[index] = "1"
            epsilon[index] = "0"
        else:
            gamma[index] = "0"
            epsilon[index] = "1"
    gamma = int("".join(gamma), 2)
    epsilon = int("".join(epsilon), 2)
    print(gamma * epsilon)


if __name__ == '__main__':
    main()
