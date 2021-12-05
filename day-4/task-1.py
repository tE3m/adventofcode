from typing import TextIO


class BingoBoard:
    _board: list[list[int]]
    _firstState: list[list[int]]
    index: int

    def __init__(self, file: TextIO, index: int):
        self.index = index
        self._board = [[int(x.strip()) for x in file.readline().strip().split()] for _ in range(5)]
        self._firstState = self._board.copy()

    def __repr__(self) -> str:
        return "Bingoboard({})".format(self.index)

    def __str__(self) -> str:
        buffer = ""
        for x in self._board:
            for y in x:
                buffer += str(y) + " "
            buffer += "\n"
        return buffer + "\n"

    def firstStateStr(self):
        buffer = ""
        for x in self._firstState:
            for y in x:
                buffer += str(y) + " "
            buffer += "\n"
        return buffer + "\n"

    @property
    def numbers(self) -> list[int]:
        return [x for y in self._board for x in y if type(x) == int]

    def markNumber(self, number: int):
        if number in self.numbers:
            y_value = int(next(index for index, y in enumerate(self._board) if number in y))
            x_value = int(self._board[y_value].index(number))
            self._board[y_value][x_value] = True

    @property
    def isBingo(self):
        for position in range(5):
            if all(map(lambda y: y[position] is True, self._board)):
                return True
        return [True for _ in range(5)] in self._board

    @property
    def score(self):
        return sum(sum(filter(lambda x: type(x) == int, y)) for y in self._board)


class BingoBoardContainer:
    _boards: list[BingoBoard] = []
    numbers: list[int]

    def __init__(self):
        with open("input.txt") as file:
            self.numbers = [int(number) for number in file.readline().split(",")]
            index = 0
            while file.readline() == "\n":
                self._boards.append(BingoBoard(file, index))
                index += 1

    def __repr__(self):
        return "BingoboardContainer({}\n{})".format(self.numbers, self._boards)

    def __str__(self):
        return self.findBingoBoard()

    def findBingoBoard(self):
        for number in self.numbers:
            for board in self._boards:
                board.markNumber(number)
                if board.isBingo:
                    return str(board.score*number)


if __name__ == '__main__':
    bingoBoardContainer = BingoBoardContainer()
    print(bingoBoardContainer)
