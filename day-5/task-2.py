def main():
    with open("input.txt") as file:
        ventLines = [[[int(coord) for coord in ventLine.split(",")] for ventLine in line.strip().split(" -> ")] for line in file.readlines()]
    ventCoords = {}
    doubleCoords = []
    for ventLine in ventLines:
        if ventLine[0][0] == ventLine[1][0]:
            xCoord = ventLine[0][0]
            biggerValue = max(ventLine[0][1], ventLine[1][1])
            smallerValue = min(ventLine[0][1], ventLine[1][1])
            for yCoord in range(smallerValue, biggerValue+1):
                if yCoord not in ventCoords.keys():
                    ventCoords[yCoord] = []
                if xCoord in ventCoords[yCoord]:
                    if [xCoord, yCoord] not in doubleCoords:
                        doubleCoords.append([xCoord, yCoord])
                else:
                    ventCoords[yCoord].append(xCoord)
        elif ventLine[0][1] == ventLine[1][1]:
            yCoord = ventLine[0][1]
            if yCoord not in ventCoords.keys():
                ventCoords[yCoord] = []
            biggerValue = max(ventLine[0][0], ventLine[1][0])
            smallerValue = min(ventLine[0][0], ventLine[1][0])
            for xCoord in range(smallerValue, biggerValue+1):
                if xCoord in ventCoords[yCoord]:
                    if [xCoord, yCoord] not in doubleCoords:
                        doubleCoords.append([xCoord, yCoord])
                else:
                    ventCoords[yCoord].append(xCoord)
        else:
            xDirection = int((ventLine[1][0]-ventLine[0][0])/abs(ventLine[1][0]-ventLine[0][0]))
            yDirection = int((ventLine[1][1]-ventLine[0][1])/abs(ventLine[1][1]-ventLine[0][1]))
            for multiplier in range(abs(ventLine[0][0]-ventLine[1][0])+1):
                xCoord = ventLine[0][0]+multiplier*xDirection
                yCoord = ventLine[0][1]+multiplier*yDirection
                if yCoord not in ventCoords.keys():
                    ventCoords[yCoord] = []
                if xCoord in ventCoords[yCoord]:
                    if [xCoord, yCoord] not in doubleCoords:
                        doubleCoords.append([xCoord, yCoord])
                else:
                    ventCoords[yCoord].append(xCoord)
    breakpoint()


if __name__ == '__main__':
    main()
