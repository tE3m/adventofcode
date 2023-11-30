from collections import deque
open_close = {
    ")": ["(", 3],
    "}": ["{", 1197],
    "]": ["[", 57],
    ">": ["<", 25137]
}


def main():
    corrupted = []
    with open("input.txt") as file:
        for line in file.readlines():
            queue = deque()
            for character in list(line.strip()):
                if len(queue) != 0 and character in open_close.keys():
                    last_elem = queue.pop()
                    if last_elem != open_close[character][0]:
                        corrupted.append(character)
                        break
                else:
                    queue.append(character)
    print(str(sum(open_close[character][1] for character in corrupted)))


if __name__ == '__main__':
    main()
