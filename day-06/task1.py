if __name__ == '__main__':
    with open("input.txt") as file:
        characters = file.readline()
    for index in range(len(characters)-4):
        if len(set(characters[index:index+4])) == 4:
            print(index+4)
            break
