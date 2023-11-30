if __name__ == '__main__':
    with open("input.txt") as file:
        characters = file.readline()
    for index in range(len(characters)-14):
        if len(set(characters[index:index+14])) == 14:
            print(index+14)
            break
