class Display:
    digits: list[str]
    displayed: list[str]

    def __init__(self, line: str):
        digits, displayed = line.strip().split(" | ")
        self.digits = digits.split(" ")
        self.displayed = displayed.split(" ")

    def __str__(self):
        return str(self.displayed)

    def __repr__(self):
        return "Display(" + str(self.displayed) + ")"

    @property
    def total(self):
        mapping = self.findCombination()
        count = ""
        for displayed_digit in self.displayed:
            for known_digit in mapping.items():
                if all(letter in known_digit[1] for letter in displayed_digit) and all(letter in displayed_digit for letter in known_digit[1]):
                    count += str(known_digit[0])
                    break
        return int(count)

    def findCombination(self):
        mapping = {number: None for number in range(10)}
        mapping[1] = list(next(digit for digit in self.digits if len(digit) == 2))
        mapping[7] = list(next(digit for digit in self.digits if len(digit) == 3))
        mapping[4] = list(next(digit for digit in self.digits if len(digit) == 4))
        mapping[8] = list(next(digit for digit in self.digits if len(digit) == 7))
        mapping[3] = list(next(digit for digit in self.digits if len(digit) == 5 and all(letter in digit for letter in mapping[1])))
        topleft = next(letter for letter in mapping[4] if letter not in mapping[7] and letter not in mapping[3])
        mapping[5] = list(next(digit for digit in self.digits if len(digit) == 5 and list(digit) != mapping[3] and topleft in digit))
        mapping[2] = list(next(digit for digit in self.digits if len(digit) == 5 and list(digit) not in mapping.values()))
        mapping[6] = list(next(digit for digit in self.digits if len(digit) == 6 and not all(letter in digit for letter in mapping[1])))
        mapping[0] = list(next(digit for digit in self.digits if len(digit) == 6 and list(digit) != mapping[6] and not all(letter in digit for letter in mapping[3])))
        mapping[9] = list(next(digit for digit in self.digits if len(digit) == 6 and list(digit) not in mapping.values()))
        return mapping


def main():
    with open("input.txt") as file:
        total = sum(Display(line).total for line in file.readlines())
    print(total)


if __name__ == '__main__':
    main()
