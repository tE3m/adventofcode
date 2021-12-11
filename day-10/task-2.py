from collections import deque
open_close = {
    "(": [")", 3],
    "{": ["}", 1197],
    "[": ["]", 57],
    "<": [">", 25137]
}


def main():
    score = []
    with open("input.txt") as file:
        lines = file.readlines()
    for line in lines:
        queue = deque()
        for character in list(line):
            if character == "\n":
                completion = [open_close[opening][0] for opening in reversed(queue)]
                temp_score = 0
                for closing in completion:
                    temp_score *= 5
                    if closing == ")":
                        temp_score += 1
                    elif closing == "]":
                        temp_score += 2
                    elif closing == "}":
                        temp_score += 3
                    else:
                        temp_score += 4
                score.append(temp_score)
            elif len(queue) != 0 and character not in open_close.keys():
                last_elem = queue.pop()
                if character != open_close[last_elem][0]:
                    break
            else:
                queue.append(character)
    print(str(sorted(score)[int(len(score)/2)]))


if __name__ == '__main__':
    main()
