from collections import deque
from re import findall

if __name__ == '__main__':
    with open("input.txt") as file:
        line = file.readline()
        stacks = [deque() for _ in range(len(line)//4)]
        while line[1] != "1":
            for index, crate in enumerate(line[1::4]):
                if crate != " ":
                    stacks[index].append(crate)
            line = file.readline()
        file.readline()
        moves = [[int(value) for value in findall(r"\d+", values)] for values in file.readlines()]
    for move in moves:
        stacks[move[2]-1].extendleft([stacks[move[1]-1].popleft() for _ in range(move[0])][::-1])
    print("".join(stack[0] for stack in stacks))
