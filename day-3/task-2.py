def mcb(lines: list, bit: int, index):
    return [line for line in lines if line[index] == bit]


def main():
    input_lines = open("input.txt").readlines()
    oxygen = []
    co2 = []
    oxygenLines = input_lines.copy()
    co2Lines = input_lines.copy()
    for index in range(13):
        if type(oxygen) == list or type(co2) == list:
            if type(oxygen) == list and len(oxygenLines) > 1:
                oxygenCounter = 0
                for line in oxygenLines:
                    if int(line[index]):
                        oxygenCounter += 1
                if oxygenCounter >= len(oxygenLines) / 2:
                    oxygen.append("1")
                else:
                    oxygen.append("0")
            elif len(oxygenLines) == 1:
                oxygen = oxygenLines[0]
            if type(co2) == list and len(co2Lines) > 1:
                co2Counter = 0
                for line in co2Lines:
                    if int(line[index]):
                        co2Counter += 1
                if co2Counter >= len(co2Lines) / 2:
                    co2.append("0")
                else:
                    co2.append("1")
            elif len(co2Lines) == 1:
                co2 = co2Lines[0]
        else:
            break
        oxygenLines = mcb(oxygenLines, oxygen[-1], index)
        co2Lines = mcb(co2Lines, co2[-1], index)
    oxygen = int("".join(oxygen.strip()), 2)
    co2 = int("".join(co2), 2)
    print(oxygen * co2)


if __name__ == '__main__':
    main()
