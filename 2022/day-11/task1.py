class Monkey:
    items: list[int]
    operation: tuple[str, str]
    divisor: int
    monkey_true: any
    monkey_false: any
    inspected = 0

    def __repr__(self) -> str:
        return str(self.items)

    def __lt__(self, other) -> bool:
        assert type(other) == Monkey
        return self.inspected < other.inspected

    def inspect(self, level: int) -> int:
        value = level if self.operation[1] == "old" else int(self.operation[1])
        new_level = level + value if self.operation[0] == "+" else level * value
        self.inspected += 1
        return new_level

    def test(self) -> None:
        for item in self.items:
            item = self.inspect(item)
            if item % self.divisor:
                self.monkey_false.items.append(item)
            else:
                self.monkey_true.items.append(item)
        self.items = []


if __name__ == '__main__':
    with open("test_input.txt") as file:
        lines = file.readlines()
    monkeys = [Monkey() for _ in range(len(lines)//7+1)]
    for index, monkey in enumerate(monkeys):
        offset = 7*index
        monkey.items = [int(item) for item in lines[offset+1].strip()[16:].split(", ")]
        monkey.operation = lines[offset+2].strip()[21:].split(" ")
        monkey.divisor = int(lines[offset+3].strip()[19:])
        monkey.monkey_true = monkeys[int(lines[offset+4].strip()[25:])]
        monkey.monkey_false = monkeys[int(lines[offset+5].strip()[26:])]
        pass
    for _ in range(20):
        for monkey in monkeys:
            monkey.test()
    first, second = sorted(monkeys)[len(monkeys)-2:]
    print(first.inspected*second.inspected)
