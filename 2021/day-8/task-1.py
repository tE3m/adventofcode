class Display:
    displayed: list
    occasions = 0

    def __init__(self, line: str):
        self.displayed = line.split()
        for combination in self.displayed:
            if len(combination) == 2 or len(combination) == 3 or len(combination) == 4 or len(combination) == 7:
                self.occasions += 1

    def __str__(self):
        return str(self.displayed)

    def __repr__(self):
        return "Display(" + str(self.displayed) + ",  " + str(self.occasions) + ")"


def main():
    with open("input.txt") as file:
        occasions = sum(Display(line.split(" | ")[1].strip()).occasions for line in file.readlines())
    print(occasions)


if __name__ == '__main__':
    main()
