if __name__ == '__main__':
    with open("input.txt") as file:
        characters = file.readline()
    for index in range(len(characters)-4):
        marker = characters[index:index+4]
        if len(set(marker)) == len(marker):
            print(index+4)
            break
